from flask import Flask, request, jsonify
from flask_cors import CORS
from database import init_db, insert_device, get_all_devices, delete_device_db

app = Flask(__name__)
CORS(app)

@app.route('/devices', methods=['POST'])
def add_device():
    data = request.get_json()
    ip = data.get('ip')
    name = data.get('name')
    traffic_rate = data.get('traffic_rate')

    if not ip or not name or traffic_rate is None:
        return jsonify({'error': 'Incomplete data'}), 400

    insert_device(ip, name, traffic_rate)
    return jsonify({'message': 'Device added successfully'})

@app.route('/devices', methods=['GET'])
def list_devices():
    devices = get_all_devices()
    return jsonify(devices)

@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    delete_device_db(device_id)
    return jsonify({'message': f'Device {device_id} successfully removed'})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
