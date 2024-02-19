# tables creations
# setting
user_roles_tbl = '''CREATE TABLE IF NOT EXISTS user_roles_tbl (
	role_id INTEGER PRIMARY KEY AUTOINCREMENT,
	role_name TEXT(30));'''
users_tbl = '''CREATE TABLE  IF NOT EXISTS users_tbl (
	user_id	INTEGER,
	username TEXT(50),
	password TEXT,
	role_id	INTEGER,
    UNIQUE("username"),
	CONSTRAINT users_tbl_FK FOREIGN KEY(role_id) REFERENCES user_roles_tbl(role_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	PRIMARY KEY(user_id AUTOINCREMENT));'''
user_role_permissions_tbl = '''CREATE TABLE IF NOT EXISTS user_role_permissions_tbl (
	role_id INTEGER,
    permission_name TEXT,
    UNIQUE("role_id","permission_name"),
    CONSTRAINT user_role_permissions_tbl_FK FOREIGN KEY(role_id) REFERENCES user_roles_tbl(role_id) ON DELETE RESTRICT ON UPDATE CASCADE);'''
store_config_tbl = '''CREATE TABLE IF NOT EXISTS store_config_tbl ( 
    store_name TEXT PRIMARY KEY, 
	contact_person TEXT,
    phone_no TEXT, 
	address TEXT,
	image_data BLOB);'''

# inventory
category_tbl = '''CREATE TABLE IF NOT EXISTS category_tbl ( 
    category_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    category_name TEXT)'''
item_tbl = '''CREATE TABLE IF NOT EXISTS item_tbl (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_code TEXT, 
    name TEXT, 
    price REAL, 
    reorder INTEGER, 
    category_id INTEGER, 
    cost_price REAL,
    UNIQUE("product_code"),
    CONSTRAINT item_tbl_FK FOREIGN KEY (category_id) REFERENCES category_tbl(category_id) ON DELETE RESTRICT ON UPDATE CASCADE)'''
item_receive_tbl = '''CREATE TABLE IF NOT EXISTS  item_receive_tbl (
	item_receive_id INTEGER PRIMARY KEY AUTOINCREMENT,
	voucher_no TEXT(20),
	tran_date TEXT(10),
	total_items INTEGER,
	user_id INTEGER,
	CONSTRAINT item_receive_tbl_FK FOREIGN KEY (user_id) REFERENCES users_tbl(user_id) ON DELETE RESTRICT ON UPDATE CASCADE);'''
item_receive_details_tbl = '''CREATE TABLE IF NOT EXISTS  item_receive_details_tbl (
	item_receive_details_id INTEGER PRIMARY KEY AUTOINCREMENT,
	item_receive_id INTEGER,
	item_id INTEGER,
	qty INTEGER,
	CONSTRAINT item_receive_details_tbl_FK FOREIGN KEY (item_receive_id) REFERENCES item_receive_tbl(item_receive_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT item_receive_details_tbl_FK_1 FOREIGN KEY (item_id) REFERENCES item_tbl(item_id) ON DELETE RESTRICT ON UPDATE CASCADE);'''
damage_loss_tbl = '''CREATE TABLE IF NOT EXISTS damage_loss_tbl ( 
    damage_loss_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    voucher_no TEXT, 
    tran_date DATE, 
    total_items INTEGER, 
    user_id INTEGER, 
    CONSTRAINT damage_loss_tbl_FK FOREIGN KEY (user_id) REFERENCES users_tbl(user_id) ON DELETE RESTRICT ON UPDATE CASCADE);'''
damage_loss_details_tbl = '''CREATE TABLE IF NOT EXISTS damage_loss_details_tbl ( 
    damage_loss_details_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    damage_loss_id INTEGER, 
    item_id INTEGER, 
    qty INTEGER, 
    remark TEXT, 
    CONSTRAINT damage_loss_details_tbl_FK FOREIGN KEY (damage_loss_id) REFERENCES damage_loss_tbl(damage_loss_id) ON DELETE CASCADE ON UPDATE CASCADE, 
    CONSTRAINT damage_loss_details_tbl_FK_1 FOREIGN KEY (item_id) REFERENCES item_tbl(item_id) ON DELETE RESTRICT ON UPDATE CASCADE);'''

# sales
sale_tbl = '''CREATE TABLE IF NOT EXISTS sale_tbl ( 
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    voucher_no TEXT, 
    tran_date DATE, 
    total_items INTEGER, 
    user_id INTEGER, 
    discount REAL,
    total_amount REAL,
    discount_percentage INTEGER,
    payment TEXT,
    CONSTRAINT sale_tbl_FK FOREIGN KEY (user_id) REFERENCES users_tbl(user_id) ON DELETE RESTRICT ON UPDATE CASCADE);'''
sale_details_tbl = '''CREATE TABLE IF NOT EXISTS sale_details_tbl ( 
    sale_details_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    sale_id INTEGER, 
    item_id INTEGER, 
    qty INTEGER, 
    price REAL, 
    CONSTRAINT sale_details_tbl_FK FOREIGN KEY (sale_id) REFERENCES sale_tbl(sale_id) ON DELETE CASCADE ON UPDATE CASCADE, 
    CONSTRAINT sale_details_tbl_FK_1 FOREIGN KEY (item_id) REFERENCES item_tbl(item_id) ON DELETE RESTRICT ON UPDATE CASCADE);'''
