
# User guide

The purpose of this guide is to **show you easy-to-understand instructions on how to use our product**.

## Table of Contents

1. [Introduction](#1-introduction)
2. [Quick Start](#2-quick-start)
3. [Features](#3-features)
    - [User Authentication Features](#user-authentication-features)
    - [Item Features](#item-features)
    - [Category Features](#category-features)
    - [Item Receive Features](#item-receive-features)
    - [Damage Loss Features](#damage-loss-features)
    - [Sale Features](#sale-features)
    - [User Features](#user-features)
    - [User Role Features](#user-role-features)
    - [User Role Permission Features](#user-role-permission-features)
    - [Store Configuration Features](#store-configuration-features)
4. [FAQ](#4-faq)
5. [Summary of Features](#5-summary-of-features)


## 1. Introduction
Point of Sale also known as POS is a Graphical User Interface (GUI) web application to manage your inventory. If you are a store owner, you will need a POS system for better management. The system provide for keeping the track record of inventory and the number of sales made per day. This POS system is suitable for convenience store or mini mart.

###### [Back to table of contents](#table-of-contents)

## 2. Quick Start
Start by installing the `necessities` by running the following commands.    

Install `Python`  
Download [python installer](https://www.python.org/downloads/) and install python


Install `flask`, `flask-bcrypt` and `python-dotenv`
```bash
pip install flask
pip install flask-bcrypt
pip install python-dotenv
```

Install `sqlite3`
```bash
sudo apt-get install sqlite3
```

After installation, create the `.env` file in the project repository and copy the follwing `key` to the .env file.

```
SECRET_KEY=360043a10710cc31d886305e505577f2
```

###### [Back to table of contents](#table-of-contents)

## 3. Features
### User Authentication Features
The user authentication feature ensures the validity of user credentials before granting access to the application. This process serves as a security measure to authenticate and authorize users.

**User Authentication Table of Contents**
* [Check User Validity](#check-user-validity)

### Check User Validity

| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
| `username` | The username of the user.  | Any input that is not empty and has less than 30 characters. It can be only characters.  |
| `password`     | The password of the user. | Password cannot be null and must be between 3 and 15 characters long. |

**Error Messages**
![User Auth Error Message](./images/UserAuthErrorMessage.png)

###### [Back to table of contents](#table-of-contents)


### Item Features
Before you start managing your items within the application, it's essential to understand the key features that allow you to add, modify, delete and view items effectively.

**Item Table of Contents**
* [Add or Modify Item](#add-or-modify-item) 
* [Delete Item](#delete-item) 
* [View Items](#view-items)

### Add or Modify Item
This feature enables you to add a new item to your inventory or modify an existing one based on the provided input dictionary.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
| `item_id` | Identifier for the item.	  | If modifying, should be an integer representing the unique item's ID. If adding, leave empty or use a non-existent ID.  |
| `product_code` | Product code of the item.  | Should not be empty, and its length should be less than 10 characters.  |
| `name` | Name of the item.| Should not be empty, and its length should be less than 30 characters. |
| `price` | Price of the item. | Should be a valid price value. |
| `reorder` | Re-order limit for the item. | Should be a valid number.|
| `category_id` | Identifier for the item's category.	 | Should be an integer representing the unique category's ID.|
| `cost_price` | Cost price of the item. | Should be a valid price value. |


### Delete Item
Use this feature to remove an item from your inventory based on its unique identifier (ID).
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
| `item_id` | Identifier for the item to delete	  | Should be an integer representing the unique item's ID. |

### View Items
Retrieve a list of items based on specified parameters, allowing you to view and manage your inventory efficiently.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`page_no`|	Page number for pagination.| Should be an integer greater than or equal to 1.|
|`search_keyword`|	Keyword for searching items.| Any input.|
|`filter_id`| Identifier for additional filtering.|	No specific restrictions mentioned in the provided code.|
|`from_tran_date`|	Starting transaction date for filtering results.| Should be a valid transaction date or an empty string.|
|`to_tran_date`| Ending transaction date for filtering results.| Should be a valid transaction date or an empty string.|

###### [Back to table of contents](#table-of-contents)


### Category Features
Adds a new category or modifies an existing one based on input dictionary.

**Category Table of Contents**
* [Add or Modify Category](#add-or-modify-category) 
* [Delete Category](#delete-category) 
* [View Categories](#view-categories)

### Add or Modify Category
This feature enables you to add a new category to your inventory or modify an existing one based on the provided input dictionary.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`category_id`|	Identifier for the category.|	If modifying, should be an integer representing the unique category's ID. If adding, leave empty or use a non-existent ID.|
|`category_name`|	Name of the category.|	Should not be empty, and its length should be less than 30 characters.|

### Delete Category
Use this feature to remove a category from your inventory based on its unique identifier (ID).
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
| `category_id` | Identifier for the category to delete.  | Should be an integer representing the unique category's ID. |

### View Categories
Retrieve a list of items based on specified parameters, allowing you to view and manage your inventory efficiently.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`page_no`|	Page number for pagination.| Should be an integer greater than or equal to 1.|
|`search_keyword`|	Keyword for searching items.| Any input.|
|`filter_id`| Identifier for additional filtering.|	No specific restrictions mentioned in the provided code.|
|`from_tran_date`|	Starting transaction date for filtering results.| Should be a valid transaction date or an empty string.|
|`to_tran_date`| Ending transaction date for filtering results.| Should be a valid transaction date or an empty string.|

###### [Back to table of contents](#table-of-contents)


### Item Receive Features
There are various features built into the Item Receive functionality, providing the ability to manage received items efficiently.

**Item Receive Table of Contents**
* [Add Item Receive](#add-item-receive) 
* [Modify Item Receive](#modify-item-receive)
* [Delete Item Receive](#delete-item-receive) 
* [View Item Receive](#view-item-receive)
* [View Item Receive Details](#view-item-receive-details)

### Add Item Receive
This feature enables you to add a new item receive entry along with details.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`voucher_no`|	Voucher number associated with the transaction.	| Should not be empty and its length should be less than 25 characters.|
|`tran_date`|	Date when the items were received.|	Should be a valid date in the format YYYY-MM-DD.|
|`total_items`|	Total number of items received in the entry.|	Should be a valid number representing the total items received.|
|`user_id`|	Identifier for the user initiating the entry.|	Should be an integer representing the unique user's ID.|
|`details`|	List of item receive details.|	Should be a list of dictionaries containing details of each received item.|

### Modify Item Receive Features
This feature enables you to modify an existing item receive entry along with details.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`item_receive_id	`|	Identifier for the item receive entry.	|	 Should be an integer representing the unique item receive entry's ID. |
|`voucher_no`|	Voucher number associated with the transaction.	| Should not be empty and its length should be less than 25 characters.|
|`tran_date`|	Date when the items were received.|	Should be a valid date in the format YYYY-MM-DD.|
|`total_items`|	Total number of items received in the entry.|	Should be a valid number representing the total items received.|
|`user_id`|	Identifier for the user initiating the entry.|	Should be an integer representing the unique user's ID.|
|`details`|	List of item receive details.|	Should be a list of dictionaries containing details of each received item.|

### Delete Item Receive
Use this feature to remove an item receive entry from your records based on its unique identifier (ID).
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`item_receive_id`|	Identifier for the item receive entry.|	Should be an integer representing the unique item receive entry's ID.|

### View Item Receive
Retrieve a list of item receive entries based on specified parameters, allowing you to view and manage your item receive records efficiently.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`page_no`|	Page number for pagination.| Should be an integer greater than or equal to 1.|
|`search_keyword`|	Keyword for searching items.| Any input.|
|`filter_id`| Identifier for additional filtering.|	No specific restrictions mentioned in the provided code.|
|`from_tran_date`|	Starting transaction date for filtering results.| Should be a valid transaction date or an empty string.|
|`to_tran_date`| Ending transaction date for filtering results.| Should be a valid transaction date or an empty string.|

### View Item Receive Details
Retrieve detailed information about a specific item receive entry based on its unique identifier (ID).
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`item_receive_id`|	Identifier for the item receive entry.|	Should be an integer representing the unique item receive entry's ID.|

###### [Back to table of contents](#table-of-contents)


### Damage Loss Features
Damage loss features allow you to manage and track items that have been damaged or lost.

**Damage Loss Table of Contents**
* [Add Damage Loss](#add-damage_loss) 
* [Modify Damage Loss](#modify-damage_loss)
* [Delete Damage Loss](#delete-damage_loss) 
* [View Damage Loss](#view-damage_loss)
* [View Damage Loss Details](#view-damage_loss-details)

### Add Damage Loss
This feature allows you to add a new damage loss entry to your records.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`voucher_no`|	Voucher number for the damage loss.|	Should not be empty and its length should be less than 25 characters.|
|`tran_date`|	Date when the damage loss occurred.|	Should be a valid date in the format YYYY-MM-DD.|
|`total_items`|	Total number of items in the sale.|	Should be a valid number.|
|`user_id`|	User ID associated with the damage loss.|	Should be an integer representing the unique user's ID.|
|`details`|	List of damage loss details.|	Should be a list of dictionaries containing details of each damage loss.|

### Modify Damage Loss
This feature allows you to modify an existing damage loss entry based on the provided input dictionary.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`damage_loss_id`|	Identifier for the damage loss entry.	|	Should be an integer representing the unique damage loss entry's ID.|
|`voucher_no`|	Voucher number for the damage loss.|	Should not be empty and its length should be less than 25 characters.|
|`tran_date`|	Date when the damage loss occurred.|	Should be a valid date in the format YYYY-MM-DD.|
|`total_items`|	Total number of items in the sale.|	Should be a valid number.|
|`user_id`|	User ID associated with the damage loss.|	Should be an integer representing the unique user's ID.|
|`details`|	List of damage loss details.|	Should be a list of dictionaries containing details of each damage loss.|

### Delete Damage Loss
Use this feature to remove a damage loss entry from your records based on its unique identifier (ID).
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`damage_loss_id`|	Identifier for the damage loss entry.	|	Should be an integer representing the unique damage loss entry's ID.|

### View Damage Loss
Retrieve a list of damage loss entries based on specified parameters, allowing you to view and manage damage loss records efficiently.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`page_no`|	Page number for pagination.| Should be an integer greater than or equal to 1.|
|`search_keyword`|	Keyword for searching items.| Any input.|
|`filter_id`| Identifier for additional filtering.|	No specific restrictions mentioned in the provided code.|
|`from_tran_date`|	Starting transaction date for filtering results.| Should be a valid transaction date or an empty string.|
|`to_tran_date`| Ending transaction date for filtering results.| Should be a valid transaction date or an empty string.|

### View Damage Loss Details
Retrieve detailed information about a specific damage loss entry based on its unique identifier (ID).
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`damage_loss_id`|	Identifier for the damage loss entry.	|	Should be an integer representing the unique damage loss entry's ID.|

###### [Back to table of contents](#table-of-contents)

### Sale Features
The sale feature involves recording transactions where items are sold. This section provides an overview of the different functionalities related to sales.

**Sale Table of Contents**
* [Add Sale](#add-sale) 
* [Modify Sale](#modify-sale)
* [Delete Sale](#delete-sale) 
* [View Sale](#view-sale)
* [View Sale Details](#view-sale-details)

| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`voucher_no`|	Voucher number for the sale.|	Should not be empty and its length should be less than 25 characters.|
|`tran_date`|	Date when the sale occurred.|	Should be a valid date in the format YYYY-MM-DD.|
|`total_items`|	Total number of items sold in the sale.|	Should be a valid number.|
|`user_id`|	User ID associated with the sale.|	Should be an integer representing the unique user's ID.|
|`discount`|	Discount applied to the sale.|	Should be a valid number.|
|`total_amount`|	Total amount of the sale.|	Should be a valid number.|
|`discount_percentage`|	Discount percentage applied to the sale.|	Should be a valid percentage value.|
|`payment`|	Payment method used for the sale.|	Should be one of the following options: 'crdp'- (Card Payment), 'cshp' - (Cash Payment), 'dgtp' - (Digital Payment).|
|`details`|	List of sale details.|	Should be a list of dictionaries containing details of each sale.|

### Modify Sale
This feature allows you to modify an existing sale entry based on the provided input dictionary.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`sale_id`|	Identifier for the sale entry.	|	Should be an integer representing the unique sale entry's ID.|
|`voucher_no`|	Voucher number for the sale.|	Should not be empty and its length should be less than 25 characters.|
|`tran_date`|	Date when the sale occurred.|	Should be a valid date in the format YYYY-MM-DD.|
|`total_items`|	Total number of items sold in the sale.|	Should be a valid number.|
|`user_id`|	User ID associated with the sale.|	Should be an integer representing the unique user's ID.|
|`discount`|	Discount applied to the sale.|	Should be a valid number.|
|`total_amount`|	Total amount of the sale.|	Should be a valid number.|
|`discount_percentage`|	Discount percentage applied to the sale.|	Should be a valid percentage value.|
|`payment`|	Payment method used for the sale.|	Should be one of the following options: 'crdp'- (Card Payment), 'cshp' - (Cash Payment), 'dgtp' - (Digital Payment).|
|`details`|	List of sale details.|	Should be a list of dictionaries containing details of each sale.|

### Delete Sale
Use this feature to remove a sale entry from your records based on its unique identifier (ID).
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`sale_id`|	Identifier for the sale entry.	|	Should be an integer representing the unique sale entry's ID.|

### View Sale
Retrieve a list of sale entries based on specified parameters, allowing you to view and manage your sales efficiently.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`page_no`|	Page number for pagination.| Should be an integer greater than or equal to 1.|
|`search_keyword`|	Keyword for searching items.| Any input.|
|`filter_id`| Identifier for additional filtering.|	No specific restrictions mentioned in the provided code.|
|`from_tran_date`|	Starting transaction date for filtering results.| Should be a valid transaction date or an empty string.|
|`to_tran_date`| Ending transaction date for filtering results.| Should be a valid transaction date or an empty string.|

### View Sale Details
Retrieve detailed information about a specific sale entry based on its unique identifier (ID).
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`sale_id`|	Identifier for the sale entry.	|	Should be an integer representing the unique sale entry's ID.|

###### [Back to table of contents](#table-of-contents)

### User Features
**User Table of Contents**
* [Add or Modify User](#add-or-modify-user) 
* [Delete User](#delete-user)
* [View Users](#view-users)

### Add or Modify User
This feature allows you to add a new user or modify an existing one based on the input dictionary.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`user_id`|	Identifier for the user.|	If modifying, should be an integer representing the unique user's ID. If adding, leave empty or use a non-existent ID.|
|`username`|	User's username.|	Any input that is not empty and has less than 25 characters. It can only contain characters.|
|`password`|	User's password.|	Password must be at least 5 characters long.|
|`role_id`|	Identifier for the user's role.|	Should be an integer representing a valid user role ID.|

### Delete User
Use this feature to delete a user based on their ID.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`user_id`|	Identifier for the user.|	Should be an integer representing the unique user's ID|

### View Users
Retrieve a list of users based on specified parameters.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`page_no`|	Page number for pagination.| Should be an integer greater than or equal to 1.|
|`search_keyword`|	Keyword for searching items.| Any input.|
|`filter_id`| Identifier for additional filtering.|	No specific restrictions mentioned in the provided code.|
|`from_tran_date`|	Starting transaction date for filtering results.| Should be a valid transaction date or an empty string.|
|`to_tran_date`| Ending transaction date for filtering results.| Should be a valid transaction date or an empty string.|

###### [Back to table of contents](#table-of-contents)

### User Role Features
**User Role Table of Contents**
* [Add or Modify User Role](#add-or-modify-user-role)
* [Delete User Role](#delete-user-role) 
* [View User Roles](#view-user-roles)

### Add or Modify User Role
Adds a new user role or modifies an existing one based on input dictionary
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`role_id`|	Identifier for the user role.|	If modifying, should be an integer representing the unique user role's ID. If adding, leave empty or use a non-existent ID.|
|`role_name`|	Name of the user role.| It should not be empty and has less than 25 characters.|

### Delete User Role
Deletes a user role based on their ID
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`role_id`|	Identifier for the user role.|	Should be an integer representing the unique user role's ID.|


### View User Roles
Retrieves a list of user roles based on specified parameters
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`page_no`|	Page number for pagination.| Should be an integer greater than or equal to 1.|
|`search_keyword`|	Keyword for searching items.| Any input.|
|`filter_id`| Identifier for additional filtering.|	No specific restrictions mentioned in the provided code.|
|`from_tran_date`|	Starting transaction date for filtering results.| Should be a valid transaction date or an empty string.|
|`to_tran_date`| Ending transaction date for filtering results.| Should be a valid transaction date or an empty string.|

###### [Back to table of contents](#table-of-contents)

### User Role Permission Features
**User Role Permission Table of Contents**
* [Modify Permissions](#modify-permissions)
* [Check Permission](#check-permission)

### Modify Permissions
This feature allows you to modify permissions for a specific user role.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`role_id`|	Identifier for the user role.|	Should be an integer representing the unique user role's ID.|
|`permissions`|	List of permissions to modify.|	Should be a list of strings representing the permissions to be modified for the user role.|

### Check Permission
Use this feature to check if a user role has a specific permission.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`role_id`|	Identifier for the user role.|	Should be an integer representing the unique user role's ID.|
|`permissions`|	List of permissions to modify.|	Should be a list of strings representing the permissions to be modified for the user role.|

###### [Back to table of contents](#table-of-contents)

### Store Configuration Features

**Store Configuration Table of Contents**
* [Modify Store Configuration](#modify-store-configuration) 

### Modify Store Configuration
This feature enables you to modify the configuration settings for the store.
| Option      | Description            | Restrictions           |
|-------------|------------------------|------------------------|
|`store_name`|	Name of the store.|	Should not be empty, and its length should be less than 50 characters.|
|`contact_person`|	Contact person for the store.|	Any input is accepted.|
|`phone_no`|	Phone number for the store.|	Should not be empty, and it must be a valid phone number.|
|`address`|	Address of the store.|	Should not be empty, and its length should be less than 255 characters.|
|`image_data`|	Image data for the store.|	Any binary image data is accepted.|


###### [Back to table of contents](#table-of-contents)

## 4. FAQ
Q: Can I delete a category ?

A: You can delete a category if and only if there are no items related to that category. You cannot delete a category which has items related to it.

Q: Can I add new items without creating category ?

A: You can add new items to existing category. If you want to add new items to non-existing category, you must first create a category you desired.

Q: Can this POS system be used in multiple stores ?

A: We don't suggest to use this POS system in multiple stores. The reason is because of the data, the system will show the same data across the multiple stores which is irrelevant.

###### [Back to table of contents](#table-of-contents)

## 5. Summary of Features
There are several features built into the application, each categorized for clarity. More details can be found in their respective sections.

| Name                                             | Description                                                            |
|--------------------------------------------------|------------------------------------------------------------------------|
| [**User Authentication Features**](#user-authentication-features)| |
| [Check User Validity](#check-user-validity)| Validates user credentials based on input dictionary |
| [**Item Features**](#item-features)||
| [Add or Modify Item](#add-or-modify-item) | dds a new item or modifies an existing one based on input dictionary|
| [Delete Item](#delete-item)| Deletes an item based on its ID|
| [View Items](#view-items)| Retrieves a list of items based on specified parameters|
| [**Category Features**](#category-features)| |
| [Add or Modify Category](#add-or-modify-category)| Adds a new category or modifies an existing one based on input dictionary |
| [Delete Category](#delete-category)| Deletes a category based on its ID |
| [View Categories](#view-categories)| Retrieves a list of categories based on specified parameters |
| [**Item Receive Features**](#item-receive-features)| |
| [Add Item Receive](#add-item-receive)| Adds a new item receive entry along with details |
| [Modify Item Receive](#modify-item-receive)| Modifies an existing item receive entry along with details |
| [Delete Item Receive](#delete-item-receive)| Deletes an item receive entry based on its ID|
| [View Item Receive](#view-item-receive) | Retrieves a list of item receive entries based on specified parameters |
| [View Item Receive Details](#view-item-receive-details) | Retrieves details of a specific item receive entry |
| [**Damage Loss Features**](#damage-loss-features) | |
| [Add Damage Loss](#add-damage-loss)| Adds a new damage loss entry along with details |
| [Modify Damage Loss](#modify-damage-loss)| Modifies an existing damage loss entry along with details |
| [Delete Damage Loss](#delete-damage-loss)| Deletes a damage loss entry based on its ID  |
| [View Damage Loss](#view-damage-loss) | Retrieves a list of damage loss entries based on specified parameters |
| [View Damage Loss Details](#view-damage-loss-details) | Retrieves details of a specific damage loss entry |
| [**Sale Features**](#sale-features) | |
| [Add Sale](#add-sale)| Adds a new sale entry along with details |
| [Modify Sale](#modify-sale)  | Modifies an existing sale entry along with details |
| [Delete Sale](#delete-sale) | Deletes a sale entry based on its ID |
| [View Sale](#view-sale) | Retrieves a list of sale entries based on specified parameters |
| [View Sale Details](#view-sale-details) | Retrieves details of a specific sale entry |
| [**User Features**](#user-features)  | |
| [Add or Modify User](#add-or-modify-user) | Adds a new user or modifies an existing one based on input dictionary |
| [Delete User](#delete-user) | Deletes a user based on their ID |
| [View Users](#view-users) | Retrieves a list of users based on specified parameters |
| [**User Role Features**](#user-role-features)| |
| [Add or Modify User Role](#add-or-modify-user-role) | Adds a new user role or modifies an existing one based on input dictionary |
| [Delete User Role](#delete-user-role) | Deletes a user role based on their ID |
| [View User Roles](#view-user-roles) | Retrieves a list of user roles based on specified parameters |
| [**User Role Permission Features**](#user-role-permission-features) |  |
| [Modify Permissions](#modify-permissions) | Modifies permissions for a specific user role |
| [Check Permission](#check-permission) | Checks if a user role has a specific permission  |  
| [**Store Configuration Features**](#store-configuration-features) |  |
| [Modify Store Configuration](#modify-store-configuration)  | Modifies the configuration settings for the store |   

###### [Back to table of contents](#table-of-contents)
