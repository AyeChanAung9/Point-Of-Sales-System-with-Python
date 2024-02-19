function initializeDatepicker() {
    const elems = document.querySelectorAll('.datepicker_input');
    for (const elem of elems) {
        const datepicker = new Datepicker(elem, {
            'format': 'yyyy-mm-dd',
            "autohide": 1
        });
    }
}

function setTodayDate() {
    var today = new Date();
    document.getElementById("date").value = today.getFullYear() + '-' + ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
}

function generateVoucherNo() {
    var today = new Date();
    randomnum = today.getFullYear() + '' + today.getMonth() + '' + today.getDate() + '' + today.getTime();
    randomnum = "S" + randomnum;
    document.getElementById('voucherNo').value = randomnum;
}

function getVoucherInfo(details) {
    voucherNo = document.getElementById('voucherNo').value
    date = document.getElementById('date').value
    total_items = document.getElementById('total_item_count').innerText
    discount = document.getElementById('discount').value
    totals = document.getElementById('totals').value
    discount_percentage = document.getElementById('discount_percentage').value
    sale_id = document.getElementById('sale_id').value
    user_id = document.getElementById('login_user_id').value

    selectElement = document.querySelector('#payment');
    payment = selectElement.value;
    console.log(payment);

    var sale = {
        "voucher_no": voucherNo,
        'tran_date': date,
        'total_items': total_items,
        'user_id': user_id,
        'discount': discount,
        "details": details,
        "total_amount": totals,
        "discount_percentage": discount_percentage,
        "payment": payment,
    };
    if (sale_id) {
        sale["sale_id"] = sale_id
        sale["delete_ids"] = delete_ids
    }
    return sale
}


function getItemsInfo() {
    const tableRows = document.querySelectorAll('table tr');
    const tableData = [];
    for (let i = 1; i < tableRows.length; i++) {
        const row = tableRows[i];
        const cells = row.getElementsByTagName('td');
        const product_code = cells[0].textContent;
        const name = cells[1].textContent;
        const category_name = cells[2].textContent;

        const price = cells[3].textContent;
        const qtyInput = cells[4].querySelector('input[type="number"]');
        const qty = qtyInput ? qtyInput.value : 1;

        const item_id = cells[6].textContent;
        const sale_detail_id = (cells[7].textContent == 'undefined') ? null : cells[7].textContent;
        tableData.push({ "product_code": product_code, "name": name, "category_name": category_name, "qty": qty, "item_id": item_id, "sale_detail_id": sale_detail_id, "price": price });
    }
    return tableData
}

function saveSaleVoucher(event) {
    event.preventDefault();
    details = getItemsInfo()
    if (details.length == 0) {
        alert("Sorry, no items have been added to the voucher yet. Please add items to the voucher before proceeding.")
        return
    }
    fetch('/sale/save_sale_voucher', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
        },
        body: JSON.stringify(getVoucherInfo(details))
    })
        .then(async function (response) {
            var data = await response.json();
            if (!response.ok) {
                throw data.error;
            }
            return data
        })
        .then(function (data) {
            alert(data.message);
            clearAllInfo()
        })
        .catch(error => {
            alert(error)
            console.error('Error Sale :', error);
        });

}
function updateSaleVoucher(event) {
    event.preventDefault();
    details = getItemsInfo()
    if (details.length == 0) {
        alert("Sorry, no items have been added to the voucher yet. Please add items to the voucher before proceeding.")
        return
    }
    fetch('/sale/update-sale-voucher', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
        },
        body: JSON.stringify(getVoucherInfo(details))
    })
        .then(async function (response) {
            var data = await response.json();
            if (!response.ok) {
                throw data.error;
            }
            return data
        })
        .then(function (data) {
            alert(data.message);
            window.location.href = "/sale"
        })
        .catch(error => {
            alert(error)
            console.error('Error Sale :', error);

        });

}

async function get_item_by_product_code(product_search) {
    try {
        const response = await fetch('/inventory/get_item_by_product_code?product_code=' + product_search);
        var data = await response.json();
        if (!response.ok) {
            throw data.error;
        }
        return data.data;
    } catch (error) {
        alert(error);
        console.error('Fetch error:', error);
    }
}

