// utils.js
export function initializeDataTable(tableId, options) {
    const dataTable = $(`#${tableId}`).DataTable({
        searching: false
    });
    dataTable.on('init.dt', function () {
        this.api().column(0).nodes().each(function (cell, i) {
            cell.innerHTML = i + 1;
        });
    });

    return dataTable;
}

export function populateFormWithData(data, formTitleId, nameKey, type) {
    if (formTitleId) {
        const formTitle = $(`#${formTitleId}`);
        if (formTitle.length) {
            formTitle.text(`Edit ${type} - ${data[nameKey]}`);
        }
    }

    Object.keys(data).forEach(key => {
        const element = $(`#${key}`);
        if (element.length) {
            element.val(data[key]);
        }
    });
}



export function fetchData(url, type, data, successCallback) {
    const config = {
        url,
        type,
        data,
        dataType: 'json',
        success: successCallback,
        error: function (jqXHR, exception) {
            alert(jqXHR.responseJSON.error)
            console.error('Error:', jqXHR);
        }
    };

    $.ajax(config);
}

export function updateDataTable(dataTable, data, formatDataCallback, dataType) {
    dataTable.clear().draw();
    data.forEach((data, index) => {
        const formattedData = formatDataCallback(data, index, dataType);
        dataTable.row.add(formattedData).draw();
    });
}

export function saveOrUpdateData(url, data, successCallback) {
    $.ajax({
        url: url,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: successCallback,
        error: function (jqXHR, exception) {
            alert(jqXHR.responseJSON.error)
            console.error('Error saving: ', jqXHR);
        }
    });
}

export function deleteData(url, successCallback) {
    $.ajax({
        url: url,
        type: 'DELETE',
        success: successCallback,
        error: function (jqXHR, exception) {
            alert(jqXHR.responseJSON.error)
            console.error('Error deleting Data:', jqXHR);
        }
    });
}

export function confirmDelete(message, callback) {
    if (confirm(message)) {
        callback();
    }
}