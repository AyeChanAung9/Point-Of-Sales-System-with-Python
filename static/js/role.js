import * as utils from './utils.js';
import { formatData } from './datatable_utils.js';

$(document).ready(function () {
    var RoleDataList;
    $('.searchLayout').removeClass("col-xl-4 col-md-4 col-sm-4").addClass("col");

    var dataTable = utils.initializeDataTable('dataTable');

    var searchKeyword = $('#search_input').val();
    var pageNo = dataTable.page.info().page + 1;


    function clearRoleForm() {
        $('#formTitle').text("Add Role");
        $('#role_id').val('');
        $('#form')[0].reset();
    }

    $.fn.fetchRoles = function (searchKeyword, pageNo) {
        const url = '/setting/get-roles';
        const data = {
            search_keyword: searchKeyword,
            page_no: pageNo,
        }
        utils.fetchData(url, 'GET', data, function (response) {
            RoleDataList = response.data;
            utils.updateDataTable(dataTable, RoleDataList, function (role, index) {
                return formatData(role, index, 'role');
            });
        });

    };

    $('#searchButton').click(function () {
        var searchKeyword = $('#search_input').val();
        var pageNo = dataTable.page.info().page + 1;
        $.fn.fetchRoles(searchKeyword, pageNo);
    });

    $.fn.fetchRoles(searchKeyword, pageNo);

    $('#resetSearchButton').click(function () {
        $('#search_input').val('');
        $.fn.fetchRoles(searchKeyword, pageNo);
    });

    $('#btnClear').click(function () {
        $('#role_id').val('');
        $('#formTitle').text("Add Role");
    });

    $('#form').submit(function (event) {
        event.preventDefault();
        var roleID = $('#role_id').val();

        var roleData = {
            role_name: $('#role_name').val(),
        };
        if (roleID) {
            roleData.role_id = roleID;
        }
        utils.saveOrUpdateData('/setting/add-edit-role', roleData,
            function (response) {
                alert(response.message);
                clearRoleForm();
                $.fn.fetchRoles(searchKeyword, pageNo);
            }
        );
    });

    $('#dataTable').on('click', '.edit-role', function (event) {
        event.preventDefault();
        var roleID = $(this).data('id');
        RoleDataList;
        var obj = $.grep(RoleDataList, function (obj) { return obj.role_id === roleID; })[0];
        utils.populateFormWithData(obj, 'formTitle', 'role_name', 'Role');
    });

    // Handle Delete role Click
    $('#dataTable').on('click', '.delete-role', function () {
        var roleID = $(this).data('id');
        utils.confirmDelete('Are you sure you want to delete this Role?', function () {
            const config = {
                url: '/setting/delete-role/' + roleID,
                successCallback: function (response) {
                    alert(response.message);
                    $.fn.fetchCategories(searchKeyword, pageNo);
                }
            };

            utils.deleteData(config.url, config.successCallback);
        });
    });

});

