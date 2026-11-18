from flask import Flask, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Mock database for parsed logs
parsed_logs = [
    {
        'log_id': 101,
        'timestamp': '2026-11-18T16:50:00Z',
        'event_type': 'Authentication',
        'status': 'Failed',
        'user': 'admin'
    },
    {
        'log_id': 102,
        'timestamp': '2026-11-18T16:52:00Z',
        'event_type': 'Process Creation',
        'status': 'Suspicious',
        'process': 'powershell.exe'
    }
]

@app.route('/api/logs', methods=['GET'])
def get_logs():
    logging.info('Fetching parsed log events')
    return jsonify(parsed_logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
