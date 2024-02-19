import { formatCurrency } from './currency_format.js';

export function configureDatepicker() {
    $("#yearDropdownForSaleReport").datepicker({
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true
    });
    $("#yearDropdownForSaleReport").datepicker('setDate', 'today');
}

export function calculateDateRange(inlineRadioOptions) {
    let fromDate, toDate;

    if (inlineRadioOptions === 'daily') {
        fromDate = $('#from').val();
        toDate = $('#to').val();
    } else if (inlineRadioOptions === 'weekly') {
        const year = $('#yearDropdown').val();
        const month = $('#monthDropdown').val();
        const last_day = new Date(year, month, 0).getDate();
        fromDate = `${year}-${month}-01`;
        toDate = `${year}-${month}-${last_day}`;
    } else if (inlineRadioOptions === 'monthly') {
        const year = $('#yearDropdown_for_monthly').val();
        fromDate = `${year}-01-01`;
        toDate = `${year}-12-31`;
    }

    return { fromDate, toDate };
}


export function fetchDataAndPopulateReports(inlineRadioOptions, fromDate, toDate) {
    $.fn.fetchAndPopulateTotalSalesGraph(inlineRadioOptions, fromDate, toDate)
    $.fn.fetchAndPopulateQtySoldByCategory(inlineRadioOptions, fromDate, toDate)
    $.fn.fetchAndPopulateRevenueCategory(inlineRadioOptions, fromDate, toDate)
    $.fn.fetchAndPopulateQtySoldByItem(inlineRadioOptions, fromDate, toDate)
    $.fn.fetchAndPopulateRevenueItem(inlineRadioOptions, fromDate, toDate)
    $.fn.fetchAndPopulateSaleGrowth(fromDate.slice(0, 4))
    $.fn.fetchAndPopulateQuarterlySale(fromDate.slice(0, 4))
    $.fn.fetchAndPopulateTopSelling(fromDate, toDate)
}

export function fetchAndPopulateTable(url, tableId, rowCreationFn, method, data, successCallback, errorCallback) {
    $.ajax({
        url: url,
        type: method,
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function (response) {
            var data = response.data;
            var counter = 1;
            var tableElement = $("#" + tableId);

            // Clear the existing content of the tbody
            tableElement.empty();

            if (data.length > 0) {
                data.forEach(function (item, index) {
                    // Use the provided rowCreationFn to create a new row
                    var newRow = rowCreationFn(tableElement, counter++, item);

                    // Append the new row to the table
                    tableElement.append(newRow);
                });
            } else {
                // If no data is available, display a message
                const numCols = tableElement.find("th").length;
                $("<tr>").appendTo(tableElement).append($("<td>").attr("colspan", numCols).addClass("text-center").text("No data available"));
            }

            if (successCallback) {
                successCallback();
            }
        },
        error: function (jqXHR, exception) {
            console.error('Error fetching items:', jqXHR.responseJSON.error);
            if (errorCallback) {
                errorCallback(jqXHR.responseJSON.error);
            }
        }
    });
}

export function createReportTableRow(tableElement, counter, item) {
    var newRow = $("<tr>").appendTo(tableElement);

    $("<td>").text(counter).appendTo(newRow);
    $("<td>").text(item.voucher_no).appendTo(newRow);
    $("<td>").text(item.item_name).appendTo(newRow);
    $("<td>").text(item.category_name).appendTo(newRow);
    $("<td>").addClass("text-end").text(item.qty).appendTo(newRow);
    $("<td>").html(formatCurrency(item.discount)).appendTo(newRow);
    $("<td>").html(formatCurrency(item.price)).appendTo(newRow);
    $("<td>").html(formatCurrency(item.total_price)).appendTo(newRow);

    return newRow;
}

export function createTopSellingRow(tableElement, counter, item) {
    var newRow = $("<tr>").appendTo(tableElement);

    $("<td>").text(counter).appendTo(newRow);
    $("<td>").text(item.item_name).appendTo(newRow);
    $("<td>").text(item.category_name).appendTo(newRow);
    $("<td>").addClass("text-end").text(item.qty).appendTo(newRow);
    $("<td>").html(formatCurrency(item.price)).appendTo(newRow);
    $("<td>").html(formatCurrency(item.sales)).appendTo(newRow);

    return newRow;
}