# log
log_tbl = '''CREATE TABLE IF NOT EXISTS log_tbl (
	log_id INTEGER PRIMARY KEY AUTOINCREMENT,
	related_vno TEXT,
	activity TEXT,
	user_id INTEGER,
	log_datetime TEXT DEFAULT (CURRENT_TIMESTAMP),
	CONSTRAINT log_tbl_FK FOREIGN KEY (user_id) REFERENCES users_tbl(user_id) ON DELETE RESTRICT ON UPDATE CASCADE);'''

# views creation
# inventory
view_for_item_category = '''CREATE VIEW IF NOT EXISTS view_for_item_category AS 
    SELECT item_tbl.*, category_tbl.category_name  
    FROM item_tbl  JOIN category_tbl  
    ON item_tbl.category_id = category_tbl.category_id'''
view_for_item_and_stock = '''CREATE VIEW IF NOT EXISTS view_for_item_and_stock AS
    SELECT view_for_item_category.*, view_for_stock_transaction_by_item.balance AS current_stock
    FROM view_for_item_category 
    INNER JOIN view_for_stock_transaction_by_item ON view_for_item_category.item_id  = view_for_stock_transaction_by_item.item_id;'''
view_for_item_receive_user = '''CREATE VIEW IF NOT EXISTS view_for_item_receive_user AS 
    SELECT ir.item_receive_id, ir.voucher_no, ir.tran_date, ir.total_items, ir.user_id, u.username 
    FROM item_receive_tbl ir JOIN users_tbl u 
    ON ir.user_id = u.user_id'''
view_for_item_receive_detail_item = '''CREATE VIEW IF NOT EXISTS  view_for_item_receive_detail_item AS 
    SELECT ird.item_receive_details_id, ird.item_receive_id, ird.item_id, ird.qty, i.product_code, i.name, i.price, i.cost_price, i.reorder, i.category_id, i.category_name 
    FROM item_receive_details_tbl ird JOIN view_for_item_category i 
    ON ird.item_id = i.item_id'''
view_for_damage_loss_user = '''CREATE VIEW IF NOT EXISTS view_for_damage_loss_user AS  
    SELECT damage_loss_tbl.*, users_tbl.username  
    FROM users_tbl  JOIN damage_loss_tbl  
    ON damage_loss_tbl.user_id = users_tbl.user_id'''
view_for_damage_loss_detail_item = '''CREATE VIEW IF NOT EXISTS view_for_damage_loss_detail_item  AS  
    SELECT damage_loss_details_tbl.*, item_tbl.product_code, item_tbl.name, item_tbl.price, item_tbl.cost_price, item_tbl.reorder, item_tbl.category_id, category_tbl.category_name
    FROM damage_loss_details_tbl JOIN item_tbl
    ON damage_loss_details_tbl.item_id = item_tbl.item_id 
    JOIN category_tbl ON item_tbl.category_id = category_tbl.category_id'''

# setting
view_for_user = '''CREATE VIEW IF NOT EXISTS view_for_user AS
    SELECT users_tbl.user_id,users_tbl.username,'password' password,users_tbl.role_id, user_roles_tbl.role_name
    FROM users_tbl JOIN user_roles_tbl 
    ON users_tbl.role_id = user_roles_tbl.role_id'''
view_for_sale_user = '''CREATE VIEW IF NOT EXISTS view_for_sale_user AS  
    SELECT sale_tbl.*, users_tbl.username  
    FROM users_tbl  JOIN sale_tbl  
    ON sale_tbl.user_id = users_tbl.user_id'''
view_for_sale_detail_item = '''CREATE VIEW IF NOT EXISTS view_for_sale_detail_item  AS  
    SELECT sale_details_tbl.*, item_tbl.product_code, item_tbl.name, item_tbl.price AS item_price, item_tbl.cost_price, item_tbl.reorder, item_tbl.category_id, category_tbl.category_name, sale_tbl.tran_date
    FROM sale_details_tbl  JOIN item_tbl  
    ON sale_details_tbl.item_id = item_tbl.item_id 
    JOIN category_tbl ON item_tbl.category_id = category_tbl.category_id
	JOIN sale_tbl on sale_details_tbl.sale_id = sale_tbl.sale_id;'''
view_for_item_receive_and_details = '''CREATE VIEW IF NOT EXISTS view_for_item_receive_and_details AS
    SELECT * FROM item_receive_tbl JOIN item_receive_details_tbl 
    ON item_receive_tbl.item_receive_id = item_receive_details_tbl.item_receive_id'''
view_for_damage_loss_and_details = '''CREATE VIEW IF NOT EXISTS view_for_damage_loss_and_details AS
    SELECT * FROM damage_loss_tbl JOIN damage_loss_details_tbl 
    ON damage_loss_tbl.damage_loss_id = damage_loss_details_tbl.damage_loss_id'''
