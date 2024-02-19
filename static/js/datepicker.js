$(document).ready(function () {
    from = $("#from")
        .datepicker({
            dateFormat: 'yy-mm-dd',
            defaultDate: "+1w",
            changeMonth: true,
            changeYear: true
        })
        .on("change", function () {
            to.datepicker("option", "minDate", getDate(this));
        }),
        to = $("#to")
            .datepicker({
                dateFormat: 'yy-mm-dd',
                defaultDate: "+1w",
                changeMonth: true,
                changeYear: true
            })
            .on("change", function () {
                from.datepicker("option", "maxDate", getDate(this));
            });

    function getDate(element) {
        var dateFormat = 'yy-mm-dd';
        var date;
        try {
            date = $.datepicker.parseDate(dateFormat, element.value);
        } catch (error) {
            console.log(error);
            date = null;
        }

        return date;
    }

    $(".btnFrom").on("click", function () {
        $("#from").focus();
    });

    $(".btnTo").on("click", function () {
        $("#to").focus();
    });
});
