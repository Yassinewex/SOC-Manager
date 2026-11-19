from flask import Flask, jsonify

app = Flask(__name__)

# Mock database for users
users = {
    1: {'username': 'admin', 'role': 'Admin'},
    2: {'username': 'analyst_l1', 'role': 'SOC L1'},
    3: {'username': 'analyst_l2', 'role': 'SOC L2'},
    4: {'username': 'soc_manager', 'role': 'SOC Manager'}
}

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
