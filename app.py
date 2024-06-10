from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_modbus():
    # Get the JSON data from the POST request
    data = request.json
    print(f"Received data: {data}")

    # Extract the fields from the JSON payload
    ip = data.get('ip')
    port = data.get('port')
    unit_id = data.get('unit_id')
    address = data.get('address')
    values = data.get('values')  # The Modbus register values
    timestamp = data.get('timestamp', 'N/A')  # Optional timestamp

    # Process the data as needed
    print(f"IP: {ip}")
    print(f"Port: {port}")
    print(f"Unit ID: {unit_id}")
    print(f"Address: {address}")
    print(f"Values: {values}")
    print(f"Timestamp: {timestamp}")

    # Implement your processing logic here

    # Send a response back to the MD309
    response = {
        "status": "success",
        "message": "Data received successfully"
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')


# curl -X POST -H "Content-Type: application/json" -d '{"ip": "192.168.0.100","port": 502,"unit_id": 1,"address": 100,"values": [123, 456, 789],"timestamp": "2024-05-21T12:34:56Z"}' http://127.0.0.1:5000/modbus
