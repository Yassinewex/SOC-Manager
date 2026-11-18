from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def dashboard():
stats = {
'total_events': 12450,
'security_alerts': 156,
'critical_alerts': 8,
'open_incidents': 12,
'monitored_machines': 25,
'resolved_incidents': 34
}
return str(stats)
if __name__ == 'main':
app.run(host='0.0.0.0', port=5000)
