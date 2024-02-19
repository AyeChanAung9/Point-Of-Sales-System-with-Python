
from tests.controller_tests.test_damage_loss_controller import TestDamageLossController
from tests.controller_tests.test_item_receive_controller import TestItemReceiveController
from tests.controller_tests.test_sale_controller import TestSaleController
from tests.test_run_function import run_test
from other.global_var import *
from database.sqlite_db import POSDatabase
from other.helper import delete_file


from tests.other_tests.test_helper import TestHelper
from tests.other_tests.test_validations import TestValidations

from tests.model_tests.test_item import TestItem
from tests.model_tests.test_category import TestCategory
from tests.model_tests.test_user import TestUser
from tests.model_tests.test_user_role import TestUserRole
from tests.model_tests.test_sale import TestSale
from tests.model_tests.test_sale_detail import TestSaleDetail
from tests.model_tests.test_damage_loss import TestDamageLoss
from tests.model_tests.test_store_configuration import TestStoreConfiguration
from tests.model_tests.test_item_receive import TestItemReceive
from tests.model_tests.test_item_receive_detail import TestItemReceiveDetail
from tests.model_tests.test_damage_loss_detail import TestDamageLossDetail
from tests.model_tests.test_search_filter import TestSearchFilter

from tests.controller_tests.test_category_controller import TestCategoryController
from tests.controller_tests.test_user_controller import TestUserController
from tests.controller_tests.test_store_configuration_controller import TestStoreConfigController
from tests.controller_tests.test_user_role_controller import TestUserRoleController
from tests.controller_tests.test_damage_loss_controller import TestDamageLossController
from tests.controller_tests.test_item_controller import TestItemController
from tests.controller_tests.test_login_controller import TestLoginController
from tests.controller_tests.test_dashboard_controller import TestDashboardController
from tests.controller_tests.test_item_receive_controller import TestItemReceiveController
from tests.controller_tests.test_sale_controller import TestSaleController
from tests.controller_tests.test_inventory_report_controller import TestInventoryReportController
from tests.controller_tests.test_sale_report_controller import TestSaleReportController
from tests.controller_tests.test_user_role_permission_controller import TestUserRolePermissionController


def run_all_tests():

    # Test others
    run_test(TestHelper, "helper functions")
    run_test(TestValidations, "validations functions")
    # -- End others --#

    # Test models
    run_test(TestItem, "item model")
    run_test(TestCategory, "category model")
    run_test(TestUser, "user model")
    run_test(TestUserRole, "user_role model")
    run_test(TestSale, "sale model")
    run_test(TestSaleDetail, "sale_detail model")
    run_test(TestDamageLoss, "damage_loss model")
    run_test(TestDamageLossDetail, "damage_loss detail model")
    run_test(TestStoreConfiguration, "store configuration model")
    run_test(TestItemReceive, "item receive model")
    run_test(TestItemReceiveDetail, "item receive detail model")
    run_test(TestSearchFilter, "search filter model")
    # -- End models --#

    # Test controllers
    run_test(TestCategoryController, "Category Controller")
    run_test(TestStoreConfigController, "Store Configuration Controller")
    run_test(TestUserController, "User Controller")
    run_test(TestUserRoleController, "User Role Controller")
    run_test(TestItemController, "Item Controller")
    run_test(TestLoginController, "Login Controller")
    run_test(TestDashboardController, "Dashboard Controller")
    run_test(TestInventoryReportController, "Inventory Report Controller")
    run_test(TestSaleReportController, "Sale Report Controller")
    run_test(TestUserRolePermissionController,
             "User Role Permission Controller")
    run_test(TestSaleController, "Sale Controller")
    run_test(TestItemReceiveController, "Item Receive Controller")
    run_test(TestDamageLossController, "Damage_Loss Controller")
    # -- End controllers --#

    # wipe out the test database

    delete_file("database/dummy.db")


if __name__ == '__main__':
    set_db_name("dummy.db")
    db = POSDatabase()
    db.setUp()
    run_all_tests()
