from io import BytesIO
import os
from typing import Any
from flask_bcrypt import check_password_hash  # type: ignore
from datetime import timedelta
from flask import Flask, jsonify, redirect, send_file, session, url_for, render_template, request  # type: ignore
from controllers.login_controller import LoginController
from controllers.store_configuration_controller import StoreConfigController
from database.sqlite_db import POSDatabase
from routes.inventory_routes import inventory_bp
from routes.sale_routes import sale_bp
from routes.reports_routes import reports_bp
from routes.setting_routes import setting_bp
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', '')

# routes
app.register_blueprint(inventory_bp)
app.register_blueprint(sale_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(setting_bp)
app.permanent_session_lifetime = timedelta(hours=1)
store_config_controller = StoreConfigController()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    try:
        login_user = request.form.to_dict()
        login_controller = LoginController()
        login_response = login_controller.check_valid(login_user)
        session['logged_in'] = True
        session['user_data'] = login_response
        response: dict[str, Any] = {
            'logged_in': session['logged_in'],
            'message': 'Logged in successfully',
            'data': login_response,
            'url': url_for('inventory.get_inventory_item')
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/log-out')
def logout():
    session['logged_in'] = False
    del session['user_data']
    return redirect(url_for('index'))


@app.route('/about_us')
def about_us():
    return render_template('about_us/about_us.html')


@app.route('/get_store_image', methods=['GET'])  # type: ignore
def get_store_image():
    try:
        response = store_config_controller.get_image()
        if response:
            image_stream = BytesIO(response)
            return send_file(image_stream, mimetype='image/jpeg')
    except Exception as e:
        return jsonify({'error': str(e)}), 404


if __name__ == "__main__":
    db = POSDatabase()
    db.setUp()
    app.run(debug=True, port=5000)
