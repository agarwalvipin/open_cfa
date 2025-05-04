import os
import re
import sys

import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# --- Configuration ---
FORM_TITLE = "Quant Questions - Week 3"

# --- Google API Setup ---
# If modifying these SCOPES, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/drive.file",  # Needed to create the form
]
# Path to your downloaded credentials.json file
CREDENTIALS_FILE = "gcredentials.json"
TOKEN_FILE = "token.json"


# --- Markdown Parsing ---
def fetch_markdown_content(file_path):
    """
    Fetches the content of a Markdown file from a local path or a GitHub URL.
    """
    if file_path.startswith("http://") or file_path.startswith("https://"):
        response = requests.get(file_path)
        if response.status_code == 200:
            return response.text
        else:
            print(
                f"Error: Unable to fetch file from URL. Status code: {response.status_code}"
            )
            sys.exit(1)
    else:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            sys.exit(1)


def parse_markdown_questions(file_path):
    """
    Parses the Markdown file to extract questions and options.
    """
    questions = []
    content = fetch_markdown_content(file_path)

    # Split into potential question blocks based on the header
    # Using a lookahead assertion to keep the delimiter
    question_blocks = re.split(r"(?=## 🟢 Q\d+ –)", content)

    for block in question_blocks:
        if not block.strip() or not block.startswith("## 🟢"):
            continue

        # Extract question text (between </details> and the first option)
        question_match = re.search(
            r"</details>\s*\n\n(.*?)\n\n- [A-Z]\)", block, re.DOTALL
        )
        if not question_match:
            print(f"Warning: Could not find question text in block:\n{block[:100]}...")
            continue
        question_text = question_match.group(1).strip()

        # Extract options
        options = re.findall(r"- ([A-Z])\) (.*?)(?=\n- [A-Z]\)|$)", block)
        if not options:
            print(
                f"Warning: Could not find options for question: {question_text[:50]}..."
            )
            continue

        # Format options for Google Forms API (list of strings)
        option_list = [f"{opt[1].strip()}" for opt in options]  # Just the text

        questions.append({"text": question_text, "options": option_list})

    return questions


