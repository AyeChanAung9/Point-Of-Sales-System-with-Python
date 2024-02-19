from flask import Blueprint, jsonify, render_template, request, session
from controllers.sale_controller import SaleController
from controllers.user_role_permission_controller import UserRolePermissionController
from other.decorators import login_required


sale_bp = Blueprint('sale', __name__)
sale_controller = SaleController()
user_role_permission_controller = UserRolePermissionController()


@sale_bp.route('/sale')
@login_required
def sale():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'sales_read'):
            return render_template('403.html')
        return render_template('sale/sale.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@sale_bp.route('/sale/sale-voucher')
@login_required
def get_sale_voucher():
    try:
        return render_template('sale/sale_voucher.html', user_id_session=session['user_data'][0])
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@sale_bp.route('/sale/get-sale', methods=['GET'])
@login_required
def get_sale():
    try:
        params = request.args.to_dict()
        response = sale_controller.view(params)
        return jsonify({"data": response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@sale_bp.route('/sale/get-sale-details/<int:sale_id>')
@login_required
def get_sale_detail(sale_id: int):
    try:
        response = sale_controller.view_details(sale_id)
        return jsonify({"data": response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@sale_bp.route('/sale/sale-voucher/<voucher_no>')
@login_required
def get_sale_voucher_data(voucher_no: str):
    params = {
        'from_tran_date': '',
        'to_tran_date': '',
        'search_keyword': voucher_no,
        'page_no': 1,
    }
    sale_response = sale_controller.view(params)
    if sale_response:
        if sale_response is not None and len(sale_response) > 0:
            sale_id = sale_response[0].get('sale_id')
            sale_detail_response = sale_controller.view_details(sale_id)
            payment = sale_response[0].get('payment')
            crdp, cshp, dgtp = "", "", ""
            payment_type = {}
            if payment == "crdp":
                crdp = "Selected"
            elif payment == "cshp":
                cshp = "Selected"
            elif payment == "dgtp":
                dgtp = "Selected"
            payment_type = {'crdp': crdp, 'cshp': cshp, 'dgtp': dgtp}
            return render_template('sale/sale_voucher.html',
                                   sale=sale_response,
                                   details=sale_detail_response,
                                   payment_type=payment_type,
                                   user_id_session=session['user_data'][0],
                                   editing=True)
    return render_template('500.html')


@sale_bp.route('/sale/delete-sale/<int:sale_id>',
               methods=['DELETE'])
@login_required
def delete_sale(sale_id: int):
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'sales_delete'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        response = sale_controller.delete(sale_id)
        return jsonify({"message": response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@sale_bp.route('/sale/save_sale_voucher', methods=['POST'])
@login_required
def save_sale_voucher():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'sales_write'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        sale = request.get_json()
        response = sale_controller.add(sale)
        return jsonify({"message": response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@sale_bp.route('/sale/update-sale-voucher', methods=['POST'])
@login_required
def update_sale_voucher():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'sales_write'):
            return jsonify({'error': 'You don\'t have permission to use this feature.'}), 403
        sale = request.get_json()
        response = sale_controller.modify(sale)
        return jsonify({"message": response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
