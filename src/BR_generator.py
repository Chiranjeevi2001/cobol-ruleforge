import subprocess
import glob
try:
    import google.generativeai as genai
except ImportError:
    print("Library not found. Installing...")
    try:
        subprocess.check_call(["pip", "install", "google.generativeai"])
        print("Library installed successfully.")
        import google.generativeai as genai  # Now try importing again
    except Exception as e:
        print(f"Failed to install library: {e}")
from IPython.display import display
from IPython.display import Markdown
import pandas as pd

directory_path_CBL = "../Test_COBOLs/InputFiles"
output_directory = "../Test_COBOLs/BR_JSON"

geminiApiKey = 'AIzaSyABQ7adBwnlHTLO8JgIh3w33kqihU5LjQY'

with open('codeSystemMessage.txt','r') as file:
    code_systemMessage = file.read()

def get_cbl_files(directory):
    cbl_files = glob.glob(directory+ '/*.cbl', recursive=True)
    return cbl_files

cbl_files = get_cbl_files(directory_path_CBL)

genai.configure(api_key=geminiApiKey)
model = genai.GenerativeModel('gemini-pro')

def get_raw_text_gemini(file_content,systemMessage):
    response = model.generate_content(code_systemMessage+"\n\n"+file_content
                                    ,generation_config=genai.types.GenerationConfig(max_output_tokens=5000))
    # candidates=response.candidates[0].content.parts[0].text
#     print(response.prompt_feedback)
    return(response.text)


import os

def read_cobol_file(file_path):
    # Check file size
    file_size = os.path.getsize(file_path)
    with open(file_path, 'r', encoding='latin-1') as file:
        return file.read()

i = 1
# Iterate through files in the directory
print("\n\nExtracting BRs...")
for filename in cbl_files:
    cobol_code = read_cobol_file(filename)
    # if cobol_code is not None:
    # Generate Markdown Output
    mark_output = get_raw_text_gemini(cobol_code, code_systemMessage)
    
    # get the output path name
    base, ext = os.path.splitext(filename)
    filename_without_extension = os.path.basename(base)
    output_filename = output_directory + "/Out_" + filename_without_extension + ".json"
    with open(output_filename,'w') as f:
    # write to the output file
        f.write(mark_output)
    print(f"Done with {i} files out of {len(cbl_files)}")
    i += 1