import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import glob
import os

directory_path_BR_JSON = "../Test_COBOLs/BR_JSON"
output_directory = "../Test_COBOLs/Output_BR_Summary"

geminiApiKey = 'AIzaSyABQ7adBwnlHTLO8JgIh3w33kqihU5LjQY'

with open('BRSummarizerMessage.txt','r') as file:
    code_systemMessage = file.read()

def get_json_files(directory):
    json_files = glob.glob(directory+ '/*.json', recursive=True)
    return json_files

json_files = get_json_files(directory_path_BR_JSON)

genai.configure(api_key=geminiApiKey)
model = genai.GenerativeModel('gemini-pro')

def get_raw_text_gemini(file_content,systemMessage):
    response = model.generate_content(code_systemMessage+"\n\n"+file_content
                                    ,generation_config=genai.types.GenerationConfig(max_output_tokens=5000))
    # candidates=response.candidates[0].content.parts[0].text
    # print(response.prompt_feedback)
    return(response.text)


def read_json_file(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        return file.read()

i = 1
# Iterate through files in the directory
print("\n\nSummarizing the BRs...")
for filename in json_files:
    cobol_code = read_json_file(filename)
    # if cobol_code is not None:
    # Generate Markdown Output
    mark_output = get_raw_text_gemini(cobol_code, code_systemMessage)
    
    # get the output path name
    base, ext = os.path.splitext(filename)
    filename_without_extension = os.path.basename(base)
    output_filename = output_directory + "/" + filename_without_extension + ".md"
    with open(output_filename,'w') as f:
    # write to the output file
        f.write(mark_output)

    
    print(f"Done with {i} files out of {len(json_files)}")
    i += 1