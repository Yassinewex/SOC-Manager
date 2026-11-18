print("SOC-Manager starting")
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "SOCManager Platform Online"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
