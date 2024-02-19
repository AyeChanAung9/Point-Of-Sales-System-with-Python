$(document).ready(function () {

    $("#username").keyup(function () {
        var inputValue = $(this).val();
        $(this).val(inputValue.toLowerCase());
        var regexp = /[^a-z]/g;
        if ($(this).val().match(regexp)) {
            $(this).val($(this).val().replace(regexp, ''));
        }
    });
    // Check if saved username and password exist in cookies.
    var savedUsername = getCookie('savedUsername');
    var savedPassword = getCookie('savedPassword');

    // Fill in the form fields with the saved values.
    if (savedUsername) {
        $('#username').val(savedUsername);
    }

    if (savedPassword) {
        $('#password').val(savedPassword);
    }

    $("#login-form").submit(function (event) {
        event.preventDefault(); // Prevent the default form submission
        var username = $('#username').val();
        var password = $('#password').val();
        var rememberMe = $('#remember_me').is(':checked');
        if (rememberMe) {
            setCookie('savedUsername', username, 30); // Set cookie for 30 days (adjust as needed).
            setCookie('savedPassword', password, 30);
        } else {
            // Clear the saved values from cookies if "Remember Me" is not checked.
            clearCookie('savedUsername');
            clearCookie('savedPassword');
        }
        $.ajax({
            type: "POST",
            url: "/login",
            data: { username: username, password: password, remember_me: rememberMe, role_name_can_empty: true },
            success: function (data) {
                // console.log(data);
                // alert(data.url)
                if (data.logged_in == true) {
                    window.location.href = data.url;
                } else {
                    $('.login-message').css('color', 'red');
                    $('.login-message').text(data.message);
                }
            },
            error: function (jqXHR, exception) {
                $('.login-message').css('color', 'red');
                $('.login-message').text(jqXHR.responseJSON["error"]);
                console.error('Error deleting item:', jqXHR);
            }
        });
    });
    // Function to set a cookie with a specified expiration time.
    function setCookie(name, value, days) {
        var expires = '';
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = '; expires=' + date.toUTCString();
        }
        document.cookie = name + '=' + value + expires + '; path=/';
    }

    // Function to get the value of a cookie.
    function getCookie(name) {
        var nameEQ = name + '=';
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            while (cookie.charAt(0) === ' ') {
                cookie = cookie.substring(1, cookie.length);
            }
            if (cookie.indexOf(nameEQ) === 0) {
                return cookie.substring(nameEQ.length, cookie.length);
            }
        }
        return null;
    }

    // Function to clear a cookie by setting its expiration to the past.
    function clearCookie(name) {
        document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    }
});