{/* <td>${currencyFormat.addComma(item['price'])}</td> */ }
function appendItemRowAndIncreaseCount(item) {
    //add new item row
    const item_table = document.getElementById("item_table_body");
    let newRow = document.createElement("tr");
    item['totals'] = item['price'] * qty;
    newRow.innerHTML = `
    <td>${item['product_code']}</td>
    <td colspan="4">${item['name']}</td>
    <td>${item['category_name']}</td>
    <td class="text-end">${formatNumber(item['price'])}</td>
    <td><input type="number" class="form-control text-end" min="1" onclick="changeTotalsByQty(this)" value=${qty} pattern="[0-9]*"></td>
    <td class="text-end">${formatNumber(item['totals'])}</td>
    <td hidden="true">${item['item_id']}</td>
    <td hidden="true">${item['sale_details_id']}</td>
    <td class="text-center">
        <a class="delete" title="Delete" data-toggle="tooltip" type="button" onclick="removeItemFromTable(this)"><i class="fas fa-trash red-icon"></i></a>
    </td>`;

    item_table.appendChild(newRow);
    console.log(item_table.rows);
    //increase count
    document.getElementById("total_item_count").innerHTML = item_table.rows.length;

}

function calculateSubTotal() {
    var sub_total_amount = 0;
    const tableRows = document.querySelectorAll('table tr');
    for (let i = 1; i < tableRows.length; i++) {
        const row = tableRows[i];
        const cells = row.getElementsByTagName('td');

        const amount = cells[5].textContent.trim();
        const total = parseFormattedNumber(amount);
        sub_total_amount += total;
    }
    discount_percentage = document.getElementById('discount_percentage').value;

    document.getElementById('sub_total').value = formatNumber(sub_total_amount).toString();

    getDiscount(discount_percentage);
}

function parseFormattedNumber(value) {
    return parseFloat(value.replace(/[^0-9.-]+/g, '').replace(/,/g, ''));
}

function formatNumber(number) {
    return Number(number).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
}


function changeTotalsByQty(input) {
    var row = input.parentNode.parentNode;
    var cells = row.getElementsByTagName("td");
    var totals = cells[5].textContent;
    var price = parseFormattedNumber(cells[3].textContent);
    var qtyInput = cells[4].querySelector('input[type="number"]');
    totals = price * qtyInput.value;
    cells[5].innerHTML = formatNumber(totals);
    calculateSubTotal();
}

async function getDiscount(discount_percentage) {
    document.getElementById('discount_percentage').value = discount_percentage;
    var sub_total = parseFormattedNumber(document.getElementById('sub_total').value);
    var discount = sub_total * (discount_percentage / 100);
    var totals = sub_total - discount;
    document.getElementById('discount').value = formatNumber(discount).toString();
    document.getElementById('totals').value = formatNumber(totals).toString();
}


async function addItemToTable() {
    product_search = document.getElementById('product_search').value
    qty = document.getElementById('qty').value

    item = await get_item_by_product_code(product_search);
    console.log("item ", item)
    if (item == undefined)
        return;
    appendItemRowAndIncreaseCount(item);
    calculateSubTotal();
    clearItemInfo();
}

const delete_ids = [];
function removeItemFromTable(btn) {
    var row = btn.parentNode.parentNode;
    var cells = row.getElementsByTagName("td");
    var sale_detail_id = cells[7].textContent;
    if (sale_detail_id != undefined)
        delete_ids.push(sale_detail_id)
    row.parentNode.removeChild(row);
    document.getElementById("total_item_count").innerHTML = item_table.rows.length - 1;
    calculateSubTotal();
}

function clearAllInfo() {
    document.getElementById("voucherNo").value = "";
    document.getElementById("total_item_count").innerHTML = 0;
    document.getElementById("sub_total").value = "";
    document.getElementById("discount_percentage").value = 0;
    document.getElementById("discount").value = "";
    document.getElementById("totals").value = "";
    document.getElementById("payment").value = "";
    generateVoucherNo()
    setTodayDate()
    clearItemInfo()
    clearTable()
}

function clearTable() {
    var tableBody = document.getElementById("item_table_body");
    while (tableBody.firstChild) {
        tableBody.removeChild(tableBody.firstChild);
    }
}

function clearItemInfo() {
    document.getElementById("product_search").value = "";
    document.getElementById("qty").value = 1;
}

initializeDatepicker()

window.onload = function () {
    calculateSubTotal();
    voucherNo = document.getElementById('voucherNo').value
    date = document.getElementById('date').value
    if (!(date && voucherNo)) {
        setTodayDate();
        generateVoucherNo();
    }
};