view_for_sale_and_details = '''CREATE VIEW IF NOT EXISTS view_for_sale_and_details AS
    SELECT
        sale_tbl.*,
        sale_details_tbl.*,
        item_tbl.product_code,
        item_tbl.cost_price,
        item_tbl.name AS item_name,
		category_tbl.category_id,
        category_tbl.category_name,
        users_tbl.username,
		(sale_details_tbl.price -(sale_details_tbl.price*discount_percentage/100))*qty AS total_price,
        (sale_details_tbl.price - item_tbl.cost_price-(sale_details_tbl.price*discount_percentage/100))*qty AS total_profit
    FROM
        sale_tbl
    JOIN
        sale_details_tbl ON sale_tbl.sale_id = sale_details_tbl.sale_id
    JOIN
        item_tbl ON sale_details_tbl.item_id = item_tbl.item_id
    JOIN
        category_tbl ON item_tbl.category_id = category_tbl.category_id
    JOIN
        users_tbl ON sale_tbl.user_id = users_tbl.user_id;'''
view_for_transaction_date = '''CREATE VIEW IF NOT EXISTS view_for_transaction_date AS
    SELECT tran_date FROM sale_tbl GROUP BY tran_date 
    UNION
    SELECT tran_date FROM item_receive_tbl GROUP BY tran_date 
    UNION 
    SELECT tran_date FROM damage_loss_tbl GROUP BY tran_date'''
view_for_daily_stock_transaction = '''CREATE VIEW IF NOT EXISTS view_for_daily_stock_transaction AS
    SELECT view_for_transaction_date.tran_date, SUM(IFNULL(vfirad.qty, 0)) AS item_receive_total, 
    SUM(IFNULL(vfdlad.qty, 0)) AS damage_loss_total,
    SUM(IFNULL(vfsad.qty, 0)) AS sale_total,
    SUM(IFNULL(vfirad.qty, 0)) - (SUM(IFNULL(vfdlad.qty, 0)) + SUM(IFNULL(vfsad.qty, 0))) AS balance
    FROM view_for_transaction_date 
    LEFT JOIN view_for_item_receive_and_details vfirad ON view_for_transaction_date.tran_date = vfirad.tran_date
    LEFT JOIN view_for_damage_loss_and_details vfdlad ON view_for_transaction_date.tran_date = vfdlad.tran_date
    LEFT JOIN view_for_sale_and_details vfsad ON view_for_transaction_date.tran_date = vfsad.tran_date
    GROUP BY view_for_transaction_date.tran_date
    ORDER BY view_for_transaction_date.tran_date'''
view_for_stock_transaction_by_item = '''CREATE VIEW IF NOT EXISTS view_for_stock_transaction_by_item AS
    SELECT *, IIF(balance <= 0, 1, 0) AS out_of_stock, 
	IIF(balance>0 AND balance<=reorder, 1, 0) AS low_in_stock
    FROM 
    (SELECT item_tbl.item_id, SUM(IFNULL(vfirad.qty, 0)) AS item_receive_total, 
    SUM(IFNULL(vfdlad.qty, 0)) AS damage_loss_total,
    SUM(IFNULL(vfsad.qty, 0)) AS sale_total,
    CASE
        WHEN SUM(IFNULL(vfirad.qty, 0)) > (SUM(IFNULL(vfdlad.qty, 0)) + SUM(IFNULL(vfsad.qty, 0))) THEN
            SUM(IFNULL(vfirad.qty, 0)) - (SUM(IFNULL(vfdlad.qty, 0)) + SUM(IFNULL(vfsad.qty, 0))) 
        ELSE 0
    END AS balance,
    item_tbl.reorder 
    FROM item_tbl
    LEFT JOIN view_for_item_receive_and_details vfirad ON item_tbl.item_id = vfirad.item_id
    LEFT JOIN view_for_damage_loss_and_details vfdlad ON item_tbl.item_id = vfdlad.item_id
    LEFT JOIN view_for_sale_and_details vfsad ON item_tbl.item_id = vfsad.item_id
    GROUP BY item_tbl.item_id
    ORDER BY item_tbl.item_id) AS item'''
view_for_log = '''CREATE VIEW IF NOT EXISTS view_for_log AS
SELECT related_vno,log_datetime,username,CASE WHEN activity='N' THEN 'CREATED' WHEN activity='M' THEN 'MODIFIED' ELSE 'DELETED' END activity 
FROM log_tbl JOIN users_tbl ON log_tbl.user_id=users_tbl.user_id'''


# triggers creation
item_receive_after_insert_trigger = '''CREATE TRIGGER IF NOT EXISTS item_receive_after_insert
    AFTER INSERT
    ON item_receive_tbl
    BEGIN
	INSERT INTO log_tbl (related_vno, activity, user_id) VALUES (NEW.voucher_no, 'N', NEW.user_id);
    END;'''
item_receive_after_update_trigger = '''CREATE TRIGGER IF NOT EXISTS item_receive_after_update
    AFTER UPDATE
    ON item_receive_tbl
    BEGIN
	INSERT INTO log_tbl (related_vno, activity, user_id) VALUES (NEW.voucher_no, 'M', NEW.user_id);
    END;'''
