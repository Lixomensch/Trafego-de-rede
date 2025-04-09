"""Main module for the backend application."""

from database import delete_device_db, get_all_devices, init_db, insert_device
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/devices", methods=["POST"])
def add_device():
    """
    Add a new device to the database.

    Request JSON data should contain the following fields:

    - ip (str): IP address of the device
    - name (str): Name of the device
    - traffic_rate (float): Traffic rate of the device

    Returns a JSON response with a message indicating the success of the operation.

    If the request data is incomplete, returns a 400 error with an error message.
    """
    data = request.get_json()
    ip = data.get("ip")
    name = data.get("name")
    traffic_rate = data.get("traffic_rate")

    if not ip or not name or traffic_rate is None:
        return jsonify({"error": "Incomplete data"}), 400

    insert_device(ip, name, traffic_rate)
    return jsonify({"message": "Device added successfully"})


@app.route("/devices", methods=["GET"])
def list_devices():
    """
    List all devices in the database.

    Returns a JSON response containing a list of all devices in the database.
    Each device is represented as a JSON object with the following fields:

    - id (int): Unique identifier of the device
    - ip (str): IP address of the device
    - name (str): Name of the device
    - traffic_rate (float): Traffic rate of the device
    """
    devices = get_all_devices()
    return jsonify(devices)


@app.route("/devices/<int:device_id>", methods=["DELETE"])
def delete_device(device_id):
    """
    Delete a device from the database.

    Parameters:
    - device_id (int): Unique identifier of the device to be deleted.

    Returns a JSON response with a message indicating the success of the operation.
    """
    delete_device_db(device_id)
    return jsonify({"message": f"Device {device_id} successfully removed"})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
