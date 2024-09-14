import streamlit as st
import google.generativeai as genai
import json

# Set the page configuration to increase the overall width
st.set_page_config(page_title="COBOL RuleForge", layout="wide")
st.markdown("<h1 style='text-align: center;'>COBOL RuleForge</h1>", unsafe_allow_html=True)
# Set up the API key
geminiApiKey = ''
genai.configure(api_key=geminiApiKey)
model = genai.GenerativeModel('gemini-pro')

# Load the system message from the text file
with open('codeSystemMessage.txt', 'r') as file:
    code_systemMessage = file.read()

# Function to read COBOL code and extract business rules
def get_raw_text_gemini(file_content):
    try:
        response = model.generate_content(
            code_systemMessage + "\n\n" + file_content,
            generation_config=genai.types.GenerationConfig(max_output_tokens=5000)
        )
        return response.text
    except Exception as e:
        st.error(f"Error generating business rules: {e}")
        return None

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
        for rule in rules:
            with placeholder.container():
                with st.expander(f"Rule ID: {rule['id']} - {rule['description']}"):
                    st.markdown(f"**Condition:** {rule['condition']}")
                    if isinstance(rule['output'], dict):
                        st.write("**Outputs:**")
                        st.json(rule['output'])  # Display output in JSON format for clarity
                    else:
                        st.markdown(f"**Output:** {rule['output']}")
    except json.JSONDecodeError as e:
        st.error(f"Failed to parse business rules: {e}. Please check the format.")
    except KeyError as e:
        st.error(f"Missing expected key in business rules: {e}.")
    except Exception as e:
        st.error(f"An unexpected error occurred while displaying business rules: {e}.")

# Layout setup: Create two columns with equal width (1:1 ratio)
left_col, right_col = st.columns(2)  # Two equal columns

# Left column: File upload and paste options
with left_col:
    st.subheader("Upload or Paste COBOL Code")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a COBOL file", type=['cbl'])

    # Text area for pasting code
    if not uploaded_file:
        cobol_text = st.text_area("Or paste COBOL code here:", height=500)

# Right column: Display the extracted business rules
with right_col:
    st.subheader("Extracted Business Rules")
    st.markdown("<br/>", unsafe_allow_html=True)  # Add some space below the subheader
    rules_placeholder = st.markdown(
        """
        <div style="background-color: #262730; padding: 10px; border-radius: 5px; min-height: 400px;">
            <p style="color: rgb(255,255,255);">Business rules will be displayed here...</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    if uploaded_file:
        # Read the uploaded COBOL code
        try:
            cobol_code = uploaded_file.read().decode('latin-1')
            with left_col:
                st.code(cobol_code, language='cobol')       
            # st.write("Processing uploaded file...")

        # Extract business rules
            with st.spinner("Extracting..."):
                business_rules = get_raw_text_gemini(cobol_code)
                display_business_rules(business_rules, rules_placeholder)
        except Exception as e:
            st.error(f"Error reading uploaded file: {e}")

    elif cobol_text:
        # Process the pasted COBOL code
        try:
            st.write("Processing pasted code...")

        # Extract business rules
            with st.spinner("Extracting..."):
                business_rules = get_raw_text_gemini(cobol_text)
                display_business_rules(business_rules, rules_placeholder)
        except Exception as e:
            st.error(f"Error processing pasted code: {e}")
