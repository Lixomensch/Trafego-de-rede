"""UI module for displaying and managing network devices with Streamlit."""

import requests
import streamlit as st
from api import delete_device, get_devices, register_device


def device_form():
    """
    Display a form to add a new device to the system.

    Fields:
        - IP Address: Text input
        - Device Name: Text input
        - Traffic Rate: Number input (Mbps)

    Behavior:
        - On submission, attempts to register the device via the API.
        - Shows success or error messages accordingly.
    """
    st.header("Add New Device")
    with st.form("form_device"):
        ip = st.text_input("IP Address")
        name = st.text_input("Device Name")
        traffic = st.number_input("Traffic Rate (Mbps)", min_value=0.0, format="%.2f")
        submitted = st.form_submit_button("Register")

        if submitted:
            if ip and name:
                try:
                    response = register_device(ip, name, traffic)
                    if response.status_code == 200:
                        st.success("Device successfully registered!")
                    else:
                        error = response.json().get("error", "Unknown error")
                        st.error(f"Error registering device: {error}")
                except requests.RequestException as err:
                    st.error(f"Request failed: {err}")
            else:
                st.warning("Please fill in all fields.")


def device_list():
    """
    Display a list of registered devices.

    Devices are shown with IP, name, traffic rate, status (green/normal or red/high),
    and a remove button. Removes a device via the API and refreshes the UI.
    """
    st.header("Registered Devices")
    try:
        devices = get_devices()

        for device in devices:
            col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])
            col1.write(f"**IP:** {device['ip']}")
            col2.write(f"**Name:** {device['name']}")
            col3.write(f"**Traffic:** {device['traffic_rate']} Mbps")

            if device["traffic_rate"] > 50:
                col4.write("**Status:** :red[High]")
            else:
                col4.write("**Status:** :green[Normal]")

            if col5.button("Remove", key=device["id"]):
                try:
                    del_res = delete_device(device["id"])
                    if del_res.status_code == 200:
                        st.success(f"Device {device['id']} removed.")
                        st.experimental_rerun()
                except requests.RequestException as err:
                    st.error(f"Failed to remove device: {err}")
    except requests.RequestException as err:
        st.error(f"Error loading devices: {err}")
