"""
Usage: Opens all .txt files in a directory and look
       for any lines with matches from the user input.
"""
# For further improvement/s:
# - print lines where the match is found.
import sys
import re
from pathlib import Path


print("(Enter 'q' anytime to terminate program.)")

# Ask the user input.
directory_path = input("Enter directory path: ")
if directory_path.lower() == 'q':
    print("\nProgram terminated. Goodbye.")
    sys.exit()
# Convert input to a path.
p = Path(directory_path)
# Check if path is valid and existing.
if p.is_dir():
    # Ask the user what to find.
    search = input("\nSearch for word(case-insensitive): ")
    if search.lower() == 'q':
        print("\nProgram terminated. Goodbye.")
        sys.exit()
    # Regular expression.
    find_text = re.compile(fr'{search}', re.I)
    txt_files = p.glob('*.txt')

    # Check if there's an existing file/s.
    if txt_files:
        # Initialize empty dictionary for data.
        found_matches = {}

        # Loop through each file.
        for i, txt_file in enumerate(txt_files):
            # Save the chapter number and create a list to
            # store each line where the matches are found.
            found_matches[txt_file.name] = []
            with open(txt_file, encoding='utf-8') as tf:
                for n, line in enumerate(tf):
                    found_text = find_text.search(line)
                    if found_text:
                        # Add each line with match to the list.
                        found_matches[txt_file.name].append(n + 1)
            #print(f"- {txt_file.name}")
        print()

        # Print the details in proper format.
        for text_file, lines in found_matches.items():

            if found_matches[text_file]:
                print(f"[{search}] found in [{text_file}].")
                print(f"Number of line(s): {len(lines)}")
                print('Lines:', end=' ')
                for line in lines:
                    print(line, end=' ')
                print("\n")
            else:
                print(f"[{search}] not found in [{text_file}].")
                print()
    else:
        print("No .txt files found.")
else:
    print(f"\nDirectory not found.")
