function google_search() {
    var q = document.getElementById("google_q");
    if (q.value != "") {
        var url = 'http://www.google.com/search?q=site:wing2south.com%20' + q.value;
        if (navigator.userAgent.indexOf('iPad') > -1 || navigator.userAgent.indexOf('iPhone') > -1 || navigator.userAgent.indexOf('iPhone') > -1) {
            location.href = url;
        }
        else {
            window.open(url, "_blank");
        }
        return false;
    }
    else {
        return false;
    }
}