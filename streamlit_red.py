import streamlit as st
import logging
import webbrowser
import json
import os
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    filename=f'red_app_{datetime.now().strftime("%Y%m%d")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Streamlit app
st.title("Red App")

# Add file uploader for JSON selection
uploaded_file = st.file_uploader("Choose a JSON file", type=['json'])
default_json_path = "data/user_data.json"

try:
    # If a file is uploaded, use that, otherwise use default path
    if uploaded_file is not None:
        data = json.load(uploaded_file)
        logger.info(f"Loaded data from uploaded file")
    elif os.path.exists(default_json_path):
        with open(default_json_path, "r") as f:
            data = json.load(f)
            logger.info(f"Loaded data from default path: {default_json_path}")
    else:
        st.info("No user data available yet")
        logger.info("No user data file found")
        data = None
    
    if data:
        # Convert single entry to list if needed
        if not isinstance(data, list):
            data = [data]
        
        # Add entry selector
        if len(data) > 1:
            selected_index = st.selectbox("Select Entry", 
                                        range(len(data)), 
                                        format_func=lambda x: f"Entry {x+1} - {data[x]['timestamp']}")
            entry = data[selected_index]
        else:
            entry = data[0]
        
        # Display user information
        st.subheader("User Information")
        st.write(f"Name: {entry['name']}")
        st.write(f"Age: {entry['age']}")
        st.write(f"Timestamp: {entry['timestamp']}")
        
        # Display image
        if os.path.exists(entry['image_path']):
            st.image(entry['image_path'], caption="Uploaded Image")
        else:
            st.error("Image file not found")
            logger.error(f"Image not found at path: {entry['image_path']}")

except Exception as e:
    st.error("Error loading data")
    logger.error(f"Error loading data: {str(e)}")

if st.button("Go to Green App"):
    logger.info("User clicked to navigate to Green App")
    webbrowser.open("http://localhost:8501")  # Green app runs on port 8501

# Set different port for this app
if __name__ == '__main__':
    import sys
    sys.argv = ["streamlit", "run", __file__, "--server.port=8502"]