export function getLabels(fromDate, toDate, interval) {
    var labels = [];
    var currentDate = new Date(fromDate);

    switch (interval) {
        case 'daily':
            while (currentDate <= new Date(toDate)) {
                labels.push(currentDate.toISOString().slice(0, 10));
                currentDate.setDate(currentDate.getDate() + 1);
            }
            break;

        case 'weekly':
            var d = new Date(toDate);
            var endDate = new Date(d.setDate(d.getDate() + 6 - d.getDay()));
            while (currentDate <= endDate) {
                var weekStart = new Date(currentDate);
                weekStart.setDate(currentDate.getDate() - currentDate.getDay()); // Sunday
                var weekEnd = new Date(weekStart);
                weekEnd.setDate(weekStart.getDate() + 6); // Saturday
                labels.push(weekStart.toLocaleString('default', { month: 'short' }) + ' ' + weekStart.getDate() + ' to ' + weekEnd.toLocaleString('default', { month: 'short' }) + ' ' + weekEnd.getDate());
                currentDate.setDate(currentDate.getDate() + 7);
            }
            break;

        case 'monthly':
            labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            break;

        default:
            console.error('Invalid interval provided');
            break;
    }

    return labels;
}

export function getLineChartReport(type, data, xlabels, option, valueFields) {
    var datasets = [];
    var dataDict = {};

    valueFields.forEach(function (valueField) {
        dataDict[valueField] = [];
    });

    data.forEach(function (item) {
        if (!dataDict[item[type]] && typeof item[type] !== "undefined") {
            dataDict[item[type]] = [];
        }

        valueFields.forEach(function (valueField) {
            var value = (valueField === 'qty') ? item.qty :
                (valueField === 'total_price') ? item.total_price :
                    (valueField === 'total_sales') ? item.total_sales :
                        (valueField === 'total_profit') ? item.total_profit : null;

            if (value !== null) {
                var date = item.tran_date.slice(0, 10);

                if (!dataDict[valueField]) {
                    dataDict[valueField] = [];
                }

                var existingData = dataDict[valueField].find(entry => entry.date === date);

                if (existingData) {
                    existingData.value = value;
                } else {
                    dataDict[valueField].push({
                        date: date,
                        value: value
                    });
                }
            }
        });

    });

    Object.keys(dataDict).forEach(function (data) {
        var values = Array(xlabels.length).fill(0);

        dataDict[data].forEach(function (item) {
            var index = xlabels.indexOf(item.date);
            if (index !== -1) {
                values[index] = item.value;
            } else {
                for (let i = 0; i < xlabels.length; i++) {
                    if (option === 'weekly') {
                        const startDateString = xlabels[i].split(' to ')[0];
                        const endDateString = xlabels[i].split(' to ')[1];
                        const startDate = new Date(startDateString + ' ' + (new Date(item.date)).getFullYear());
                        const endDate = new Date(endDateString + ' ' + (new Date(item.date)).getFullYear());
                        const currentDate = new Date(item.date);

                        currentDate.setHours(0, 0, 0, 0);

                        if (currentDate >= startDate && currentDate <= endDate) {
                            values[i] = item.value;
                            break;
                        }
                    } else if (option === 'monthly') {
                        var monthIndex = item.date.slice(5, 7) - 1;
                        if (monthIndex !== -1) {
                            values[monthIndex] = item.value;
                            break;
                        }
                    }
                }
            }
        });

        datasets.push({
            label: data,
            data: values,
            fill: (valueFields[0] === 'qty'),
            pointHoverRadius: 10
        });
    });

    return datasets;
}

export function getDataByCategory(data, xlabels, option) {
    const field = ['category_name'];
    return getLineChartReport(field, data, xlabels, option, ['qty']);
}

export function getDataByProduct(data, xlabels, option) {
    const field = ['item_name'];
    return getLineChartReport(field, data, xlabels, option, ['qty']);
}

export function getRevenueCategory(data, xlabels, option) {
    const field = ['category_name'];
    return getLineChartReport(field, data, xlabels, option, ['total_price']);
}

export function getRevenueProduct(data, xlabels, option) {
    const field = ['item_name'];
    return getLineChartReport(field, data, xlabels, option, ['total_price']);
}

export function createOrUpdateChart(existingChart, chartId, chartType, chartData, additionalOptions = {}) {
    let chartInstance;

    if (!existingChart) {
        chartInstance = new Chart(chartId, {
            type: chartType,
            data: chartData,
            options: {
                legend: {
                    display: false
                },
                scales: {
                    x: {
                        beginAtZero: false,
                        title: {
                            display: true,
                        }
                    },
                    y: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Value'
                        },
                        ...additionalOptions.y,
                    }
                },
                responsive: true,
                ...additionalOptions,
            }
        });
    } else {
        chartInstance = existingChart;
        chartInstance.data.labels = chartData.labels;
        chartInstance.data.datasets = chartData.datasets;
        chartInstance.update();
    }

    return chartInstance;
}

export function formatDate(date) {
    const [month, day] = date.split(' ');
    const paddedMonth = (new Date(Date.parse(month + " 1, 2000"))).getMonth() + 1;
    const formattedMonth = paddedMonth.toString().padStart(2, '0');
    const paddedDay = day.padStart(2, '0');
    return formattedMonth + '-' + paddedDay;
}