item_receive_after_delete_trigger = '''CREATE TRIGGER IF NOT EXISTS item_receive_after_delete
    AFTER DELETE
    ON item_receive_tbl
    BEGIN
	INSERT INTO log_tbl (related_vno, activity, user_id) VALUES (OLD.voucher_no, 'D', OLD.user_id);
    DELETE FROM item_receive_details_tbl WHERE item_receive_id = OLD.item_receive_id;
    END;'''
damage_loss_after_insert_trigger = '''CREATE TRIGGER IF NOT EXISTS damage_loss_after_insert
    AFTER INSERT
    ON damage_loss_tbl
    BEGIN
	INSERT INTO log_tbl (related_vno, activity, user_id) VALUES (NEW.voucher_no, 'N', NEW.user_id);
    END;'''
damage_loss_after_update_trigger = '''CREATE TRIGGER IF NOT EXISTS damage_loss_after_update
    AFTER UPDATE
    ON damage_loss_tbl
    BEGIN
	INSERT INTO log_tbl (related_vno, activity, user_id) VALUES (NEW.voucher_no, 'M', NEW.user_id);
    END;'''
damage_loss_after_delete_trigger = '''CREATE TRIGGER IF NOT EXISTS damage_loss_after_delete
    AFTER DELETE
    ON damage_loss_tbl
    BEGIN
	INSERT INTO log_tbl (related_vno, activity, user_id) VALUES (OLD.voucher_no, 'D', OLD.user_id);
    DELETE FROM damage_loss_details_tbl WHERE damage_loss_id = OLD.damage_loss_id;
    END;'''
sale_after_insert_trigger = '''CREATE TRIGGER IF NOT EXISTS sale_after_insert
    AFTER INSERT
    ON sale_tbl
    BEGIN
	INSERT INTO log_tbl (related_vno, activity, user_id) VALUES (NEW.voucher_no, 'N', NEW.user_id);
    END;'''
sale_after_update_trigger = '''CREATE TRIGGER IF NOT EXISTS sale_after_update
    AFTER UPDATE
    ON sale_tbl
    BEGIN
	INSERT INTO log_tbl (related_vno, activity, user_id) VALUES (NEW.voucher_no, 'M', NEW.user_id);
    END;'''
sale_after_delete_trigger = '''CREATE TRIGGER IF NOT EXISTS sale_after_delete
    AFTER DELETE
    ON sale_tbl
    BEGIN
	INSERT INTO log_tbl (related_vno, activity, user_id) VALUES (OLD.voucher_no, 'D', OLD.user_id);
    DELETE FROM sale_details_tbl WHERE sale_id = OLD.sale_id;
    END;'''

# limit to show item list in each page
item_count_to_show = 20

# item
item_add = "INSERT INTO item_tbl (product_code, name, price, reorder, category_id, cost_price) VALUES (?, ?, ?, ?, ?, ?)"
item_delete = "DELETE FROM item_tbl WHERE item_id=?"
item_view_by_keyword = "SELECT * FROM view_for_item_and_stock WHERE (product_code LIKE ? OR name LIKE ?)"
item_view_by_category = "SELECT * FROM view_for_item_and_stock WHERE (product_code LIKE ? OR name LIKE ?) AND category_id = ?"
item_view_by_item_id = "SELECT * FROM view_for_item_and_stock WHERE item_id = ?"
item_view_by_product_code = "SELECT * FROM view_for_item_and_stock WHERE product_code = ?"
item_modify = "UPDATE item_tbl SET product_code=?, name=?, price=?, reorder=?, category_id=?, cost_price=? WHERE item_id=?"

# category
category_add = "INSERT INTO category_tbl (category_name) VALUES (?)"
category_delete = "DELETE FROM category_tbl WHERE category_id = ?"
category_view_by_keyword = "SELECT * FROM category_tbl WHERE category_name LIKE ? "
category_view_for_item_filter = "SELECT * FROM category_tbl"
category_modify = "UPDATE category_tbl SET category_name = ? WHERE category_id = ?"

# item receive
item_receive_add = "INSERT INTO item_receive_tbl (voucher_no, tran_date, total_items, user_id) VALUES (?,?,?,?)"
item_receive_modify = "UPDATE item_receive_tbl SET voucher_no = ?, tran_date = ?, total_items  = ?, user_id = ? WHERE item_receive_id = ?"
item_receive_delete = "DELETE FROM item_receive_tbl WHERE item_receive_id = ?"
item_receive_view_base = "SELECT * FROM view_for_item_receive_user WHERE voucher_no LIKE ?"
item_receive_view_where_trandate = " AND tran_date BETWEEN ? AND ? "

# item receive detail
item_receive_detail_add = "INSERT INTO item_receive_details_tbl (item_receive_id, item_id, qty) VALUES (?,?,?)"
item_receive_detail_modify = "REPLACE INTO item_receive_details_tbl (item_receive_details_id, item_receive_id, item_id, qty) VALUES (?,?,?,?)"
item_receive_detail_delete = "DELETE FROM item_receive_details_tbl WHERE item_receive_details_id = ?"
item_receive_detail_view_by_item_receive_id = "SELECT * FROM view_for_item_receive_detail_item WHERE item_receive_id= ?"

