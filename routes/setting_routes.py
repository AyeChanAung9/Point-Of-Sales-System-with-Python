from io import BytesIO
import json
from flask import Blueprint, jsonify, render_template, request, send_file, session  # type: ignore
from controllers.store_configuration_controller import StoreConfigController
from controllers.user_controller import UserController
from controllers.user_role_controller import UserRoleController
from controllers.user_role_permission_controller import UserRolePermissionController
from other.decorators import login_required

setting_bp = Blueprint('setting', __name__)
# Create an instance of the User and UserList Controller
user_controller = UserController()
role_controller = UserRoleController()
user_role_permission_controller = UserRolePermissionController()
store_config_controller = StoreConfigController()

#   Redirecting


@setting_bp.route('/setting/user_management')
@login_required
def get_user_management():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'users'):
            return render_template('403.html')
        response = role_controller.get_all()
        return render_template('setting/user_management.html', roles=response)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@setting_bp.route('/setting/role_management')
@login_required
def get_role_management():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'user_roles'):
            return render_template('403.html')
        return render_template('setting/role_management.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@setting_bp.route('/setting/user_permission/<role_id>/<role_name>')
@login_required
def get_user_permission(role_id: int, role_name: str):
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'user_permissions'):
            return render_template('403.html')
        return render_template('setting/user_permission.html', role_id=role_id, role_name=role_name)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ---------- Start Role ----------
# role List & Search role function
@setting_bp.route('/setting/get-roles', methods=['GET'])
@login_required
def get_roles():
    try:
        params = request.args.to_dict()
        response = role_controller.view(params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Add Edit Role function
@setting_bp.route('/setting/add-edit-role', methods=['POST'])
@login_required
def add_edit_roles():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'user_roles'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        role_data = json.loads(request.data)
        response = role_controller.add_or_modify(role_data)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Delete Role function
@setting_bp.route('/setting/delete-role/<int:role_id>',
                  methods=['DELETE'])
@login_required
def delete_role(role_id: int):
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'user_roles'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        response = role_controller.delete(role_id)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ---------- End Role ----------


# ---------- Start User ----------
# Users List & Search User function
@setting_bp.route('/setting/get-users', methods=['GET'])
@login_required
def get_users():
    try:
        params = request.args.to_dict()
        response = user_controller.view(params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Add Edit Users function


@setting_bp.route('/setting/add-edit-user', methods=['POST'])
@login_required
def add_edit_user():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'users'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        user_data = json.loads(request.data)
        response = user_controller.add_or_modify(user_data)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Delete user function


@setting_bp.route('/setting/delete-user/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id: int):
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'users'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        response = user_controller.delete(user_id)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ---------- End Item ----------

# Store Configuration
@setting_bp.route('/setting/save_store_configuration', methods=['GET', 'POST'])
@login_required
def save_store_config():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'store_configuration'):
            return render_template('403.html')
        if request.method == 'POST':
            store_name = request.form['storename']
            contact_person = request.form['contactperson']
            phone_no = request.form['phonenumber']
            address = request.form['address']
            file = request.files['file']
            response = store_config_controller.modify(
                {'store_name': store_name, 'contact_person': contact_person, 'phone_no': phone_no, 'address': address, 'image_data': file.read()})
            return jsonify({'message': response}), 200
        return render_template('setting/store_configuration.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@setting_bp.route('/setting/get_store_image', methods=['GET'])
@login_required
def get_store_image():
    try:
        response = store_config_controller.get_image()
        if response:
            image_stream = BytesIO(response)
            return send_file(image_stream, mimetype='image/jpeg')
    except Exception as e:
        return jsonify({'error': str(e)}), 404


@setting_bp.route('/setting/get_store_configuration', methods=['GET'])
@login_required
def get_store_configuration():
    try:
        response = store_config_controller.view()
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ---------- End Store Configuration ----------


# User Permissoin
@setting_bp.route('/setting/save_user_permission', methods=['POST'])
@login_required
def save_user_permission():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'user_permissions'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        permissions = json.loads(request.data)
        response = user_role_permission_controller.modify(permissions)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@setting_bp.route('/setting/load_user_permission/<int:role_id>', methods=['GET'])
@login_required
def load_user_permission(role_id: int):
    try:
        response = user_role_permission_controller.get_by_role_id(role_id)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
# ---------- End User Permissoin ----------
