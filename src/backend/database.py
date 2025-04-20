"""Database module for the backend application."""

import sqlite3
import os

DB_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, "devices.db")


def init_db():
    """
    Initialize the database.

    Creates a SQLite database with a table named "devices" if it does not already exist.
    The table has the following columns:

    - id (int): Unique identifier of the device
    - ip (str): IP address of the device
    - name (str): Name of the device
    - traffic_rate (float): Traffic rate of the device
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,
            name TEXT NOT NULL,
            traffic_rate REAL NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


def insert_device(ip, name, traffic_rate):
    """
    Insert a new device into the database.

    Parameters:
    - ip (str): IP address of the device
    - name (str): Name of the device
    - traffic_rate (float): Traffic rate of the device

    Returns:
    None
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO devices (ip, name, traffic_rate) VALUES (?, ?, ?)",
        (ip, name, traffic_rate),
    )
    conn.commit()
    conn.close()


def get_all_devices():
    """
    Retrieve all devices from the database.

    Returns a list of dictionaries, where each dictionary contains the following keys:

    - id (int): Unique identifier of the device
    - ip (str): IP address of the device
    - name (str): Name of the device
    - traffic_rate (float): Traffic rate of the device
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, ip, name, traffic_rate FROM devices")
    devices = [
        {"id": row[0], "ip": row[1], "name": row[2], "traffic_rate": row[3]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return devices


def delete_device_db(device_id):
    """
    Delete a device from the database.

    Parameters:
    - device_id (int): Unique identifier of the device to be deleted.

    Returns:
    None
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM devices WHERE id = ?", (device_id,))
    conn.commit()
    conn.close()
