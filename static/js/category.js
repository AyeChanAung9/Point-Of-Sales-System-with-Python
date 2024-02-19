import * as utils from './utils.js';
import { formatData } from './datatable_utils.js';

$(document).ready(function () {
    var CategoryDataList;

    $('.searchLayout').removeClass("col-xl-4 col-md-4 col-sm-4").addClass("col");

    var dataTable = utils.initializeDataTable('dataTable');

    var searchKeyword = $('#search_input').val();
    var pageNo = dataTable.page.info().page + 1;

    function clearCategoryForm() {
        $('#formTitle').text("Add Category");
        $('#category_id').val('');
        $('#form')[0].reset();
    }

    $.fn.fetchCategories = function (searchKeyword, pageNo) {
        const url = '/inventory/get-categories';
        const data = {
            search_keyword: searchKeyword,
            page_no: pageNo,
        };

        utils.fetchData(url, 'GET', data, function (response) {
            CategoryDataList = response.data;
            utils.updateDataTable(dataTable, CategoryDataList, function (category, index) {
                return formatData(category, index, 'category');
            });
        });
    };


    $('#searchButton').click(function () {
        var searchKeyword = $('#search_input').val();
        var pageNo = dataTable.page.info().page + 1;
        $.fn.fetchCategories(searchKeyword, pageNo);
    });

    $.fn.fetchCategories(searchKeyword, pageNo);

    $('#resetSearchButton').click(function () {
        $('#search_input').val('');  // Clear the search input
        $.fn.fetchCategories(searchKeyword, pageNo);
    });

    $('#btnClear').click(function () {
        $('#category_id').val('');
        $('#formTitle').text("Add Category");
    });

    $('#form').submit(function (event) {
        event.preventDefault();
        var categoryID = $('#category_id').val();
        var categoryData = {
            category_name: $('#category_name').val(),
        };
        if (categoryID) {
            categoryData.category_id = categoryID;
        }

        utils.saveOrUpdateData('/inventory/add-edit-category', categoryData,
            function (response) {
                console.log(response);
                alert(response.message);
                clearCategoryForm();
                $.fn.fetchCategories(searchKeyword, pageNo);
            }
        );
    });


    // Handle Edit Item Click
    $('#dataTable').on('click', '.edit-category', function (event) {
        event.preventDefault();
        var categoryID = $(this).data('id');
        CategoryDataList;
        var obj = $.grep(CategoryDataList, function (obj) { return obj.category_id === categoryID; })[0];
        utils.populateFormWithData(obj, 'formTitle', 'category_name', 'Category');
    });

    // Handle Delete Item Click
    $('#dataTable').on('click', '.delete-category', function () {
        var categoryID = $(this).data('id');
        utils.confirmDelete('Are you sure you want to delete this category?', function () {
            const config = {
                url: '/inventory/delete-category/' + categoryID,
                successCallback: function (response) {
                    console.log(response);
                    alert(response.message);
                    $.fn.fetchCategories(searchKeyword, pageNo);
                }
            };

            utils.deleteData(config.url, config.successCallback);
        });
    });

});
