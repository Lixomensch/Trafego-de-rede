import sqlite3

def init_db():
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,
            name TEXT NOT NULL,
            traffic_rate REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_device(ip, name, traffic_rate):
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO devices (ip, name, traffic_rate) VALUES (?, ?, ?)', (ip, name, traffic_rate))
    conn.commit()
    conn.close()

def get_all_devices():
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, ip, name, traffic_rate FROM devices')
    devices = [
        {'id': row[0], 'ip': row[1], 'name': row[2], 'traffic_rate': row[3]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return devices

def delete_device_db(device_id):
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM devices WHERE id = ?', (device_id,))
    conn.commit()
    conn.close()
