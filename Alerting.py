from flask import Flask, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Mock database for active alerts
active_alerts = [
    {
        'alert_id': 1,
        'severity': 'Critical',
        'source': 'Firewall',
        'message': 'Brute force attack detected'
    },
    {
        'alert_id': 2,
        'severity': 'High',
        'source': 'EDR',
        'message': 'Malware execution blocked'
    }
]

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    logging.info('Fetching active alerts')
    return jsonify(active_alerts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
