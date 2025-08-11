import csv
import os
import random

import genanki

# --- Configuration ---
ROOT_DIR = "CFA"
OUTPUT_FILENAME = "cfa_anki_deck.apkg"

# --- Anki Model and Deck Configuration ---
# Generate random IDs for the model to avoid conflicts
MODEL_ID = random.randrange(1 << 30, 1 << 31)
DECK_ID_START = random.randrange(1 << 20, 1 << 21)

# Define the Anki card model (template)
# This defines the fields and how cards look.
my_model = genanki.Model(
    MODEL_ID,
    "CFA Basic Model (with MathJax)",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": '<div class="card front">{{Front}}</div>',
            "afmt": '{{FrontSide}}\n\n<hr id="answer">\n\n<div class="card back">{{Back}}</div>',
        },
    ],
    css="""
  .card {
    font-family: Arial;
    font-size: 20px;
    text-align: center;
    color: black;
    background-color: white;
  }

  .card.front {
    padding: 20px;
  }

  .card.back {
    text-align: left;
    padding: 20px;
  }
  """,
)


def create_anki_package():
    """
    Scans the ROOT_DIR for .tsv files and creates an Anki .apkg file.
    """
    print("Starting Anki deck creation...")
    decks = []
    deck_id_counter = DECK_ID_START

    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        for filename in filenames:
            if filename.endswith(".tsv"):
                # Construct the hierarchical deck name from the file path
                # e.g., CFA/Quant/01_TVM.tsv -> CFA::Quant::01_TVM
                deck_name = os.path.join(dirpath, filename.replace(".tsv", ""))
                deck_name = deck_name.replace(os.path.sep, "::")

                # Create a new deck for this file
                deck_id_counter += 1
                my_deck = genanki.Deck(deck_id_counter, deck_name)

                tsv_path = os.path.join(dirpath, filename)

                try:
                    # Read the tab-separated file
                    with open(tsv_path, "r", encoding="utf-8") as f:
                        reader = csv.reader(f, delimiter="\t")
                        for i, row in enumerate(reader):
                            # Skip header row if present (simple check)
                            if i == 0 and row[0].lower() == "front":
                                continue

                            # Ensure row has enough columns
                            if len(row) >= 3:
                                front = row[0]
                                back = row[1]
                                tags_string = row[2]

                                # genanki expects tags as a list of strings
                                tags = tags_string.split()

                                my_note = genanki.Note(
                                    model=my_model, fields=[front, back], tags=tags
                                )
                                my_deck.add_note(my_note)
                            else:
                                print(
                                    f"  [Warning] Skipping malformed row {i + 1} in {filename}"
                                )

                    if len(my_deck.notes) > 0:
                        decks.append(my_deck)
                        print(
                            f"  Deck '{my_deck.name}' created with {len(my_deck.notes)} notes."
                        )
                    else:
                        print(
                            f"  [Warning] No notes found in {filename}, skipping deck."
                        )

                except Exception as e:
                    print(f"[Error] Could not process file {tsv_path}: {e}")

    # Package all the decks together
    if decks:
        my_package = genanki.Package(decks)
        my_package.write_to_file(OUTPUT_FILENAME)
        print(f"\nSuccessfully created '{OUTPUT_FILENAME}' with {len(decks)} decks.")
    else:
        print(
            "\nNo decks were created. Please check your folder structure and .tsv files."
        )


if __name__ == "__main__":
    if not os.path.isdir(ROOT_DIR):
        print(f"[Error] Root directory '{ROOT_DIR}' not found.")
        print(
            "Please make sure your directory structure is correct and run this script from the parent directory."
        )
    else:
        create_anki_package()
