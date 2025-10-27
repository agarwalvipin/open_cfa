#!/usr/bin/env python3
r"""
Script to fix markdown formatting by replacing escaped characters and citation markers.

This script replaces:
- '\>' with '>'
- '\<' with '<'
- '\_' with '_'
- Removes citation markers like '[cite_start]', '[cite: 1234]', etc.

Usage: python fix_markdown.py <markdown_file>
"""

import os
import re
import sys


def fix_markdown(file_path):
    """
    Fix markdown formatting by replacing escaped characters and citation markers.

    Args:
        file_path (str): Path to the markdown file to fix
    """
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return False

    # Check if it's a file (not a directory)
    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a file.")
        return False

    try:
        # Read the file content
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Store original content for comparison
        original_content = content

        # Perform replacements for escaped characters
        content = content.replace("\\>", ">")
        content = content.replace("\\<", "<")
        content = content.replace("\\_", "_")

        # Remove citation markers
        # Pattern matches [cite_start] and [cite: 1234] including incomplete ones like [cite: 2835
        content = re.sub(r"\[cite_start\]", "", content)
        content = re.sub(r"\[cite: \d+\]", "", content)
        content = re.sub(r"\[cite: \d+", "", content)  # For incomplete citations
        content = re.sub(r"\[cite: \d+, \d+\]", "", content)  # For range citations

        # Remove citation numbers like ", 613]" or " 617]" or "-678]" etc.
        # This handles patterns like ", 613]", " , 617]", "-668, 673]", " -678]"
        content = re.sub(r",?\s*-?\d+(?:,\s*\d+)*\]", "", content)

        # Check if any changes were made
        if content == original_content:
            print(f"No changes needed in '{file_path}'.")
            return True

        # Write the modified content back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Successfully fixed markdown formatting in '{file_path}'.")
        return True

    except Exception as e:
        print(f"Error processing file '{file_path}': {e}")
        return False


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) != 2:
        print("Usage: python fix_markdown.py <markdown_file>")
        print("\nThis script fixes markdown formatting by replacing:")
        print("  '\\>' with '>'")
        print("  '\\<' with '<'")
        print("  '\\_' with '_'")
        print("And removes citation markers like:")
        print("  '[cite_start]'")
        print("  '[cite: 1234]'")
        print("  ', 613]' or ' -678]' (citation numbers)")
        sys.exit(1)

    file_path = sys.argv[1]

    # Fix the markdown file
    success = fix_markdown(file_path)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
