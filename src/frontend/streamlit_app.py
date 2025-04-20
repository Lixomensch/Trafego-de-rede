"""Streamlit application for monitoring network devices."""

import streamlit as st
from ui import device_form, device_list

st.set_page_config(page_title="Network Monitoring", layout="wide")
st.title("Network Device Monitoring")


def main():
    """
    Main function to display the network device monitoring interface.

    This function sets up the Streamlit page configuration and title.
    It calls the `device_form` function to display the form for adding new devices,
    and the `device_list` function to show the list of registered devices.
    """
    device_form()
    device_list()


if __name__ == "__main__":
    main()
