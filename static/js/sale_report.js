import * as utils from './report_utils.js';
import { saveOrUpdateData } from './utils.js';

$(document).ready(function () {
    $("#daily, #weekly, #monthly").click(function () {
        const inlineRadioOptions = $(this).val();
        if (inlineRadioOptions === 'daily') {
            $("#from_to_date").show();
            $('#weekly_select').hide();
            $('#monthly_select').hide();
        }
        if (inlineRadioOptions === 'weekly') {
            $('#weekly_select').show();
            $("#from_to_date").hide();
            $('#monthly_select').hide();
        }
        if (inlineRadioOptions === 'monthly') {
            $('#monthly_select').show();
            $("#from_to_date").hide();
            $('#weekly_select').hide();
        }
    });
    $("#monthly").click();

    $('#searchForm').submit(function (event) {
        event.preventDefault();
        var inlineRadioOptions = $('input[name="inlineRadioOptions"]:checked').val();

        // Calculate date range
        const { fromDate, toDate } = utils.calculateDateRange(inlineRadioOptions);

        $("#yearForTotalSales").val(fromDate.slice(0, 4));
        $("#saleGrowthYear").text(fromDate.slice(0, 4));
        $("#productWiseYear").text(fromDate.slice(0, 4));

        utils.fetchDataAndPopulateReports(inlineRadioOptions, fromDate, toDate);
    });

    setTimeout(function () {
        $('#searchForm').submit();
    }, 100);

    utils.configureDatepicker();

    var date = $('#yearDropdownForSaleReport').val();
    var myLineChart;
    var myCateogryChart;
    var myBarChart;
    var myRevenueCategoryChart;
    var myQtySoldCategoryChart;
    var myQtySoldItemChart;
    var myRevenueItemChart;
    var mySaleGrowthChart;
    var myQuarterlySalesChart;
    var xSaleLabel;
    var datasets;


    $.fn.fetchAndPopulateSaleGrowth = function (year) {
        const url = '/report/get-sale-growth';
        const saleGrowthData = { 'year': year, };

        saveOrUpdateData(url, saleGrowthData, function (response) {
            var data = response.data;

            var itemNames = [];
            var salePercentages = [];

            data.forEach(function (item) {
                itemNames.push(item.item_name);
                salePercentages.push(item.sale_percentage);
            });
            var barChartData = {
                labels: itemNames,
                datasets: [{
                    label: 'Sale Percentage',
                    data: salePercentages,
                }]
            };

            var saleGrowth = document.getElementById("saleGrowth");
            if (saleGrowth) {
                mySaleGrowthChart = utils.createOrUpdateChart(mySaleGrowthChart, saleGrowth, 'bar', barChartData, {
                    y: {
                        min: 0,
                        max: 100,
                        ticks: {
                            callback: (value) => {
                                return `${value}.0%`;
                            }
                        }
                    }
                });
            }
        });
    };

    $.fn.fetchAndPopulateQuarterlySale = function (year) {
        const url = '/report/get-quarterly-sale';
        const quarterData = { 'year': year, }
        saveOrUpdateData(url, quarterData, function (response) {
            var data = response.data;
            var items = [...new Set(data.map(entry => entry.item_name))];
            var datasets = [];

            ['Q1', 'Q2', 'Q3', 'Q4'].forEach(function (quarter) {
                var quarterData = [];
                items.forEach(function (item) {
                    var itemQuarterData = data.find(entry => entry.item_name === item && entry.quarter.toString() === quarter.substring(1));
                    quarterData.push(itemQuarterData ? itemQuarterData.total_quarterly_sales : 0);
                });

                datasets.push({
                    label: quarter,
                    data: quarterData,
                    borderWidth: 1
                });
            });


            var quarterlySalesChart = document.getElementById("quarterlySalesChart");
            if (quarterlySalesChart) {
                myQuarterlySalesChart = utils.createOrUpdateChart(myQuarterlySalesChart, quarterlySalesChart, 'bar', {
                    labels: items,
                    datasets: datasets
                });
            }
        });
    };

    $.fn.fetchAndPopulateQtySoldByCategory = function (option, fromDate, toDate) {
        const url = '/report/get-qty-category';
        const categoryData = {
            'option': option,
            'fromDate': fromDate,
            'toDate': toDate,
        }
        saveOrUpdateData(url, categoryData, function (response) {
            var data = response.data;

            var xlabels = [];

            if (['daily', 'weekly', 'monthly'].includes(option)) {
                xlabels = utils.getLabels(fromDate, toDate, option);
            } else {
                console.error('Invalid interval provided');
            }
            datasets = utils.getDataByCategory(data, xlabels, option);

            var chartData = {
                labels: xlabels,
                datasets: datasets,
                pointHoverRadius: 10,
                fill: true,
            };

            var qtySoldCategory = document.getElementById("qtySoldCategory");
            if (qtySoldCategory) {
                myQtySoldCategoryChart = utils.createOrUpdateChart(myQtySoldCategoryChart, qtySoldCategory, 'line', chartData);
            }
        });

    };

    $.fn.fetchAndPopulateQtySoldByItem = function (option, fromDate, toDate) {
        const url = '/report/get-qty-item';
        const itemData = {
            'option': option,
            'fromDate': fromDate,
            'toDate': toDate,
        }
        saveOrUpdateData(url, itemData, function (response) {
            var data = response.data;

            var xlabels = [];

            if (['daily', 'weekly', 'monthly'].includes(option)) {
                xlabels = utils.getLabels(fromDate, toDate, option);
            } else {
                console.error('Invalid interval provided');
            }
            datasets = utils.getDataByProduct(data, xlabels, option);
            var chartData = {
                labels: xlabels,
                datasets: datasets,
                pointHoverRadius: 10,
                fill: true,
            };

            var qtySoldItem = document.getElementById("qtySoldItem");
            if (qtySoldItem) {
                myQtySoldItemChart = utils.createOrUpdateChart(myQtySoldItemChart, qtySoldItem, 'line', chartData);
            }
        });

    };

    $.fn.fetchAndPopulateRevenueCategory = function (option, fromDate, toDate) {
        const url = '/report/get-revenue-category';
        const categoryData = {
            'option': option,
            'fromDate': fromDate,
            'toDate': toDate,
        }
        saveOrUpdateData(url, categoryData, function (response) {
            var data = response.data;

            var xlabels = [];

            if (['daily', 'weekly', 'monthly'].includes(option)) {
                xlabels = utils.getLabels(fromDate, toDate, option);
            } else {
                console.error('Invalid interval provided');
            }
            datasets = utils.getRevenueCategory(data, xlabels, option);
            var chartData = {
                labels: xlabels,
                datasets: datasets
            };

            var revenueCategory = document.getElementById("revenueCategory");
            if (revenueCategory) {
                myRevenueCategoryChart = utils.createOrUpdateChart(myRevenueCategoryChart, revenueCategory, 'line', chartData);
            }
        });

    };

    $.fn.fetchAndPopulateRevenueItem = function (option, fromDate, toDate) {
        const url = '/report/get-revenue-item';
        const itemData = {
            'option': option,
            'fromDate': fromDate,
            'toDate': toDate,
        }
        saveOrUpdateData(url, itemData, function (response) {
            var data = response.data;

            var xlabels = [];
            if (['daily', 'weekly', 'monthly'].includes(option)) {
                xlabels = utils.getLabels(fromDate, toDate, option);
            } else {
                console.error('Invalid interval provided');
            }
            datasets = utils.getRevenueProduct(data, xlabels, option);
            var chartData = {
                labels: xlabels,
                datasets: datasets
            };

            var revenueItem = document.getElementById("revenueItem");
            if (revenueItem) {
                myRevenueItemChart = utils.createOrUpdateChart(myRevenueItemChart, revenueItem, 'line', chartData);
            }
        });

    };

    $.fn.fetchAndPopulateCategory = function (fromDate, toDate) {
        const url = '/report/get-total-sales-categories';
        const categoryData = {
            'fromDate': fromDate,
            'toDate': toDate,
        }
        saveOrUpdateData(url, categoryData, function (response) {
            var data = response.data;

            var categoryNames = [];
            var categoryPrices = [];

            data.forEach(function (item) {
                categoryNames.push(item.category_name);
                categoryPrices.push(item.total_price);
            });

            var barChartData = {
                labels: categoryNames,
                datasets: [{
                    label: 'Categories',
                    backgroundColor: 'rgba(76, 146, 255, 0.74)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    data: categoryPrices,
                }]
            };
            var categoriesChart = document.getElementById("categoriesChart");
            if (categoriesChart) {
                myCateogryChart = utils.createOrUpdateChart(myCateogryChart, categoriesChart, 'bar', barChartData);
            }
        });
    };

    $.fn.fetchAndPopulateBarChart = function (fromDate, toDate) {
        const url = '/report/get-items-qty-data';
        const itemData = {
            'fromDate': fromDate,
            'toDate': toDate,
        }
        saveOrUpdateData(url, itemData, function (response) {
            var data = response.data;

            var itemNames = [];
            var itemPrices = [];

            data.forEach(function (item) {
                itemNames.push(item.item_name);
                itemPrices.push(item.total_price);
            });

            var barChartData = {
                labels: itemNames,
                datasets: [{
                    label: 'Items',
                    backgroundColor: 'rgba(75, 192, 192, 0.8)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    data: itemPrices
                }]
            };
            var barChart = document.getElementById("barChart");
            if (barChart) {
                myBarChart = utils.createOrUpdateChart(myBarChart, barChart, 'bar', barChartData);
            }
        });
    };

    $.fn.fetchAndPopulateTotalSalesGraph = function (option, fromDate, toDate) {
        const url = '/report/get-total-sales';
        const itemData = {
            'option': option,
            'fromDate': fromDate,
            'toDate': toDate,
        };

        saveOrUpdateData(url, itemData, function (response) {
            var data = response.data;

            var xlabels = [];


            if (['daily', 'weekly', 'monthly'].includes(option)) {
                xlabels = utils.getLabels(fromDate, toDate, option);
            } else {
                console.error('Invalid interval provided');
                return;
            }
            xSaleLabel = xlabels;

            var valueFields = ['total_sales', 'total_profit'];
            var datasets = utils.getLineChartReport(valueFields, data, xlabels, option, valueFields);


            var chartData = {
                labels: xlabels,
                datasets: datasets,
            };

            var totalSales = document.getElementById("totalSales");
            myLineChart = utils.createOrUpdateChart(myLineChart, totalSales, 'line', chartData);
        });
    };

    totalSales.onclick = function (e) {
        var activePoints = myLineChart.getElementsAtEventForMode(e, 'nearest', { intersect: true }, true);

        if (activePoints.length > 0) {
            var pointedIndex = activePoints[0].index;
            var dateTime = xSaleLabel[pointedIndex];

            var fromDate;
            var toDate;
            if (dateTime.length == 3) {
                var year = $('#yearForTotalSales').val();
                var month = (pointedIndex < 9) ? "0" + (pointedIndex + 1) : "" + (pointedIndex + 1);
                var last_day = new Date(year, month, 0).getDate();
                fromDate = year + '-' + month + '-01';
                toDate = year + '-' + month + '-' + last_day;
            }
            else if (dateTime.length == 10) {
                fromDate = dateTime;
                toDate = dateTime;
            }
            else if (dateTime.length >= 14) {
                var weeklyRange = dateTime.split(' to ');
                fromDate = utils.formatDate(weeklyRange[0]);
                toDate = utils.formatDate(weeklyRange[1]);

                var year = $('#yearForTotalSales').val();
                fromDate = year + '-' + fromDate;
                toDate = year + '-' + toDate;
            }

            $('.divTotalSales').removeClass("col-xl-6").addClass("col-xl-4");

            $('.divCollapse').hide();
            $('#divBarChart').hide().fadeIn(2000);
            $('#divCategoriesChart').hide().fadeIn(2000);
            $.fn.fetchAndPopulateBarChart(fromDate, toDate);
            $.fn.fetchAndPopulateCategory(fromDate, toDate);
        }
    };

    $.fn.fetchAndPopulateTopSelling = function (fromDate, toDate) {
        var itemData = {
            'fromDate': fromDate,
            'toDate': toDate,
        };
        const url = '/report/get-top-selling';
        const tableId = 'tblTotalSales';
        utils.fetchAndPopulateTable(url, tableId, utils.createTopSellingRow, 'POST', itemData);
    };

    $.fn.fetchAndPopulateReportTable = function (date) {
        const url = '/report/get-sale-report-daily/' + date;
        const tableId = 'dailySaleReport';
        utils.fetchAndPopulateTable(url, tableId, utils.createReportTableRow, 'GET', {});
    };
    $.fn.fetchAndPopulateReportTable(date);

    $('#yearDropdownForSaleReport').change(function () {
        var date = $('#yearDropdownForSaleReport').val();
        $.fn.fetchAndPopulateReportTable(date);
    });

    $("#btnDownloadCSV").on("click", function () {

        var now = new Date();
        var dateTime = now.toISOString().slice(0, 19).replace("T", " ");
        var table = $("#tblDailySaleReport");
        var rows = table.find("tr");

        var csvContent = "Daily Sale Report\n";

        var headerRow = table.find("thead tr");
        var headerData = [];
        headerRow.find("th").each(function () {
            headerData.push($(this).text());
        });
        csvContent += headerData.join(",") + "\n";

        rows.each(function () {
            var cells = $(this).find("td");
            var rowData = [];
            cells.each(function () {
                rowData.push($(this).text());
            });
            csvContent += rowData.join(",") + "\n";
        });

        var blob = new Blob([csvContent], { type: "text/csv" });
        var link = $("<a>")
            .attr("href", window.URL.createObjectURL(blob))
            .attr("download", "daily_sale_report_" + dateTime + ".csv")
            .appendTo("body");

        link[0].click();
        link.remove();

    });

});
