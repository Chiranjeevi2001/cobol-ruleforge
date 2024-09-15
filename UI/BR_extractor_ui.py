import streamlit as st
import google.generativeai as genai
import json

st.set_page_config(page_title="COBOL RuleForge", layout="wide")
st.markdown("<h1 style='text-align: center;'>COBOL RuleForge</h1>", unsafe_allow_html=True)
def clear_cache():
    keys = list(st.session_state.keys())
    for key in keys:
        st.session_state.pop(key)

st.button('Clear Cache', on_click=clear_cache)
# Set up the API key
geminiApiKey = ''
genai.configure(api_key=geminiApiKey)
model = genai.GenerativeModel('gemini-pro')

# Load the BR Extraction system message from the text file
try:
    with open('BRExtractionMessage.txt', 'r') as file:
        BR_Extraction_systemMessage = file.read()
except FileNotFoundError:
    st.error("The system message file 'BRExtractionMessage.txt' was not found.")
    st.stop()
    
# Load the BR Summarizer system message from the text file
try:
    with open('BRSummarizerMessage.txt', 'r') as file:
        BR_Summarizer_systemMessage = file.read()
except FileNotFoundError:
    st.error("The system message file 'BRSummarizerMessage.txt' was not found.")
    st.stop()

# Function to read COBOL code and extract business rules
def get_BRs_text_gemini(file_content):
    try:
        response = model.generate_content(
            BR_Extraction_systemMessage + "\n\n" + file_content,
            generation_config=genai.types.GenerationConfig(max_output_tokens=5000)
        )
        return response.text
    except Exception as e:
        st.error(f"Error during business rule extraction: {e}")
        return None
# Function to summarize the generated business rules

def get_BR_summary_gemini(business_rules):
    try:
        response = model.generate_content(
            BR_Summarizer_systemMessage + "\n\n" + business_rules,
            generation_config=genai.types.GenerationConfig(max_output_tokens=5000)
        )
        return response.text
    except Exception as e:
        st.error(f"Error during business rule summarization: {e}")
        return None

# Preprocess the COBOL code before passing it to the model
def preprocess_cobol_code(cobol_code):
    lines = []
    for line in cobol_code.splitlines():
        # Remove leading and trailing whitespaces
        line_stripped = line.rstrip()  # Preserve leading spaces
        # Skip empty lines and comment lines
        if line_stripped and not line_stripped.lstrip().startswith('*'):
            lines.append(line)
    return '\n'.join(lines)

# Function to parse and display the business rules
def display_business_rules(business_rules, placeholder):
    if business_rules is None:
        placeholder.warning("No business rules to display.")
        return

    try:
        # Attempt to parse the business rules JSON
        rules = json.loads(f'[{business_rules}]')  # Ensuring it is valid JSON format

        # Replace placeholder with actual business rules display
        placeholder.empty()  # Clear the placeholder box
        with placeholder.container():
            for rule in rules:
                st.json(rule)
    except json.JSONDecodeError as e:
        placeholder.error(f"Error parsing the extracted business rules: {e}")
        placeholder.warning("Please check the extracted business rules manually.")
        
# Function to create a download button for the business rules in JSON format
def download_business_rules(business_rules, key):
    try:
        # Ensure the business rules are valid JSON
        rules = json.loads(f'[{business_rules}]')
        json_data = json.dumps(rules, indent=4)
        
        # Create a download button for the JSON file
        st.download_button(
            label="Download Business Rules (JSON)",
            data=json_data,
            key = key,
            file_name="business_rules.json",
            mime="application/json"
        )
    except json.JSONDecodeError as e:
        st.error(f"Error preparing business rules for download: {e}")

# Function to create a download button for the business rules summary in Markdown format
def download_summary(summary, key):
    st.download_button(
        label="Download Summary (Markdown)",
        data=summary,
        key=key,
        file_name="business_rules_summary.md",
        mime="text/markdown"
    )

# Layout setup: Create two columns with equal width (1:1 ratio)
left_col, mid_col, right_col = st.columns(3)

