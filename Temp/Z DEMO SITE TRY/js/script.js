/* =================================== $ Variavble for id Start ===================================== */

var $ = function(id) {
    return document.getElementById(id);
}

/* =================================== $ Variavble for id End ===================================== */



/* =================================== $ Variavble for class Start ===================================== */

var clss = function(className) {
    return document.getElementsByClassName(className);
}

/* =================================== $ Variavble for class End ===================================== */



/* =================================== Nav Color change Start ===================================== */

var myHNav = $("header1");
var myNavA = clss("header1");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
    myHNav.style.color = "black";
    myHNav.style.backgroundColor = "white";
    myHNav.style.transition = "1s";
    myNavA.onmouseover = function () { myHNav.style.color = "white"; };
    // myHNav.onmouseout = function () { pinmouseOut() };
  } else {
    myHNav.style.color = "white";
    myHNav.style.backgroundColor = "black";
    myHNav.style.transition = "1s";
    myNavA.onmouseover = function () { myHNav.style.color = "black"; };
    // myHNav.onmouseout = function () { pinmouseOut() };
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

/* =================================== Nav Color change End ===================================== */



