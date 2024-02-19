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
    randomnum = "DL" + randomnum;
    document.getElementById('voucherNo').value = randomnum;
}

function getVoucherInfo(details) {
    voucherNo = document.getElementById('voucherNo').value
    date = document.getElementById('date').value
    total_items = document.getElementById('total_item_count').innerText
    damage_loss_id = document.getElementById('damage_loss_id').value
    user_id = document.getElementById('login_user_id').value
    var damage_loss = {
        "voucher_no": voucherNo,
        'tran_date': date,
        'total_items': total_items,
        'user_id': user_id,
        "details": details
    };
    if (damage_loss_id) {
        damage_loss["damage_loss_id"] = damage_loss_id
        damage_loss["delete_ids"] = delete_ids
    }
    return damage_loss
}


function getItemsInfo() {
    const tableRows = document.querySelectorAll('table tr');
    const tableData = [];
    damage_loss_id = document.getElementById('damage_loss_id').value
    for (let i = 1; i < tableRows.length; i++) {
        const row = tableRows[i];
        const cells = row.getElementsByTagName('td');
        const product_code = cells[0].textContent;
        const name = cells[1].textContent;
        const category_name = cells[2].textContent;

        const qtyInput = cells[3].querySelector('input[type="number"]');
        const qty = qtyInput ? qtyInput.value : 1;

        const item_id = cells[4].textContent;
        const damage_loss_details_id = (cells[5].textContent == 'undefined') ? null : cells[5].textContent;
        const remark = cells[6].textContent;
        if (damage_loss_id) {
            tableData.push({ "damage_loss_details_id": damage_loss_details_id, "damage_loss_id": damage_loss_id, "item_id": item_id, "product_code": product_code, "name": name, "category_name": category_name, "qty": qty, "remark": remark });
        } else {
            tableData.push({ "product_code": product_code, "name": name, "category_name": category_name, "qty": qty, "remark": remark, "item_id": item_id, "damage_loss_details_id": damage_loss_details_id });
        }

    }
    return tableData
}

function saveDamageLossVoucher(event) {
    event.preventDefault();
    details = getItemsInfo()
    if (details.length == 0) {
        alert("Sorry, no items have been added to the voucher yet. Please add items to the voucher before proceeding.")
        return
    }
    fetch('/inventory/save_damage_loss_voucher', {
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
            console.error('Error:', error)

        });
}
function updateDamageLossVoucher(event) {
    event.preventDefault();
    details = getItemsInfo()
    if (details.length == 0) {
        alert("Sorry, no items have been added to the voucher yet. Please add items to the voucher before proceeding.")
        return
    }
    fetch('/inventory/update-damage-loss-voucher', {
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
            window.location.href = "/inventory/damage-loss"
        })
        .catch(error => {
            alert(error)
            console.error('Error:', error)

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

function appendItemRowAndIncreaseCount(item) {
    //add new item row
    const item_table = document.getElementById("item_table_body");
    remark = document.getElementById('remark').value
    let newRow = document.createElement("tr");
    newRow.innerHTML = `
    <td>${item['product_code']}</td>
    <td colspan="4">${item['name']}</td>
    <td>${item['category_name']}</td>
    <td><input type="number" class="form-control text-end col-md-1" min="1" value=${qty} pattern="[0-9]*"></td>
    <td hidden="true">${item['item_id']}</td>
    <td hidden="true">${item['damage_loss_details_id']}</td>
    <td>${remark}</td>
    <td class="text-center">
        <a class="delete" title="Delete" data-toggle="tooltip" type="button" onclick="removeItemFromTable(this)"><i class="fas fa-trash red-icon"></i></a>
    </td>`;

    item_table.appendChild(newRow);

    //increase count
    document.getElementById("total_item_count").innerHTML = item_table.rows.length;
}

async function addItemToTable() {
    product_search = document.getElementById('product_search').value
    qty = document.getElementById('qty').value

    item = await get_item_by_product_code(product_search);
    console.log("item ", item)
    if (item == undefined)
        return;
    appendItemRowAndIncreaseCount(item);
    clearItemInfo();
}

const delete_ids = [];
function removeItemFromTable(btn) {
    var row = btn.parentNode.parentNode;
    var cells = row.getElementsByTagName("td");
    var damage_loss_details_id = cells[5].textContent;
    if (damage_loss_details_id != undefined)
        delete_ids.push(damage_loss_details_id)
    row.parentNode.removeChild(row);
    document.getElementById("total_item_count").innerHTML = item_table.rows.length - 1;
}

function clearAllInfo() {
    document.getElementById("voucherNo").value = "";
    document.getElementById("total_item_count").innerHTML = 0;
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
    document.getElementById("remark").value = "";
}

initializeDatepicker()

window.onload = function () {
    voucherNo = document.getElementById('voucherNo').value
    date = document.getElementById('date').value
    if (!(date && voucherNo)) {
        setTodayDate();
        generateVoucherNo();
    }
};