# damage / loss
damage_loss_add = "INSERT INTO damage_loss_tbl (voucher_no, tran_date, total_items, user_id) VALUES (?,?,?,?)"
damage_loss_modify = "UPDATE damage_loss_tbl SET voucher_no = ?, tran_date = ?, total_items  = ?, user_id = ? WHERE damage_loss_id = ?"
damage_loss_delete = "DELETE FROM damage_loss_tbl WHERE damage_loss_id = ?"
damage_loss_view_base = "SELECT * FROM view_for_damage_loss_user WHERE voucher_no LIKE ?"
damage_loss_view_where_trandate = " AND tran_date BETWEEN ? AND ? "

# damage / loss detail
damage_loss_detail_add = "INSERT INTO damage_loss_details_tbl (damage_loss_id, item_id, qty, remark) VALUES (?,?,?,?)"
damage_loss_detail_modify = "REPLACE INTO damage_loss_details_tbl (damage_loss_details_id, damage_loss_id, item_id, qty, remark) VALUES (?,?,?,?,?)"
damage_loss_detail_delete = "DELETE FROM damage_loss_details_tbl WHERE damage_loss_details_id = ?"
damage_loss_detail_view_by_damage_loss_id = "SELECT * FROM view_for_damage_loss_detail_item WHERE damage_loss_id= ?"

# user_role
user_role_add = "INSERT INTO user_roles_tbl (role_name) VALUES (?);"
user_role_delete = "DELETE FROM user_roles_tbl WHERE role_id = ?;"
user_role_modify = "UPDATE user_roles_tbl SET role_name = ? WHERE role_id = ?;"
user_role_view = "SELECT * FROM user_roles_tbl WHERE role_name LIKE ? "
user_role_view_for_role_filter = "SELECT * FROM user_roles_tbl"

# user
user_add = "INSERT INTO users_tbl (username, password, role_id) VALUES (?, ?, ?)"
user_delete = "DELETE FROM users_tbl WHERE user_id = ?"
user_modify = "UPDATE users_tbl SET username = ?, password = ?, role_id = ? WHERE user_id = ?"
user_view = "SELECT * FROM view_for_user"
user_view_by_id = "SELECT * FROM view_for_user WHERE user_id = ?"
user_view_by_keyword = "SELECT * FROM view_for_user WHERE (username LIKE ?)"
user_view_by_role = "SELECT * FROM view_for_user WHERE (username LIKE ?) AND role_id = ?"
user_view_by_username = "SELECT * FROM users_tbl WHERE username=?"

# user role permission
user_role_permissions_delete = "DELETE FROM user_role_permissions_tbl where role_id=?"
user_role_permissions_insert = "INSERT INTO user_role_permissions_tbl (role_id, permission_name) VALUES (?, ?)"
user_role_permissions_view_by_role_id = "SELECT permission_name FROM user_role_permissions_tbl WHERE role_id=?"
user_role_permissions_has_permission = "SELECT * FROM user_role_permissions_tbl WHERE role_id=? and permission_name=?"


# sale
sale_add = "INSERT INTO sale_tbl (voucher_no, tran_date, total_items, user_id, discount, total_amount, discount_percentage, payment) VALUES (?,?,?,?,?,?,?,?)"
sale_modify = "UPDATE sale_tbl SET voucher_no = ?, tran_date = ?, total_items  = ?, user_id = ?, discount = ?, total_amount = ?, discount_percentage = ?, payment = ? WHERE sale_id = ?"
sale_delete = "DELETE FROM sale_tbl WHERE sale_id = ?"
sale_view_base = "SELECT * FROM view_for_sale_user WHERE voucher_no LIKE ?"
sale_view_where_trandate = " AND tran_date BETWEEN ? AND ? "

# sale detail
sale_detail_add = "INSERT INTO sale_details_tbl (sale_id, item_id, qty, price) VALUES (?,?,?,?)"
sale_detail_modify = "REPLACE INTO sale_details_tbl (sale_details_id, sale_id, item_id, qty, price) VALUES (?,?,?,?,?)"
sale_detail_delete = "DELETE FROM sale_details_tbl WHERE sale_details_id = ?"
sale_detail_view_by_sale_id = "SELECT * FROM view_for_sale_detail_item WHERE sale_id= ?"

# store configuration
store_config_modify = "UPDATE store_config_tbl SET store_name=?, contact_person=?, phone_no=?, address=?, image_data=?"
store_config_view = "SELECT store_name,contact_person,phone_no,address FROM store_config_tbl"
store_config_image = "SELECT image_data FROM store_config_tbl;"

