from flask import Flask, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Mock database for threat intelligence feeds
threat_feeds = [
    {
        'threat_id': 'TI-901',
        'indicator': '185.220.101.5',
        'type': 'Malicious IP',
        'region': 'Eastern Europe',
        'confidence': 95
    },
    {
        'threat_id': 'TI-902',
        'indicator': 'apt29_campaign_hashes',
        'type': 'Malicious Hash',
        'region': 'Global',
        'confidence': 88
    }
]

@app.route('/api/threat-intel', methods=['GET'])
def get_threat_intel():
    logging.info('Fetching threat intelligence feeds')
    return jsonify(threat_feeds)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
