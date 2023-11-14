import os

# Function to process the text file
def process_text_file(input_file_path):
    with open(input_file_path, 'r') as input_file:
        # Read the content of the file
        lines = input_file.readlines()

    # Remove empty lines
    non_empty_lines = [line.strip() for line in lines if line.strip()]

    # Remove lines starting with 'Pen' and the line below it
    # Remove lines starting with 'Rectangle'
    filtered_lines = []
    skip_next_line = False
    for line in non_empty_lines:
        if line.startswith('Pen'):
            skip_next_line = True
        elif line.startswith('Rectangle'):
            continue
        elif skip_next_line:
            skip_next_line = False
        else:
            filtered_lines.append(line)

    # Extract page numbers starting with 'Page #'
    original = [line.split()[1] for line in filtered_lines if line.startswith('Page')]

    return original

# Function to process image file names in a folder
def process_image_folder(folder_path):
    # Get all file names from the folder
    file_names = os.listdir(folder_path)

    # Extract xyz parts from file names
    extracted_numbers = [name.split('_')[1] for name in file_names if name.startswith('page')]

    return extracted_numbers

# Specify the paths
input_text_file_path = 'count.txt'
image_folder_path = output_dir

# Process the text file
original_numbers = process_text_file(input_text_file_path)
print(f"Length of orig - {len(original_numbers)}")
# Process the image folder
extracted_numbers = process_image_folder(image_folder_path)
print(f"Length of extracted - {len(extracted_numbers)}")

# Find numbers not matching in the two lists
mismatched_numbers = set(original_numbers) - set(extracted_numbers)

# Print or use the results as needed
print("Original Numbers:", sorted(original_numbers))
print("Extracted Numbers:", sorted(extracted_numbers))
print("Mismatched Numbers:", list(mismatched_numbers))