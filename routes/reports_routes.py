from flask import Blueprint, jsonify, render_template, request, session
import json
from controllers.dashboard_controller import DashboardController
from controllers.inventory_report_controller import InventoryReportController
from controllers.sale_report_controller import SaleReportController
from controllers.user_role_permission_controller import UserRolePermissionController
from other.decorators import login_required

reports_bp = Blueprint('report', __name__)
sale_report_controller = SaleReportController()
inventory_report_controller = InventoryReportController()
dashboard_controller = DashboardController()
user_role_permission_controller = UserRolePermissionController()


@reports_bp.route('/report/sale')
@login_required
def get_sale_report():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'reports'):
            return render_template('403.html')
        response = sale_report_controller.get_year()
        return render_template('report/sale_report.html', years=response)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/inventory')
@login_required
def get_inventory_report():
    try:
        if not user_role_permission_controller.has_permission(session['user_data'][-1], 'reports'):
            return render_template('403.html')
        return render_template('report/inventory_report.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/dashboard')
@login_required
def get_dashboard_report():
    try:
        return render_template('report/dashboard.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/get-top-selling', methods=['POST'])
@login_required
def get_top_selling():
    try:
        request_data = json.loads(request.data)
        from_date = request_data.get('fromDate')
        to_date = request_data.get('toDate')
        params = {
            'from_date': from_date,
            'to_date': to_date,
        }
        response = sale_report_controller.get_top_selling(params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/get-items-qty-data', methods=['POST'])
@login_required
def get_items_by_total_sales():
    try:
        request_data = json.loads(request.data)
        from_date = request_data.get('fromDate')
        to_date = request_data.get('toDate')
        params = {
            'from_date': from_date,
            'to_date': to_date,
        }
        response = sale_report_controller.get_items_by_total_sales(params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/get-total-sales-categories', methods=['POST'])
@login_required
def get_categories_sales_by_total_sales():
    try:
        request_data = json.loads(request.data)
        from_date = request_data.get('fromDate')
        to_date = request_data.get('toDate')
        params = {
            'from_date': from_date,
            'to_date': to_date,
        }
        response = sale_report_controller.get_categories_sales_by_total_sales(
            params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/get-total-sales', methods=['POST'])
@login_required
def get_total_sales_by_month():
    try:
        sale = json.loads(request.data)
        option = sale.get('option')
        from_date = sale.get('fromDate')
        to_date = sale.get('toDate')
        params = {
            'option': option,
            'from_date': from_date,
            'to_date': to_date,
        }
        response = sale_report_controller.get_total_sales(params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/get-sale-report-daily/<date>')
@login_required
def get_sale_report_by_daily(date: str):
    try:
        response = sale_report_controller.get_sale_report_by_daily(date)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/get-qty-category', methods=['POST'])
@login_required
def get_qty_sold_by_category():
    try:
        sale = json.loads(request.data)
        option = sale.get('option')
        from_date = sale.get('fromDate')
        to_date = sale.get('toDate')
        params = {
            'option': option,
            'from_date': from_date,
            'to_date': to_date,
        }
        response = sale_report_controller.get_qty_sold_by_category(params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/get-revenue-category', methods=['POST'])
@login_required
def get_revenue_category():
    try:
        sale = json.loads(request.data)
        option = sale.get('option')
        from_date = sale.get('fromDate')
        to_date = sale.get('toDate')
        params = {
            'option': option,
            'from_date': from_date,
            'to_date': to_date,
        }
        response = sale_report_controller.get_revenue_category(params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/get-qty-item', methods=['POST'])
@login_required
def get_qty_sold_by_item():
    try:
        request_data = json.loads(request.data)
        option = request_data.get('option')
        from_date = request_data.get('fromDate')
        to_date = request_data.get('toDate')
        params = {
            'option': option,
            'from_date': from_date,
            'to_date': to_date,
        }
        response = sale_report_controller.get_qty_sold_by_item(params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/get-revenue-item', methods=['POST'])
@login_required
def get_revenue_item():
    try:
        request_data = json.loads(request.data)
        option = request_data.get('option')
        from_date = request_data.get('fromDate')
        to_date = request_data.get('toDate')
        params = {
            'option': option,
            'from_date': from_date,
            'to_date': to_date,
        }

        response = sale_report_controller.get_revenue_item(params)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/get-sale-growth', methods=['POST'])
@login_required
def get_sale_growth():
    try:
        request_data = json.loads(request.data)
        year = request_data.get('year')
        response = sale_report_controller.get_sale_growth(year)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/get-quarterly-sale', methods=['POST'])
@login_required
def get_quarterly_sale():
    try:
        request_data = json.loads(request.data)
        year = request_data.get('year')
        response = sale_report_controller.get_quarterly_sale(year)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/inventory-report-info', methods=['POST'])
@login_required
def get_inventory_report_info():
    try:
        year = request.args.get('year', '')
        response = inventory_report_controller.get_stock_info_by_year(year)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/monthly-inventory-info', methods=['POST'])
@login_required
def get_monthly_inventory_info():
    try:
        year = request.args.get('year', '')
        response = inventory_report_controller.get_stock_transactions_by_year(
            year)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/dashboard-sales-total', methods=['POST'])
@login_required
def get_dashboard_sales_total():
    try:
        response = dashboard_controller.sales()
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/dashboard-inventory-info', methods=['POST'])
@login_required
def get_dashboard_inventory_info():
    try:
        response = dashboard_controller.inventory_info()
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reports_bp.route('/report/dashboard-inventory-transactions', methods=['POST'])
@login_required
def get_dashboard_inventory_transactions():
    try:
        date = request.args.get('date', '')
        response = dashboard_controller.inventory_transactions(date)
        return jsonify({'data': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
