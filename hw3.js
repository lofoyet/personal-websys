// JavaScript Document

function startTime() {
	"use strict";
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
	var greeting;
    m = checkTime(m);
    s = checkTime(s);
	if (h < 7) { greeting = " Get some sleep my friend!";}
	else if (h < 12) { greeting = " Good Morning!";}
	else if (h < 18) { greeting = " Focus on your work!";}
	else if (h < 20) { greeting = " What did you have for dinner?";}
	else if (h < 23) { greeting = " Party time!";}
	else { greeting = " Good Night!";}
    document.getElementById('txt').innerHTML =
    "It's " + h + ":" + m + ":" + s + greeting;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
	"use strict";
    if (i < 10) {i = "0" + i;}  // add zero in front of numbers < 10
    return i;
}


