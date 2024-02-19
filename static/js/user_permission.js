const actions = ["_read", "_write", "_delete"];

function checkActions(name) {
    for (const action of actions) {
        checkAndSetPermission(name + action)
    }
}

var permissions
function checkAndSetPermission(permission_name) {
    if (document.getElementById(permission_name).checked) {
        permissions.push(permission_name)
    }
}

function populatePermissions() {
    permissions = []
    checkActions('item')
    checkActions('category')
    checkActions('item_receive')
    checkActions('damage_loss')
    checkActions('sales')
    checkAndSetPermission('reports')
    checkAndSetPermission('users')
    checkAndSetPermission('user_roles')
    checkAndSetPermission('user_permissions')
    checkAndSetPermission('store_configuration')

    role_id = document.getElementById("role_id").value
    const permissions_data = {
        "role_id": role_id,
        "permissions": permissions
    };
    return permissions_data
}

function save_user_permission(event) {
    event.preventDefault();

    fetch('/setting/save_user_permission', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
        },
        body: JSON.stringify(populatePermissions())
    })
        .then(async function (response) {
            var data = await response.json();
            if (!response.ok) {
                throw data.error;
            }
            return data
        })
        .then(function (data) {
            alert(data.message);
        })
        .catch(error => {
            alert(error)
            console.error('Error:', error)

        });
}


function load_user_permission() {

    role_id = document.getElementById("role_id").value

    fetch('/setting/load_user_permission/' + role_id, {
        method: 'GET',
        headers: {
            'Content-type': 'application/json',
        },
    })
        .then(async function (response) {
            var data = await response.json();
            if (!response.ok) {
                throw data.error;
            }
            return data
        })
        .then(function (data) {
            permissions = data.data
            permissions.forEach(function (value) {
                document.getElementById(value).checked = true;
            });
        })
        .catch(error => {
            alert(error)
            console.error('Error:', error)
        });

}


window.onload = function () {
    load_user_permission();
}
