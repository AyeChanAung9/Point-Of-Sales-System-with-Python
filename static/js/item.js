import * as utils from './utils.js';
import { formatData } from './datatable_utils.js';

$(document).ready(function () {
    var itemDataList;

    $('.searchLayout').removeClass("col-xl-4 col-md-4").addClass("col-lg-4 col-sm-4");

    var dataTable = utils.initializeDataTable('dataTable');

    var searchKeyword = $('#search_input').val();
    var filterId = $('#categoryFilter').val();
    var pageNo = dataTable.page.info().page + 1;

    function clearItemForm() {
        $('#formTitle').text("Add Item");
        $('#item_id').val('');
        $('#form')[0].reset();
    }

    $.fn.fetchItems = function (searchKeyword, filterId, pageNo) {
        const url = '/inventory/get-items';
        const data = {
            search_keyword: searchKeyword,
            filter_id: filterId,
            page_no: pageNo,
        };

        utils.fetchData(url, 'GET', data, function (response) {
            itemDataList = response.data;
            utils.updateDataTable(dataTable, itemDataList, function (item, index) {
                return formatData(item, index, 'item');
            });
        });
    };

    $('#categoryFilter').change(function () {
        var searchKeyword = $('#search_input').val();
        var pageNo = dataTable.page.info().page + 1;
        var selectedCategoryId = $(this).val();
        $.fn.fetchItems(searchKeyword, selectedCategoryId, pageNo);
    });

    $('#searchButton').click(function () {
        var searchKeyword = $('#search_input').val();
        var filterId = $('#categoryFilter').val();
        var pageNo = dataTable.page.info().page + 1;
        $.fn.fetchItems(searchKeyword, filterId, pageNo);
    });

    $.fn.fetchItems(searchKeyword, filterId, pageNo);

    $('#resetSearchButton').click(function () {
        $('#search_input').val('');
        $('#categoryFilter').val('');
        $.fn.fetchItems(searchKeyword, filterId, pageNo);
    });

    $('#btnClear').click(function () {
        $('#item_id').val('');
        $('#formTitle').text("Add Item");
    });

    $('#form').submit(function (event) {
        event.preventDefault();
        var itemID = $('#item_id').val();
        var itemData = {
            name: $('#name').val(),
            product_code: $('#product_code').val(),
            cost_price: $('#cost_price').val(),
            price: $('#price').val(),
            reorder: $('#reorder').val(),
            category_id: $('#category_id').val(),
            category_name_can_empty: "true"
        };

        if (itemID) {
            itemData.item_id = itemID;
        }

        utils.saveOrUpdateData('/inventory/add-edit-item', itemData,
            function (response) {
                console.log(response);
                alert(response.message);
                clearItemForm();
                $.fn.fetchItems(searchKeyword, filterId, pageNo);
            }
        );
    });


    $('#dataTable').on('click', '.edit-item', function (event) {
        event.preventDefault();
        var itemId = $(this).data('id');
        itemDataList;
        var obj = $.grep(itemDataList, function (obj) { return obj.item_id === itemId; })[0];
        utils.populateFormWithData(obj, 'formTitle', 'name', 'Item');
    });

    $('#dataTable').on('click', '.delete-item', function () {
        var itemId = $(this).data('id');
        utils.confirmDelete('Are you sure you want to delete this item?', function () {
            const config = {
                url: '/inventory/delete-item/' + itemId,
                successCallback: function (response) {
                    console.log(response);
                    alert(response.message);
                    $.fn.fetchItems(searchKeyword, filterId, pageNo);
                }
            };

            utils.deleteData(config.url, config.successCallback);
        });
    });

});