# --- Google Forms API Interaction ---
def authenticate_google_forms():
    """Handles Google API authentication."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing token: {e}")
                print(f"Deleting {TOKEN_FILE} and re-authenticating.")
                os.remove(TOKEN_FILE)
                creds = None  # Force re-authentication
        if not creds:  # Need to run the flow
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"Error: {CREDENTIALS_FILE} not found.")
                print(
                    "Please download your OAuth 2.0 client credentials from the Google Cloud Console"
                )
                print(
                    "and save the file as 'credentials.json' in the same directory as this script."
                )
                return None
            # Correctly indented block starts here (level 3 indentation - 12 spaces)
            # Explicitly define the redirect_uri for the console flow
            redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES,
                redirect_uri=redirect_uri,  # Add the redirect URI here
            )
            # Use run_console() instead of run_local_server
            print("\nPlease open the following URL in your browser to authorize:")
            # Get authorization url and state
            auth_url, _ = flow.authorization_url(
                prompt="consent"
            )  # Added prompt='consent' for clarity
            print(auth_url)  # Corrected indentation (level 3)
            print(
                "\nEnter the authorization code shown in your browser after approval:"
            )  # Corrected indentation (level 3)
            # Get the authorization code from the user
            code = input(
                "Paste the authorization code here: "
            ).strip()  # Corrected indentation (level 3)
            # Fetch the token using the provided code
            try:  # Corrected indentation (level 3)
                flow.fetch_token(code=code)
                creds = flow.credentials  # Get credentials after fetching token
            except Exception as e:  # Corrected indentation (level 3)
                print(f"Error fetching token using code: {e}")
                creds = None  # Ensure creds is None on error

        # Save the credentials for the next run only if obtained successfully (level 2 indentation - 8 spaces)
        if creds:
            with open(TOKEN_FILE, "w") as token:
                token.write(creds.to_json())
        else:
            print("Failed to obtain credentials using console flow.")
            return None  # Return None if auth failed

    return creds


def create_google_form(creds, title, questions_data):
    """Creates a new Google Form and adds questions."""
    try:
        # Build the service objects
        forms_service = build("forms", "v1", credentials=creds)
        drive_service = build(
            "drive", "v3", credentials=creds
        )  # Needed for initial creation

        # Create the initial form structure
        form = {
            "info": {
                "title": title,
                "documentTitle": title,  # Sets the filename in Drive
            }
        }

        # Create the form using Drive API (Forms API doesn't have a direct create method)
        print("Creating new Google Form...")
        created_form_metadata = (
            drive_service.files()
            .create(
                body={"name": title, "mimeType": "application/vnd.google-apps.form"},
                fields="id",
            )
            .execute()
        )
        form_id = created_form_metadata.get("id")
        print(f"Form created with ID: {form_id}")

        # Remove the default 'Untitled Question' created by Google Forms
        form_metadata = forms_service.forms().get(formId=form_id).execute()
        items = form_metadata.get("items", [])
        if items:
            delete_request = {
                "requests": [
                    {
                        "deleteItem": {
                            "location": {
                                "index": 0
                            }  # Use index to delete the first item
                        }
                    }
                ]
            }
            forms_service.forms().batchUpdate(
                formId=form_id, body=delete_request
            ).execute()
            print("Default 'Untitled Question' removed.")

        # Sanitize question text and options to remove newlines
        sanitized_questions = []
        for q_data in questions_data:
            sanitized_text = q_data["text"].replace("\n", " ").strip()
            sanitized_options = [
                opt.replace("\n", " ").strip() for opt in q_data["options"]
            ]
            sanitized_questions.append(
                {"text": sanitized_text, "options": sanitized_options}
            )

        # Update form description to show the total number of questions
        form_description = (
            f"This form contains a total of {len(sanitized_questions)} questions."
        )
        form_update_body = {
            "requests": [
                {
                    "updateFormInfo": {
                        "info": {"description": form_description},
                        "updateMask": "description",
                    }
                }
            ]
        }
        forms_service.forms().batchUpdate(
            formId=form_id, body=form_update_body
        ).execute()

        # Ensure the index is properly set for each question and include question numbers
        requests = []  # Initialize the requests list outside the loop
        for i, q_data in enumerate(sanitized_questions):
            question_number = f"Q{i + 1}: "  # Add question number prefix
            requests.append(
                {
                    "createItem": {
                        "item": {
                            "title": question_number + q_data["text"],
                            "questionItem": {
                                "question": {
                                    "required": True,  # Make questions required by default
                                    "choiceQuestion": {
                                        "type": "RADIO",  # Multiple choice
                                        "options": [
                                            {"value": opt} for opt in q_data["options"]
                                        ],
                                    },
                                }
                            },
                        },
                        "location": {"index": i},  # Correctly set the index
                    }
                }
            )

        # Add questions to the form using Forms API batchUpdate
        if requests:
            print(f"Adding {len(requests)} questions to the form...")
            batch_update_body = {"requests": requests}
            forms_service.forms().batchUpdate(
                formId=form_id, body=batch_update_body
            ).execute()
            print("Questions added successfully.")
        else:
            print("No questions found to add.")

        # Get the URL of the created form
        form_metadata = forms_service.forms().get(formId=form_id).execute()
        form_url = form_metadata.get("responderUri")
        print("\nGoogle Form created successfully!")
        print(f"View/Edit URL: https://docs.google.com/forms/d/{form_id}/edit")
        if form_url:
            print(f"Shareable URL for responders: {form_url}")

        return form_id, form_url

    except HttpError as error:
        print(f"An API error occurred: {error}")
        print(f"Details: {error.content}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None


# --- Main Execution ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 create_google_form.py <MARKDOWN_FILE_PATH>")
        sys.exit(1)

    MARKDOWN_FILE_PATH = sys.argv[1]
    markdown_content = fetch_markdown_content(MARKDOWN_FILE_PATH)

    # Deduce FORM_TITLE from the Markdown file name
    if MARKDOWN_FILE_PATH.startswith("http://") or MARKDOWN_FILE_PATH.startswith(
        "https://"
    ):
        FORM_TITLE = (
            MARKDOWN_FILE_PATH.split("/")[-1]
            .replace(".md", "")
            .replace("_", " ")
            .title()
        )
    else:
        FORM_TITLE = (
            MARKDOWN_FILE_PATH.split("/")[-1]
            .replace(".md", "")
            .replace("_", " ")
            .title()
        )

    print("Parsing Markdown questions...")
    parsed_questions = parse_markdown_questions(MARKDOWN_FILE_PATH)

    if not parsed_questions:
        print("No questions parsed. Exiting.")
    else:
        print(f"Successfully parsed {len(parsed_questions)} questions.")
        print("Authenticating with Google...")
        credentials = authenticate_google_forms()

        if credentials:
            print("Authentication successful.")
            create_google_form(credentials, FORM_TITLE, parsed_questions)
        else:
            print("Authentication failed. Cannot create Google Form.")
