$('#formStore').submit(function (event) {
    event.preventDefault();

    var formData = new FormData(this);

    $.ajax({
        type: 'POST',
        url: '/setting/save_store_configuration',
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {
            alert(data.message)
        },
        error: function (jqXHR, exception) {
            alert(jqXHR.responseJSON.error)
            console.log(jqXHR.responseJSON.error);
        }
    });
});


$('input[name="file"]').change(function () {
    readURL(this);
});

// Function to read and display the selected image
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#logo_image').attr('src', e.target.result);
            $('#image').attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function load_logo_image() {
    fetch('/setting/get_store_image')
        .then(response => response.blob())
        .then(blob => {
            // Create a URL for the blob data and set it as the image source
            const imageUrl = URL.createObjectURL(blob);
            document.getElementById('logo_image').src = imageUrl;
        })
        .catch(error => console.error('Error:', error));
}

function get_store_config() {

    fetch('/setting/get_store_configuration', {
        method: 'GET',
        headers: {
            'Content-type': 'application/json',
        },
    })
        .then(function (response) {
            return response.json()
        })
        .then(function (response) {
            store_data = response.data
            document.getElementById("storename").value = store_data["store_name"]
            document.getElementById("contactperson").value = store_data["contact_person"]
            document.getElementById("phonenumber").value = store_data["phone_no"]
            document.getElementById("address").value = store_data["address"]
        })
        .catch(error => {
            alert(error)
            console.error('Error:', error)

        });

}

window.onload = function () {
    get_store_config();
    load_logo_image();
}
