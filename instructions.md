create a new streamlit app that calls another streamlit app

green app 
form for capturing user input with an image upload
save data as json file
the data will be appended to the json file so users can see the history of their inputs
date stamp the input
port 8501

red app
displays the image and the user input
streamlit green calls streamlit red and vice versa
load json file
create a UI to load the json file user can navigate to load a JSON file.
port 8502




To enable verbose logging, run the Streamlit apps with the `--logger.level=debug` flag.

Create a log file to capture all errors. This can be done by redirecting the output of the Streamlit commands to a file. For example:

streamlit run streamlit_green.py --logger.level=debug > green_app.log 2>&1
streamlit run streamlit_red.py --logger.level=debug > red_app.log 2>&1


# run as powershell
Start-Process -FilePath "streamlit" -ArgumentList "run streamlit_green.py" ; Start-Process -FilePath "streamlit" -ArgumentList "run streamlit_red.py --server.port 8502"