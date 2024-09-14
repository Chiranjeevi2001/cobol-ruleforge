import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import glob
import os

directory_path_CBL = "../Test_COBOLs/InputFiles"
output_directory = "../Test_COBOLs/Output_Code_Summary"

geminiApiKey = 'AIzaSyABQ7adBwnlHTLO8JgIh3w33kqihU5LjQY'

with open('codeSummarizationMessage.txt','r') as file:
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
    # print(response.prompt_feedback)
    return(response.text)


def read_cobol_file(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        return file.read()

i = 1
# Iterate through files in the directory
print("\n\nSummarizing the code...")
for filename in cbl_files:
    cobol_code = read_cobol_file(filename)
    # if cobol_code is not None:
    # Generate Markdown Output
    mark_output = get_raw_text_gemini(cobol_code, code_systemMessage)
    
    # get the output path name
    base, ext = os.path.splitext(filename)
    filename_without_extension = os.path.basename(base)
    output_filename = output_directory + "/Out_" + filename_without_extension + ".md"
    with open(output_filename,'w') as f:
    # write to the output file
        f.write(mark_output)

    print(f"Done with {i} files out of {len(cbl_files)}")
    i += 1