"""API interaction module for the frontend application."""

import os

import requests

API_URL = os.getenv("API_URL", "http://localhost:5000/devices")
TIMEOUT = 5


def get_devices():
    """
    Retrieve the list of all registered devices from the API.

    Returns:
        list[dict]: A list of device dictionaries, each containing:
            - id (int): Device ID
            - ip (str): IP address
            - name (str): Device name
            - traffic_rate (float): Traffic rate in Mbps
    """
    response = requests.get(API_URL, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def register_device(ip, name, traffic_rate):
    """
    Register a new device via the API.

    Args:
        ip (str): IP address of the device.
        name (str): Name of the device.
        traffic_rate (float): Traffic rate in Mbps.

    Returns:
        requests.Response: The response from the API.
    """
    payload = {"ip": ip, "name": name, "traffic_rate": traffic_rate}
    return requests.post(API_URL, json=payload, timeout=TIMEOUT)


def delete_device(device_id):
    """
    Delete a device using its ID.

    Args:
        device_id (int): Unique identifier of the device.

    Returns:
        requests.Response: The response from the API.
    """
    delete_url = f"{API_URL}/{device_id}"
    return requests.delete(delete_url, timeout=TIMEOUT)
