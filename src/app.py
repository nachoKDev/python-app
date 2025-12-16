from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details', methods=['GET'])
def details():
    return jsonify({
        'time' : datetime.datetime.now().strftime("%U:%M:%S%p on %A, %B %d, %Y"),
        'hostname': socket.gethostname()
    })

@app.route('/api/v1/healthz', methods=['GET'])
def health_check():
    health_status = {
        "status": "Up and Running!!",
    }
    return jsonify(health_status), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

