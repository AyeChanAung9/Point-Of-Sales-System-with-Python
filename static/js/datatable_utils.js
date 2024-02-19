import { formatCurrency } from './currency_format.js';

function formatData(data, index, dataType) {
    const formatFields = getFormatFieldsFunction(dataType);
    return formatFields(data, index);
}

function getFormatFieldsFunction(dataType) {
    const formatFunctions = {
        'item': formatItemFields,
        'category': formatCategoryFields,
        'item_receive': formatItemReceiveFields,
        'item_receive_detail': formatItemReceiveDetailFields,
        'damage_loss': formatDamageLossFields,
        'damage_loss_detail': formatDamageLossDetailFields,
        'sale': formatSaleFields,
        'sale_detail': formatSaleDetailFields,
        'user': formatUserFields,
        'role': formatRoleFields,
        'default': () => []
    };

    return formatFunctions[dataType] || formatFunctions['default'];
}

function formatItemFields(item, index) {
    return [
        index + 1,
        item.name,
        item.product_code,
        formatCurrency(item.cost_price),
        formatCurrency(item.price),
        formatCurrency(item.reorder),
        item.category_name,
        formatCurrency(item.current_stock),
        formatActions('edit-item', 'delete-item', '', item.item_id)
    ];
}

function formatCategoryFields(category, index) {
    return [
        index + 1,
        category.category_name,
        formatActions('edit-category', 'delete-category', '', category.category_id)
    ];
}

function formatItemReceiveFields(itemReceive, index) {
    return [
        index + 1,
        itemReceive.voucher_no,
        itemReceive.tran_date,
        formatCurrency(itemReceive.total_items),
        itemReceive.username,
        formatActions('item-receive', 'delete-item', 'view-item', itemReceive.item_receive_id, itemReceive.voucher_no)
    ];
}

function formatItemReceiveDetailFields(itemReceive, index) {
    return [
        index + 1,
        itemReceive.name,
        itemReceive.category_name,
        formatCurrency(itemReceive.cost_price),
        formatCurrency(itemReceive.qty),
        formatCurrency(itemReceive.reorder)
    ];
}

function formatDamageLossFields(damageLoss, index) {
    return [
        index + 1,
        damageLoss.voucher_no,
        damageLoss.tran_date,
        formatCurrency(damageLoss.total_items),
        damageLoss.username,
        formatActions('damage-loss', 'delete-item', 'view-item', damageLoss.damage_loss_id, damageLoss.voucher_no)
    ];
}

function formatDamageLossDetailFields(damageLoss, index) {
    return [
        index + 1,
        damageLoss.name,
        damageLoss.category_name,
        formatCurrency(damageLoss.price),
        formatCurrency(damageLoss.qty),
        formatCurrency(damageLoss.reorder),
        damageLoss.remark
    ];
}

function formatSaleFields(sale, index) {
    const paymentType = getPaymentType(sale.payment);
    return [
        index + 1,
        sale.voucher_no,
        sale.tran_date,
        formatCurrency(sale.total_items),
        formatCurrency(sale.discount),
        formatCurrency(sale.total_amount),
        paymentType,
        sale.username,
        formatActions('sale', 'delete-item', 'view-item', sale.sale_id, sale.voucher_no)
    ];
}

function formatSaleDetailFields(sale, index) {
    return [
        index + 1,
        sale.name,
        sale.category_name,
        formatCurrency(sale.price),
        formatCurrency(sale.qty),
        formatCurrency(sale.reorder)
    ];
}

function formatUserFields(user, index) {
    return [
        index + 1,
        user.username,
        user.role_name,
        formatActions('edit-user', 'delete-user', '', user.user_id)
    ];
}

function formatRoleFields(role, index) {
    return [
        index + 1,
        role.role_name,
        `<a class="permissions-role" data-id="${role.role_id}" href="/setting/user_permission/${role.role_id}/${role.role_name}"><i class="far fa-lock" style="color: #feb204;"></i></a> ` +
        formatActions('edit-role', 'delete-role', '', role.role_id)
    ];
}

function formatActions(editClass, deleteClass, viewClass, id, voucherNo = '') {
    const viewAction = viewClass ? `<a class="${viewClass}" title="View Item" data-id="${id}" data-voucher-id="${voucherNo}" href=""><i class="far fa-eye text-secondary"></i></a> ` : '';

    let editAction = '';
    if (editClass === 'sale') {
        editAction = `<a class="${editClass}" title="Edit Item" data-id="${id}" href="/sale/${editClass}-voucher/${voucherNo}"><i class="far fa-edit mx-3"></i></a> `;
    } else {
        editAction = `<a class="${editClass}" title="Edit Item" data-id="${id}" href="/inventory/${editClass}-voucher/${voucherNo}"><i class="far fa-edit mx-3"></i></a> `;
    }

    const deleteAction = `<a class="${deleteClass}" title="Delete Item" data-id="${id}" href=""><i class="fas fa-trash text-danger"></i></a>`;

    return `${viewAction}${editAction}${deleteAction}`;
}

function getPaymentType(payment) {
    switch (payment) {
        case 'cshp':
            return 'Cash Payment';
        case 'crdp':
            return 'Card Payment';
        case 'dgtp':
            return 'Digital Payment';
        default:
            return '';
    }
}

export { formatData };