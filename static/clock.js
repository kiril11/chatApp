function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    var month = today.getUTCMonth() + 1; 
    var day = today.getUTCDate();
    var year = today.getUTCFullYear();
    realDate = day + "/" + month + "/" + year;
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById("clock").innerHTML = "The date is: " + realDate + "." + " The current time is: " +
    h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i}; 
    return i;
}