# sale report
get_top_selling_items = '''SELECT item_name, category_name, SUM(qty) AS qty, SUM(price) AS price, SUM(qty*price) AS sales 
FROM view_for_sale_and_details 
WHERE tran_date BETWEEN ? AND ? 
GROUP BY item_name, price 
ORDER BY qty DESC LIMIT 10;'''
get_total_sales_monthly = '''SELECT tran_date,
    strftime('%Y-%m', tran_date) AS month,
    SUM(total_price) AS total_sales,
    SUM(total_profit) AS total_profit
    FROM view_for_sale_and_details
    WHERE tran_date BETWEEN ? AND ?
    GROUP BY month
    ORDER BY month;'''
get_total_sales_daily = '''SELECT tran_date, 
	SUM(total_price) AS total_sales,
    SUM(total_profit) AS total_profit
    FROM view_for_sale_and_details
    WHERE tran_date BETWEEN ? AND ?
    GROUP BY tran_date
    ORDER BY tran_date;'''
get_total_sales_weekly = '''SELECT tran_date, 
	SUM(total_price) AS total_sales,
	SUM(total_profit) AS total_profit,
	strftime('%W', tran_date) AS WeekNumber,
    max(date(tran_date, 'weekday 0', '-7 day')) WeekStart,
    max(date(tran_date, 'weekday 0', '-1 day')) WeekEnd
	from view_for_sale_and_details
    WHERE tran_date BETWEEN ? AND ?
    GROUP BY WeekNumber
    ORDER BY WeekNumber;'''
get_sale_year_by_year = "SELECT strftime('%Y', tran_date) AS year FROM view_for_sale_and_details GROUP BY year ORDER BY year DESC;"
get_categories_sales_by_total_sales = '''SELECT
	strftime('%m', tran_date) AS month,
    category_name,
    SUM(total_price) AS total_price
    FROM view_for_sale_and_details
    WHERE tran_date BETWEEN ? AND ?
    GROUP BY month, category_name
    ORDER BY month, total_price DESC;'''
get_items_by_total_sales = '''SELECT
	strftime('%m', tran_date) AS month,
    item_name,
    SUM(total_price) AS total_price
    FROM view_for_sale_and_details
    WHERE tran_date BETWEEN ? AND ?
    GROUP BY month, item_name
    ORDER BY month, total_price DESC;'''
get_sale_report_by_daily = "SELECT voucher_no,item_name,category_name,qty,price*qty - total_price AS discount, price, total_price FROM view_for_sale_and_details WHERE tran_date=?"
get_qty_sold_by_category_daily = '''SELECT
    c.category_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    COALESCE(SUM(v.qty), 0) AS qty
    FROM
        category_tbl c
    LEFT JOIN
        view_for_sale_and_details v ON c.category_id = v.category_id AND v.tran_date BETWEEN ? AND ?
    GROUP BY
        c.category_id, v.tran_date
    ORDER BY
        c.category_name, v.tran_date;'''
get_qty_sold_by_category_weekly = '''SELECT
    c.category_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    COALESCE(SUM(v.qty), 0) AS qty,
    COALESCE(strftime('%W', v.tran_date),'No Sales') AS WeekNumber,
    COALESCE(max(date(v.tran_date, 'weekday 0', '-7 day')),'No Sales') AS WeekStart,
    COALESCE(max(date(v.tran_date, 'weekday 0', '-1 day')),'No Sales') AS WeekEnd
    FROM
        category_tbl c
    LEFT JOIN
        (
            SELECT
                category_id,
                tran_date,
                SUM(qty) AS qty
            FROM
                view_for_sale_and_details
            WHERE
                tran_date BETWEEN ? AND ?
            GROUP BY
                category_id, strftime('%W', tran_date)
        ) v ON c.category_id = v.category_id
    GROUP BY
        c.category_id, v.tran_date, WeekNumber
    ORDER BY
        c.category_name, WeekNumber;'''
get_qty_sold_by_category_monthly = '''SELECT
    c.category_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    strftime('%Y-%m', v.tran_date) AS year,
    COALESCE(SUM(v.qty), 0) AS qty
    FROM
        category_tbl c
    LEFT JOIN
        (
            SELECT
                category_id,
                tran_date,
                SUM(qty) AS qty
            FROM
                view_for_sale_and_details
            WHERE
                tran_date BETWEEN ? AND ?
            GROUP BY
                category_id, strftime('%Y-%m', tran_date)
        ) v ON c.category_id = v.category_id
    GROUP BY
        c.category_id, year, v.tran_date
    ORDER BY
        v.tran_date;'''
get_revenue_category_daily = '''SELECT
    c.category_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    COALESCE(SUM(v.total_price), 0) AS total_price
    FROM
        category_tbl c
    LEFT JOIN
        view_for_sale_and_details v ON c.category_id = v.category_id AND v.tran_date BETWEEN ? AND ?
    GROUP BY
        c.category_id, v.tran_date
    ORDER BY
        c.category_name, v.tran_date;'''
