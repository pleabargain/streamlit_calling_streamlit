import streamlit as st
import logging
import webbrowser
import json
import os
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    filename=f'green_app_{datetime.now().strftime("%Y%m%d")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create data directory if it doesn't exist
Path("data").mkdir(exist_ok=True)
Path("uploads").mkdir(exist_ok=True)

# Streamlit app
st.title("Green App")

# Create form
with st.form("user_input_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    uploaded_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
    submit_button = st.form_submit_button("Submit")

if submit_button:
    try:
        if uploaded_file is not None:
            # Save the uploaded image
            image_path = f"uploads/{uploaded_file.name}"
            with open(image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Create data dictionary
            data = {
                "name": name,
                "age": age,
                "image_path": image_path,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Load existing data or create new list
            json_path = "data/user_data.json"
            try:
                with open(json_path, "r") as f:
                    existing_data = json.load(f)
                    if not isinstance(existing_data, list):
                        existing_data = [existing_data]
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []
            
            # Append new data
            existing_data.append(data)
            
            # Save updated data
            with open(json_path, "w") as f:
                json.dump(existing_data, f, indent=4)
            
            logger.info(f"Saved user data: {data}")
            st.success("Data saved successfully!")
        else:
            st.error("Please upload an image")
            logger.warning("Form submitted without image")
    except Exception as e:
        logger.error(f"Error saving data: {str(e)}")
        st.error("An error occurred while saving the data")

if st.button("Go to Red App"):
    logger.info("User clicked to navigate to Red App")
    webbrowser.open("http://localhost:8502")

# Set different port for this app
if __name__ == '__main__':
    import sys
    sys.argv = ["streamlit", "run", __file__, "--server.port=8501"]
