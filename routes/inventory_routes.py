import json
from flask import Blueprint, jsonify, render_template, request, session
from controllers.damage_loss_controller import DamageLossController
from controllers.item_controller import ItemController
from controllers.category_controller import CategoryController
from controllers.item_receive_controller import ItemReceiveController
from controllers.user_role_permission_controller import UserRolePermissionController
from other.decorators import login_required

inventory_bp = Blueprint('inventory', __name__)
item_controller = ItemController()
category_controller = CategoryController()
item_receive_controller = ItemReceiveController()
damage_loss_controller = DamageLossController()
user_role_permission_controller = UserRolePermissionController()


#   Redirecting
@inventory_bp.route('/inventory/item')
@login_required
def get_inventory_item():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'item_read'):
            return render_template('403.html')
        response = category_controller.get_all()
        return render_template('inventory/item.html', categories=response)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@inventory_bp.route('/inventory/category')
@login_required
def get_inventory_category():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'category_read'):
            return render_template('403.html')
        return render_template('inventory/category.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@inventory_bp.route('/inventory/item-receive')
@login_required
def get_inventory_item_receive():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'item_receive_read'):
            return render_template('403.html')
        return render_template('inventory/item_receive.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@inventory_bp.route('/inventory/item-receive-voucher')
@login_required
def get_inventory_item_receive_voucher():
    try:
        return render_template('inventory/item_receive_voucher.html', user_id_session=session['user_data'][0])
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@inventory_bp.route('/inventory/damage-loss')
@login_required
def get_inventory_damage_loss():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'damage_loss_read'):
            return render_template('403.html')
        return render_template('inventory/damage_loss.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@inventory_bp.route('/inventory/damage-loss-voucher')
@login_required
def get_inventory_damage_loss_voucher():
    try:
        return render_template('inventory/damage_loss_voucher.html', user_id_session=session['user_data'][0])
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ---------- Start Item ----------
# Item List & Search Item function


@inventory_bp.route('/inventory/get-items', methods=['GET'])
@login_required
def get_items():
    try:
        params = request.args.to_dict()
        response = item_controller.view(params)
        return jsonify({"data": response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Add Edit items function
@inventory_bp.route('/inventory/add-edit-item', methods=['POST'])
@login_required
def add_edit_item():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'item_write'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        item_data = json.loads(request.data)
        response = item_controller.add_or_modify(item_data)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Delete Item function


@inventory_bp.route('/inventory/delete-item/<int:item_id>', methods=['DELETE'])
@login_required
def delete_item(item_id: int):
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'item_delete'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        response = item_controller.delete(item_id)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ---------- End Item ----------


# ---------- Start Category ----------
# category List & Search category function
@inventory_bp.route('/inventory/get-categories', methods=['GET'])
@login_required
def get_categories():
    try:
        params = request.args.to_dict()
        categories = category_controller.view(params)
        return jsonify({'data': categories}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Add Edit category function
@inventory_bp.route('/inventory/add-edit-category', methods=['POST'])
@login_required
def add_edit_category():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'category_write'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        category_data = json.loads(request.data)
        response = category_controller.add_or_modify(category_data)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Delete Category function
@inventory_bp.route('/inventory/delete-category/<int:category_id>',
                    methods=['DELETE'])
@login_required
def delete_category(category_id: int):
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'category_delete'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        response = category_controller.delete(category_id)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ---------- End Category ----------


# ---------- Item Receive ----------
@inventory_bp.route('/inventory/get-receive-items', methods=['GET'])
@login_required
def get_receive_items():
    try:
        params = request.args.to_dict()
        response = item_receive_controller.view(params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Get Item Receive Details
@inventory_bp.route('/inventory/get-receive-item-details/<int:item_receive_id>')
@login_required
def get_receive_item_detail(item_receive_id: int):
    try:
        response = item_receive_controller.view_details(item_receive_id)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Item Receive Voucher With Data
@inventory_bp.route('/inventory/item-receive-voucher/<voucher_no>')
@login_required
def get_inventory_item_receive_voucher_data(voucher_no: str):
    try:
        params = {'search_keyword': voucher_no}
        item_receive_response = item_receive_controller.view(params)
        if len(item_receive_response) > 0:
            item_receive_id = item_receive_response[0].get('item_receive_id')
            response_detail = item_receive_controller.view_details(
                item_receive_id)
            return render_template('inventory/item_receive_voucher.html',
                                   item_receive=item_receive_response,
                                   details=response_detail,
                                   user_id_session=session['user_data'][0],
                                   editing=True)
        return render_template('500.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Delete Item Receive function


@inventory_bp.route('/inventory/delete-receive-item/<int:item_receive_id>',
                    methods=['DELETE'])
@login_required
def delete_receive_item(item_receive_id: int):
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'item_receive_delete'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        response = item_receive_controller.delete(item_receive_id)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@inventory_bp.route('/inventory/save_item_receive_voucher', methods=['POST'])
@login_required
def save_item_receive_voucher():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'item_receive_write'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        item_receive = request.get_json()
        response = item_receive_controller.add(item_receive)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@inventory_bp.route('/inventory/update-item-receive-voucher', methods=['POST'])
@login_required
def update_item_receive_voucher():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'item_receive_write'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        item_receive = request.get_json()
        response = item_receive_controller.modify(item_receive)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@inventory_bp.route('/inventory/get_item_by_product_code', methods=['GET'])
@login_required
def get_item_by_product_code():
    try:
        product_code = request.args.get('product_code', '')
        response = item_controller.get_by_product_code(product_code)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ---------- End Item Receive ----------


# ---------- Damage Loss ----------
@inventory_bp.route('/inventory/get-damage-loss', methods=['GET'])
@login_required
def get_damage_loss():
    try:
        params = request.args.to_dict()
        response = damage_loss_controller.view(params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Damage Loss Detail
@inventory_bp.route('/inventory/get-damage-loss-details/<int:damage_loss_id>')
@login_required
def get_damage_loss_detail(damage_loss_id: int):
    try:
        response = damage_loss_controller.view_details(damage_loss_id)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Damage Loss Voucher with data
@inventory_bp.route('/inventory/damage-loss-voucher/<voucher_no>')
@login_required
def get_damage_loss_voucher_data(voucher_no: str):
    try:
        params = {'search_keyword': voucher_no}
        damage_loss_response = damage_loss_controller.view(params)
        if len(damage_loss_response) > 0:
            damage_loss_id = damage_loss_response[0].get('damage_loss_id')
            response_detail = damage_loss_controller.view_details(
                damage_loss_id)
            return render_template('inventory/damage_loss_voucher.html',
                                   damage_loss=damage_loss_response,
                                   details=response_detail,
                                   user_id_session=session['user_data'][0],
                                   editing=True)
        return render_template('500.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Delete Damage Loss


@inventory_bp.route('/inventory/delete-damage-loss/<int:damage_loss_id>',
                    methods=['DELETE'])
@login_required
def delete_damage_loss(damage_loss_id: int):
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'damage_loss_delete'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        response = damage_loss_controller.delete(damage_loss_id)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@inventory_bp.route('/inventory/save_damage_loss_voucher', methods=['POST'])
@login_required
def save_damage_loss_voucher():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'damage_loss_write'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        damage_loss = request.get_json()
        response = damage_loss_controller.add(damage_loss)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@inventory_bp.route('/inventory/update-damage-loss-voucher', methods=['POST'])
@login_required
def update_damage_loss_voucher():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'damage_loss_write'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        damage_loss = request.get_json()
        response = damage_loss_controller.modify(damage_loss)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ---------- End Damage Loss ----------
