from flask import Flask
from models import db
from Alerting import alerting_bp
from dashboard import dashboard_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://soc_user:soc_password@db:5432/soc_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# تسجيل الوحدات
app.register_blueprint(alerting_bp)
app.register_blueprint(dashboard_bp)

@app.route('/')
def home():
    return "Bienvenue sur l'API SOC-Manager. Allez sur /dashboard pour voir l'interface."

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # إنشاء الجداول تلقائياً
    app.run(host='0.0.0.0', port=5000, debug=True)