get_revenue_category_weekly = '''SELECT
    c.category_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    COALESCE(SUM(v.total_price), 0) AS total_price,
    COALESCE(strftime('%W', v.tran_date),'No Sales') AS WeekNumber,
    COALESCE(max(date(v.tran_date, 'weekday 0', '-7 day')),'No Sales') AS WeekStart,
    COALESCE(max(date(v.tran_date, 'weekday 0', '-1 day')),'No Sales') AS WeekEnd
    FROM
        category_tbl c
    LEFT JOIN
        (
            SELECT
                category_id,
                tran_date,
                SUM(total_price) AS total_price
            FROM
                view_for_sale_and_details
            WHERE
                tran_date BETWEEN ? AND ?
            GROUP BY
                category_id, strftime('%W', tran_date)
        ) v ON c.category_id = v.category_id
    GROUP BY
        c.category_id, v.tran_date, WeekNumber
    ORDER BY
        c.category_name, WeekNumber;'''
get_revenue_category_monthly = '''SELECT
    c.category_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    strftime('%Y-%m', v.tran_date) AS year,
    COALESCE(SUM(v.total_price), 0) AS total_price
    FROM
        category_tbl c
    LEFT JOIN
        (
            SELECT
                category_id,
                tran_date,
                SUM(total_price) AS total_price
            FROM
                view_for_sale_and_details
            WHERE
                tran_date BETWEEN ? AND ?
            GROUP BY
                category_id, strftime('%Y-%m', tran_date)
        ) v ON c.category_id = v.category_id
    GROUP BY
        c.category_id, year, v.tran_date
    ORDER BY
        v.tran_date;'''

get_qty_sold_by_item_daily = '''SELECT
    i.item_id,
    i.name AS item_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    COALESCE(SUM(v.qty), 0) AS qty
    FROM
        item_tbl i
    LEFT JOIN
        view_for_sale_and_details v ON i.item_id = v.item_id AND v.tran_date BETWEEN ? AND ?
    GROUP BY
        i.item_id, v.tran_date
    ORDER BY
        i.item_id, v.tran_date;'''

get_qty_sold_by_item_weekly = '''SELECT
    i.item_id,
    i.name AS item_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    COALESCE(SUM(v.qty), 0) AS qty,
    COALESCE(strftime('%W', v.tran_date),'No Sales') AS WeekNumber,
    COALESCE(max(date(v.tran_date, 'weekday 0', '-7 day')),'No Sales') AS WeekStart,
    COALESCE(max(date(v.tran_date, 'weekday 0', '-1 day')),'No Sales') AS WeekEnd
    FROM
        item_tbl i
    LEFT JOIN (
        SELECT
            item_id,
            tran_date,
            SUM(qty) AS qty
        FROM
            view_for_sale_and_details
        WHERE
            tran_date BETWEEN ? AND ?
        GROUP BY
            item_id, tran_date, strftime('%W', tran_date)
    ) v ON i.item_id = v.item_id
    GROUP BY
        i.item_id, i.name, v.tran_date, WeekNumber
    ORDER BY
        i.item_id, WeekNumber;'''
get_qty_sold_by_item_monthly = '''SELECT
    i.item_id,
    i.name AS item_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    strftime('%Y-%m', v.tran_date) AS year,
    COALESCE(SUM(v.qty), 0) AS qty
    FROM
        item_tbl i
    LEFT JOIN (
        SELECT
            item_id,
            tran_date,
            SUM(qty) AS qty
        FROM
            view_for_sale_and_details
        WHERE
            tran_date BETWEEN ? AND ?
        GROUP BY
            item_id, strftime('%Y-%m', tran_date)
    ) v ON i.item_id = v.item_id
    GROUP BY
        i.item_id, i.name, year
    ORDER BY
        i.item_id, year;'''

get_revenue_item_daily = '''SELECT
    i.item_id,
    i.name AS item_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    COALESCE(SUM(v.total_price), 0) AS total_price
    FROM
        item_tbl i
    LEFT JOIN
        view_for_sale_and_details v ON i.item_id = v.item_id AND v.tran_date BETWEEN ? AND ?
    GROUP BY
        i.item_id, i.name, v.tran_date
    ORDER BY
        i.item_id, v.tran_date;'''
get_revenue_item_weekly = '''SELECT
    i.item_id,
    i.name AS item_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    COALESCE(SUM(v.total_price), 0) AS total_price,
    COALESCE(strftime('%W', v.tran_date),'No Sales') AS WeekNumber,
    COALESCE(max(date(v.tran_date, 'weekday 0', '-7 day')),'No Sales') AS WeekStart,
    COALESCE(max(date(v.tran_date, 'weekday 0', '-1 day')),'No Sales') AS WeekEnd
    FROM
        item_tbl i
    LEFT JOIN (
        SELECT
            item_id,
            tran_date,
            SUM(total_price) AS total_price
        FROM
            view_for_sale_and_details
        WHERE
            tran_date BETWEEN ? AND ?
        GROUP BY
            item_id, tran_date, strftime('%W', tran_date)
    ) v ON i.item_id = v.item_id
    GROUP BY
        i.item_id, i.name, v.tran_date, WeekNumber
    ORDER BY
        i.item_id, WeekNumber;'''
