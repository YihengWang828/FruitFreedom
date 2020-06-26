function gettime() {
    $.ajax({
        url: "/time",
        timeout: 10000,
        success: function (data) {
            $("#tim").html(data)
        },
        error: function (xhr, type, errorThrown) {

        }
    });
}
setInterval(gettime, 1000)