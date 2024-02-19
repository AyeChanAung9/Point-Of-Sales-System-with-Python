function set_inventory_report_info(info) {
    $.each(info, function (key, value) {
        $("#" + key).text(value.toLocaleString('en-US', { minimumFractionDigits: 0 }));
    });
}

function get_selection_year() {
    var selectedValue = $("#selectBy").val();

    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();

    if (selectedValue == "this_year") {
        $("#inv_qty_year").text(currentYear)
        return currentYear
    }
    $("#inv_qty_year").text(currentYear - 1)
    return currentYear - 1
}

async function refresh_inventory_report_info(year) {
    $.ajax({
        url: '/report/inventory-report-info?year=' + year,
        method: 'POST',
        dataType: 'json',
        success: function (response) {
            set_inventory_report_info(response.data)
        },
        error: function (jqXHR, exception) {
            alert(jqXHR.responseJSON.error)
            console.error('AJAX request failed:', jqXHR.responseJSON.error)
        }
    });
}


var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

var myInvBarChart;
$.fn.fetchAndPopulateMonthlyInventory = function (year) {
    $.ajax({
        url: '/report/monthly-inventory-info?year=' + year,
        type: 'POST',
        contentType: 'application/json',
        success: function (response) {
            var data = response.data;
            var invBarChart = $("#invBarChart")[0];
            if (!myInvBarChart) {
                var barChartData = {
                    labels: monthNames,
                    datasets: [{
                        label: 'Received',
                        backgroundColor: "GoldenRod",
                        borderWidth: 1,
                        data: data.receive_values,
                        fill: false,
                    }, {
                        label: 'Sales',
                        backgroundColor: "Grey",
                        borderWidth: 1,
                        data: data.sale_values,
                        fill: false,
                    }, {
                        label: 'Damage/Loss',
                        backgroundColor: "Teal",
                        borderWidth: 1,
                        data: data.damage_loss_values,
                        fill: false,
                    }
                    ]
                };
                myInvBarChart = new Chart(invBarChart, {
                    type: 'bar',
                    data: barChartData,
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            } else {
                myInvBarChart.data.datasets[0].data = data.receive_values;
                myInvBarChart.data.datasets[1].data = data.sale_values;
                myInvBarChart.data.datasets[2].data = data.damage_loss_values;
                myInvBarChart.update();
            }

        },
        error: function (jqXHR, exception) {
            alert(jqXHR.responseJSON.error)
            console.error('Error fetching items:', jqXHR.responseJSON.error)
        }
    });
};

function refresh_all() {
    var year = get_selection_year()
    refresh_inventory_report_info(year);
    $.fn.fetchAndPopulateMonthlyInventory(year);
}

$("#selectBy").on("change", function () {
    refresh_all();
});

window.onload = function () {
    refresh_all()
};