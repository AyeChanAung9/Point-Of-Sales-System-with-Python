import * as utils from './utils.js';
import { formatData } from './datatable_utils.js';

$(document).ready(function () {
    var UserDataList;
    $('.searchLayout').removeClass("col-xl-4 col-md-4").addClass("col-lg-4 col-sm-4");
    var dataTable = utils.initializeDataTable('dataTable');

    var searchKeyword = $('#search_input').val();
    var filterId = $('#roleFilter').val();
    var pageNo = dataTable.page.info().page + 1;


    function clearUserForm() {
        $('#formTitle').text("Add User");
        $('#user_id').val('');
        $('#form')[0].reset();
    }

    $.fn.fetchUsers = function (searchKeyword, filterId, pageNo) {
        const url = '/setting/get-users';
        const data = {
            search_keyword: searchKeyword,
            filter_id: filterId,
            page_no: pageNo,
        };
        utils.fetchData(url, 'GET', data, function (response) {
            UserDataList = response.data;
            utils.updateDataTable(dataTable, UserDataList, function (user, index) {
                return formatData(user, index, 'user');
            });
        });

    };

    $('#roleFilter').change(function () {
        var searchKeyword = $('#search_input').val();
        var pageNo = dataTable.page.info().page + 1;
        var selectedRoleId = $(this).val();
        $.fn.fetchUsers(searchKeyword, selectedRoleId, pageNo);
    });

    $('#searchButton').click(function () {
        var searchKeyword = $('#search_input').val();
        var filterId = $('#roleFilter').val();
        var pageNo = dataTable.page.info().page + 1;
        $.fn.fetchUsers(searchKeyword, filterId, pageNo);
    });

    $.fn.fetchUsers(searchKeyword, filterId, pageNo);

    $('#resetSearchButton').click(function () {
        $('#search_input').val('');
        $('#roleFilter').val('');
        $.fn.fetchUsers(searchKeyword, filterId, pageNo);
    });

    $('#btnClear').click(function () {
        $('#user_id').val('');
        $('#formTitle').text("Add User");
    });

    $('#form').submit(function (event) {
        event.preventDefault();
        var userID = $('#user_id').val();
        var userData = {
            username: $('#username').val(),
            password: $('#password').val(),
            role_id: $('#role_id').val(),
            role_name_can_empty: "true"
        };

        if (userID) {
            userData.user_id = userID
        }

        utils.saveOrUpdateData('/setting/add-edit-user', userData,
            function (response) {
                alert(response.message);
                clearUserForm();
                $.fn.fetchItems(searchKeyword, filterId, pageNo);
            }
        );
    });

    $('#dataTable').on('click', '.edit-user', function (event) {
        event.preventDefault();
        var userID = $(this).data('id');
        UserDataList;
        var obj = $.grep(UserDataList, function (obj) { return obj.user_id === userID; })[0];
        utils.populateFormWithData(obj, 'formTitle', 'username', 'User');
    });

    $('#dataTable').on('click', '.delete-user', function () {
        var userID = $(this).data('id');
        utils.confirmDelete('Are you sure you want to delete this User?', function () {
            const config = {
                url: '/setting/delete-user/' + userID,
                successCallback: function (response) {
                    alert(response.message);
                    $.fn.fetchItems(searchKeyword, filterId, pageNo);
                }
            };

            utils.deleteData(config.url, config.successCallback);
        });
    });

});