# Left column: File upload and paste options
with left_col:
    st.subheader("Upload or Paste COBOL Code")

    # File uploader
    uploaded_file = st.file_uploader("Upload a COBOL file", type=['cbl', 'cob'])

    # Conditionally display the text area only if no file is uploaded
    if not uploaded_file:
        cobol_text = st.text_area("Or paste COBOL code here:")

# Right column: Display the extracted business rules
with mid_col:
    st.subheader("Extracted Business Rules")

    # Create a placeholder for business rules with a greyish background
    rules_placeholder = st.markdown(
        """
        <div style="background-color: #262730; padding: 10px; border-radius: 5px;">
            <p style="color: rgb(255,255,255);">Business rules will be displayed here...</p>
        </div>
        <br/>
        """, 
        unsafe_allow_html=True
    )
    regenerate = st.button("Regenerate")

    # Checking for user inputs and processing accordingly
    if uploaded_file:
        # Read the uploaded COBOL code
        try:
            cobol_code = uploaded_file.read().decode('latin-1')
            with left_col:
                st.code(cobol_code, language='cobol') 
            # st.write("Processing uploaded file...")

            # Preprocess the COBOL code before passing it to the model
            preprocessed_code = preprocess_cobol_code(cobol_code)

            # Extract business rules
            if "business_rules" not in st.session_state:
                with st.spinner("Extracting..."):
                    st.session_state.business_rules = get_BRs_text_gemini(preprocessed_code)
    
            business_rules = st.session_state.business_rules
            display_business_rules(business_rules, rules_placeholder)
        except Exception as e:
            st.error(f"Error reading the uploaded file: {e}")

    elif 'cobol_text' in locals() and cobol_text:
        # Process the pasted COBOL code if no file is uploaded
        try:
            st.write("Processing pasted code...")

            # Preprocess the COBOL code before passing it to the model
            preprocessed_code = preprocess_cobol_code(cobol_text)

            if "business_rules" not in st.session_state:
                with st.spinner("Extracting..."):
                    st.session_state.business_rules = get_BRs_text_gemini(preprocessed_code)
    
            business_rules = st.session_state.business_rules
            display_business_rules(business_rules, rules_placeholder)
        except Exception as e:
            st.error(f"Error reading the uploaded file: {e}")
    
    if regenerate and preprocessed_code:
        # st.write("Regenerating business rules...")
        with st.spinner("Re-extracting..."):
            st.session_state.business_rules = get_BRs_text_gemini(preprocessed_code)
        business_rules = st.session_state.business_rules
        display_business_rules(business_rules, rules_placeholder)
    
    if "business_rules" in st.session_state:
        download_business_rules(st.session_state.business_rules, 'business_rules_json')

            

with right_col:
    st.subheader("Business Rule Summarizer")
    st.markdown('<br/>', unsafe_allow_html=True)
    
    rules_placeholder = st.markdown(
        """
        <div style="background-color: #262730; padding: 10px; border-radius: 5px;">
            <p style="color: rgb(255,255,255);">Business rules summary will be displayed here...</p>
        </div>
        <br/>
        """, 
        unsafe_allow_html=True
    )
    regenerate_summary = st.button("Regenerate Summary")
    if "business_rules" in st.session_state:
        if "summary" not in st.session_state:
            with st.spinner("Summarizing..."):
                st.session_state.summary = get_BR_summary_gemini(business_rules)
        
        summary = st.session_state.summary
        if summary:
            rules_placeholder.empty()
            with rules_placeholder.container():
                st.markdown(summary, unsafe_allow_html=True)
        else:
            st.error("Error summarizing the business rules.")
            
    if regenerate_summary and business_rules:
        with st.spinner("Re-Summarizing..."):
            st.session_state.summary = get_BR_summary_gemini(business_rules)
        
        summary = st.session_state.summary
        if summary:
            rules_placeholder.empty()
            with rules_placeholder.container():
                st.markdown(summary, unsafe_allow_html=True)
        else:
            st.error("Error summarizing the business rules.")
            
    if "summary" in st.session_state:
        download_summary(st.session_state.summary, 'business_rules_summary_md')
        