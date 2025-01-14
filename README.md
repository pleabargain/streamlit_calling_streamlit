# Streamlit Dual-App System

#why
I'm trying to think of ways to isolate the logic of the app from the UI.

#repo
https://github.com/pleabargain/streamlit_calling_streamlit

A dual-app system built with Streamlit that demonstrates inter-app communication and data persistence. The system consists of two applications (Green App and Red App) that work together to capture, store, and display user information and images.

## Features

### Green App (Port 8501)
- User input form with fields for name and age
- Image upload capability
- Automatic data persistence to JSON
- Timestamp recording for each entry
- Navigation to Red App
- Detailed error logging

### Red App (Port 8502)
- JSON file upload interface
- Display of user information and uploaded images
- Entry navigation for multiple records
- Navigation to Green App
- Detailed error logging

## File Structure
```
.
├── streamlit_green.py    # Green App implementation
├── streamlit_red.py      # Red App implementation
├── data/                 # Data storage directory
│   └── user_data.json    # Persistent data storage
├── uploads/              # Image storage directory
└── *.log                 # Log files for debugging
```

## Installation & Setup

1. Install required dependencies:
```bash
pip install streamlit
```

2. Start the Green App:
```bash
streamlit run streamlit_green.py --logger.level=debug > green_app.log 2>&1
```

3. Start the Red App:
```bash
streamlit run streamlit_red.py --logger.level=debug > red_app.log 2>&1
```

## Usage Instructions

### Green App (Data Entry)
1. Access the Green App at `http://localhost:8501`
2. Fill in the form with:
   - Name
   - Age (0-120)
   - Upload an image (PNG, JPG, JPEG)
3. Click "Submit" to save the data
4. Use the "Go to Red App" button to view entries

### Red App (Data Display)
1. Access the Red App at `http://localhost:8502`
2. Choose between:
   - Using the default data file
   - Uploading a custom JSON file
3. Navigate between multiple entries using the dropdown
4. View user details and uploaded images
5. Use the "Go to Green App" button to add new entries

## Technical Details

### Data Storage
- User data is stored in JSON format at `data/user_data.json`
- Images are stored in the `uploads/` directory
- Each entry contains:
  - Name
  - Age
  - Image path
  - Timestamp

### Logging
- Debug-level logging enabled
- Log files:
  - `green_app_[DATE].log`
  - `red_app_[DATE].log`
- Logs capture:
  - User actions
  - Data operations
  - Errors and warnings

### Error Handling
- Comprehensive error handling for:
  - File operations
  - Data validation
  - Image uploads
  - JSON parsing
