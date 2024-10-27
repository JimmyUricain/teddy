from flask import Flask
from app.Blueprints.Starter.starter import starter_bp


app = Flask(__name__, static_folder='app/static')
app.register_blueprint(starter_bp)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)