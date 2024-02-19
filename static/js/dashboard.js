function set_info(info) {
  $.each(info, function (key, value) {
    $("#" + key).text(value.toLocaleString('en-US', { minimumFractionDigits: 0 }));
  });
}

async function refresh_dashboard_sales_total() {
  $.ajax({
    url: '/report/dashboard-sales-total',
    method: 'POST',
    dataType: 'json',
    success: function (response) {
      set_info(response.data)
    },
    error: function (jqXHR, exception) {
      alert(jqXHR.responseJSON.error)
      console.error('AJAX request failed:', error);
    }
  });
}

async function refresh_dashboard_inventory_info() {
  $.ajax({
    url: '/report/dashboard-inventory-info',
    method: 'POST',
    dataType: 'json',
    success: function (response) {
      set_info(response.data)
    },
    error: function (jqXHR, exception) {
      alert(jqXHR.responseJSON.error)
      console.error('AJAX request failed:', error);
    }
  });
}

async function refresh_dashboard_inventory_transactions() {
  var date = $('#yearDropdownForInvMovement').val();
  $.ajax({
    url: '/report/dashboard-inventory-transactions?date=' + date,
    method: 'POST',
    dataType: 'json',
    success: function (response) {
      set_info(response.data)
    },
    error: function (jqXHR, exception) {
      alert(jqXHR.responseJSON.error)
      console.error('AJAX request failed:', jqXHR.responseJSON.error);
    }
  });
}

var myLineChart;
$.fn.fetchAndPopulateTotalSalesGraph = function (year) {
  let itemData = {
    'option': 'monthly',
    'fromDate': year + '-01-01',
    'toDate': year + '-12-31',
  }
  $.ajax({
    url: '/report/get-total-sales',
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(itemData),
    success: function (response) {
      var data = response.data;
      var xlabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

      var salesData = [];
      var profitData = [];

      Object.keys(xlabels).forEach(function (datetime) {
        salesData = Array(xlabels.length).fill(0);
        profitData = Array(xlabels.length).fill(0);

        data.forEach(function (item) {
          var index = xlabels.indexOf(item.tran_date);
          if (index !== -1) {
            salesData[index] = item.total_sales;
            profitData[index] = item.total_profit;
          } else {
            for (let i = 0; i < xlabels.length; i++) {
              var monthIndex = item.month.slice(5, 7) - 1;
              if (monthIndex !== -1) {
                salesData[monthIndex] = item.total_sales;
                profitData[monthIndex] = item.total_profit;
                break;
              }
            }
          }
        });
      });

      var chartData = {
        labels: xlabels,
        datasets: [{
          label: 'Total Sales',
          data: salesData,
          pointHoverRadius: 10,
        },
        {
          label: 'Total Profit',
          data: profitData,
          pointHoverRadius: 10,
        }]
      };

      var totalSales = document.getElementById("salesChartLine");
      if (totalSales) {
        if (!myLineChart) {
          myLineChart = new Chart(totalSales, {
            type: 'line',
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
                    text: 'Values'
                  },
                }
              },
              responsive: true
            }
          });
        } else {
          myLineChart.data = chartData;
          myLineChart.update();

        }
      }
    },
    error: function (jqXHR, exception) {
      console.error('Error fetching items:', jqXHR);
    }
  });
};


$("#yearDropdownForInvMovement").datepicker({
  dateFormat: 'yy-mm-dd',
  changeMonth: true,
  changeYear: true
});
$("#yearDropdownForInvMovement").datepicker('setDate', 'today');

$('#yearDropdownForInvMovement').change(function () {
  refresh_dashboard_inventory_transactions();
});

window.onload = function () {
  refresh_dashboard_sales_total();
  refresh_dashboard_inventory_info();
  refresh_dashboard_inventory_transactions();

  var date = new Date();
  var currentYear = date.getFullYear();
  $("#dashboard_year").text(currentYear)
  $.fn.fetchAndPopulateTotalSalesGraph(currentYear)
};