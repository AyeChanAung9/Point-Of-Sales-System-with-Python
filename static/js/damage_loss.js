import * as utils from './utils.js';
import { formatData } from './datatable_utils.js';

$(document).ready(function () {
    var dataTable = utils.initializeDataTable('dataTable');
    var dataDetailTable = utils.initializeDataTable('dataDetailTable');
    var searchKeyword = $('#search_input').val();
    var fromDate = $('.fromDate').val();
    var toDate = $('.toDate').val();
    var pageNo = dataTable.page.info().page + 1;

    $.fn.fetchItems = function (searchKeyword, fromDate, toDate, pageNo) {
        const url = '/inventory/get-damage-loss';
        const data = {
            search_keyword: searchKeyword,
            from_tran_date: fromDate,
            to_tran_date: toDate,
            page_no: pageNo
        }
        utils.fetchData(url, 'GET', data, function (response) {
            utils.updateDataTable(dataTable, response.data, function (damage_loss, index) {
                return formatData(damage_loss, index, 'damage_loss');
            });
        });
    }

    $('#searchButton').click(function () {
        var searchKeyword = $('#search_input').val();
        var fromDate = $('#from').val();
        var toDate = $('#to').val();
        var pageNo = dataTable.page.info().page + 1;
        if (fromDate != '' && toDate == '') {
            alert('ToDate cannot be blank!');
            $('.toDate').focus();
        }
        $.fn.fetchItems(searchKeyword, fromDate, toDate, pageNo);
    });

    $.fn.fetchItems(searchKeyword, fromDate, toDate, pageNo);

    $('#resetSearchButton').click(function () {
        $('#search_input').val('');
        $('#from').val('');
        $('#to').val('');
        $.fn.fetchItems(searchKeyword, fromDate, toDate, pageNo);
    });

    $('#dataTable').on('click', '.view-item', function (event) {
        event.preventDefault();
        var damageId = $(this).data('id');
        var voucherId = $(this).data('voucher-id');
        const url = '/inventory/get-damage-loss-details/' + damageId;
        utils.fetchData(url, 'GET', null, function (response) {

            $('.detail_voucher_no').text("- " + voucherId);
            utils.updateDataTable(dataDetailTable, response.data, function (damage_loss, index) {
                return formatData(damage_loss, index, 'damage_loss_detail');
            });
        });

    });

    $('#dataTable').on('click', '.delete-item', function (event) {
        event.preventDefault();
        var damageId = $(this).data('id');
        utils.confirmDelete('Are you sure you want to delete this item?', function () {
            const config = {
                url: '/inventory/delete-damage-loss/' + damageId,
                successCallback: function (response) {
                    alert(response.message);
                    $.fn.fetchItems(searchKeyword, fromDate, toDate, pageNo);
                }
            };

            utils.deleteData(config.url, config.successCallback);
        });
    });

});