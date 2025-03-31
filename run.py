import os
import platform
import requests
import streamlit as st

# Streamlit UI
st.title("System Info Sender")

if st.button("Send Info to Server"):
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

    # Send the data via HTTP POST
    try:
        response = requests.post(server_url, data=data)
        st.success(f"Sent successfully! Server Response: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
