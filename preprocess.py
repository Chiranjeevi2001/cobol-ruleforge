import os

# Function to preprocess Cobol file
def preprocess_cobol_file(file_path):
    lines = []
    with open(file_path, 'r',encoding='latin-1') as file:
        for line in file:
            # Remove leading and trailing whitespaces
            line_stripped = line.rstrip()  # Preserve leading spaces
            # Skip empty lines and comment lines
            if line_stripped and not line_stripped.lstrip().startswith('*'):
                lines.append(line)
    return ''.join(lines)

# Directory containing Cobol files
directory = './Test_COBOLs/InputFiles'

# Traverse through directories and preprocess Cobol files
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(('.cbl', '.cob')):
            file_path = os.path.join(root, filename)
            preprocessed_code = preprocess_cobol_file(file_path)
            # Write preprocessed code back to the file
            with open(file_path, 'w', encoding='latin-1') as file:
                file.write(preprocessed_code)