get_revenue_item_monthly = '''SELECT
    i.item_id,
    i.name AS item_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    strftime('%Y-%m', v.tran_date) AS year,
    COALESCE(SUM(v.total_price), 0) AS total_price
    FROM
        item_tbl i
    LEFT JOIN (
        SELECT
            item_id,
            tran_date,
            SUM(total_price) AS total_price
        FROM
            view_for_sale_and_details
        WHERE
            tran_date BETWEEN ? AND ?
        GROUP BY
            item_id, strftime('%Y-%m', tran_date)
    ) v ON i.item_id = v.item_id
    GROUP BY
        i.item_id, i.name, year
    ORDER BY
        i.item_id, year;'''
get_sale_growth = '''SELECT
    i.item_id,
    i.name AS item_name,
    COALESCE(v.tran_date, 'No Sales') AS tran_date,
    COALESCE(v.total_price, 0) AS total_price,
    COALESCE(
        v.total_price / (
            SELECT SUM(total_price)
            FROM view_for_sale_and_details
            WHERE strftime('%Y', v.tran_date) = ?
        ) * 100,
        0
    ) AS sale_percentage
    FROM
        item_tbl i
    LEFT JOIN
        view_for_sale_and_details v ON i.item_id = v.item_id AND strftime('%Y', v.tran_date) = ?
    GROUP BY
        i.item_id, i.name
    ORDER BY
        i.item_id, v.tran_date;'''
get_quarterly_sale = '''SELECT
    i.product_code,
    i.name AS item_name,
    i.category_id,
    c.category_name,
    COALESCE((CAST(strftime('%m', d.tran_date) AS INTEGER) - 1) / 3 + 1, 'No Sales') AS quarter,
    COALESCE(strftime('%Y', d.tran_date),'No Sales') AS year,
    COALESCE(SUM(d.total_price), 0) AS total_quarterly_sales,
    COALESCE(SUM(d.total_profit), 0) AS total_quarterly_profit
    FROM
        item_tbl i
    LEFT JOIN
        view_for_sale_and_details d ON i.item_id = d.item_id AND strftime('%Y', d.tran_date) = ?
    LEFT JOIN
        category_tbl c ON i.category_id = c.category_id
    GROUP BY
        i.product_code, i.name, i.category_id, c.category_name, quarter, year
    ORDER BY
        i.product_code, quarter, year;'''


# dashboard
inventory_overview = '''SELECT 
    (SELECT IFNULL(SUM(current_stock),0) FROM view_for_item_and_stock) AS in_hand,
    (SELECT IFNULL(SUM(out_of_stock),0) FROM view_for_stock_transaction_by_item) AS out_of_stock,
    (SELECT IFNULL(SUM(low_in_stock),0) FROM view_for_stock_transaction_by_item) AS low_in_stock;'''
transaction_qty = '''SELECT sale_total sale_qty, item_receive_total item_receive_qty, damage_loss_total damage_loss_qty 
    FROM view_for_daily_stock_transaction WHERE tran_date = ?
    UNION
    SELECT 0,0,0 
    where NOT EXISTS(select * from view_for_daily_stock_transaction WHERE tran_date = ?)'''
sales_overview = '''SELECT 
    (SELECT IFNULL(SUM(total_amount),0) 
		FROM view_for_sale_and_details
		WHERE tran_date = ?) AS today_sales,
    (SELECT IFNULL(SUM(total_amount),0) 
		FROM view_for_sale_and_details
		WHERE strftime('%Y-%W', tran_date) = strftime('%Y-%W', date(?))) AS weekly_sales,
    (SELECT IFNULL(SUM(total_amount),0) 
		FROM view_for_sale_and_details
		WHERE strftime('%Y-%m', tran_date) = strftime('%Y-%m', date(?))) AS monthly_sales,
    (SELECT IFNULL(SUM(total_amount),0)
		FROM view_for_sale_and_details
		WHERE strftime('%Y', tran_date) = strftime('%Y', date(?)))  AS yearly_sales;'''

# inventory report
get_stock_info_by_year = "SELECT * FROM (SELECT COUNT(*) AS total_products FROM item_tbl) AS Total_Products CROSS JOIN (SELECT COUNT(*) AS total_categories FROM category_tbl) AS Total_Categories CROSS JOIN (SELECT SUM(low_in_stock) AS low_in_stock, SUM(out_of_stock) AS out_of_stock, SUM(balance) AS instock FROM view_for_stock_transaction_by_item) AS Stock CROSS JOIN (SELECT IFNULL(SUM(item_receive_total), 0) AS item_receive_total, IFNULL(SUM(damage_loss_total), 0) AS damage_loss_total, IFNULL(SUM(sale_total), 0) AS sale_total FROM view_for_daily_stock_transaction WHERE strftime('%Y', tran_date) = ? ) AS Total"
get_stock_transactions_by_year = '''SELECT strftime('%m', tran_date) trans_month,SUM(vfdst.item_receive_total) AS item_receive_total,SUM(vfdst.sale_total) AS sale_total,SUM(vfdst.damage_loss_total) AS damage_loss_total FROM view_for_daily_stock_transaction vfdst 
WHERE strftime('%Y', tran_date) = ? GROUP BY strftime('%Y%m', tran_date) ORDER BY strftime('%Y%m', tran_date) 
'''
