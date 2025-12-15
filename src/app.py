# '/api/v1/detailts'
# '/api/v1/healthz'

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/details', methods=['GET'])
def get_details():
    details = {
        "name": "Example API",
        "version": "1.0.0",
        "description": "This is an example API endpoint providing details."
    }
    return jsonify(details), 200

@app.route('/api/v1/healthz', methods=['GET'])
def health_check():
    health_status = {
        "status": "healthy",
    }
    return jsonify(health_status), 200

@app.route('/api/v1/hostname', methods=['GET'])
def get_hostname():
    import socket
    hostname = socket.gethostname()
    return jsonify({"hostname": hostname}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
