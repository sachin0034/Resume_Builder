# resume.py
import streamlit as st
import model
import yaml  # Import YAML module instead of JSON
import os

def main():
    st.title("AI Based Resume Builder")
    st.write("Create a beautiful resume with ready-made templates. Use the AI assistant to generate your content. "
             "Be prepared in minutes for your next job.")

    # Add sidebar for API key input
    with st.sidebar:
        st.header("Settings")
        api_key = st.text_input("Enter OpenAI API Key", type="password")
        if st.button("Save API Key"):
            if api_key:
                os.environ['OPENAI_API_KEY'] = api_key
                st.success("API Key saved successfully!")
            else:
                st.error("Please enter an API Key")

    # Text input field
    user_input = st.text_input("Enter Details for Building Resume:")

    # Display the input text
    st.write("USE THIS PROMPT TEMPLATE TO GET BEST OUTPUT:")
    st.code("write a resume in YAML format by taking profile details and returning a full resume with all essential points and return as YAML file, Strictly follow the format and make up information wherever missing according to my profile. I need all the sections to be included. Don't drop anything. Be short and crisp in writing. don't include prompt in output nor info, give results")

    if user_input:
        response = model.generate(user_input)
        st.write(response)

        # Download button for YAML output
        download_yaml(response)


def download_yaml(data):
    if st.button("Download YAML"):
        # Set up the file name
        filename = "resume.yaml"

        # Convert dictionary to YAML string
        yaml_data = yaml.dump(data, default_flow_style=False)  # Convert to YAML format

        # Download the YAML file
        st.download_button(
            label="Click to download",
            data=yaml_data,
            file_name=filename,
            mime="application/yaml")  # Set MIME type as YAML


if __name__ == "__main__":
    main()
