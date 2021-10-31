// --------------- Which category to show when clicked on a certain catergory------------
function allcategory() {
  let obj = document.getElementById("changedcategory");
  obj.innerHTML = "All Categories";

  let to_show_or_notshow = [
    document.getElementById("passshow"),
    document.getElementById("creditshow"),
    document.getElementById("notesshow"),
  ];

  for (let i = 0; i < to_show_or_notshow.length; i++) {
    if (to_show_or_notshow[i].className == "notshow")
      to_show_or_notshow[i].className = "";
    // console.log(to_show_or_notshow[i].className)
  }
}

function not_show_func(showthisid, id1, id2) {
  let to_show_or_notshow = [
    document.getElementById(id1),
    document.getElementById(id2),
  ];

  document.getElementById(showthisid).className = "";

  for (let i = 0; i < to_show_or_notshow.length; i++) {
    to_show_or_notshow[i].className = "notshow";
  }
}

function passcategory() {
  let obj = document.getElementById("changedcategory");
  obj.innerHTML = "Passwords";

  not_show_func("passshow", "creditshow", "notesshow");
}

function cardcategory() {
  let obj = document.getElementById("changedcategory");
  obj.innerHTML = "Payment Cards";

  not_show_func("creditshow", "passshow", "notesshow");
}

function notescategory() {
  let obj = document.getElementById("changedcategory");
  obj.innerHTML = "Secure Notes";

  not_show_func("notesshow", "passshow", "creditshow");
}

// ------------- Showing the passwords, number, pin etc. and also copying them --------------

function showpassword() {
  let elm = document.getElementById("thispassword");

  if (elm.getAttribute("type") == "password") {
    elm.setAttribute("type", "text");
  } else elm.setAttribute("type", "password");
}

function copypassword() {
  let elm = document.getElementById("thispassword");

  // console.log(elm.getAttribute('value'));
  navigator.clipboard.writeText(elm.getAttribute("value"));
}

function shownumber() {
  let elm = document.getElementById("thisnumber");

  if (elm.getAttribute("type") == "password") {
    elm.setAttribute("type", "number");
  } else elm.setAttribute("type", "password");
}

function copynumber() {
  let elm = document.getElementById("thisnumber");

  // console.log(elm.getAttribute('value'));
  navigator.clipboard.writeText(elm.getAttribute("value"));
}

function showpin() {
  let elm = document.getElementById("thispin");

  if (elm.getAttribute("type") == "password") {
    elm.setAttribute("type", "number");
  } else elm.setAttribute("type", "password");
}

function copypin() {
  let elm = document.getElementById("thispin");

  // console.log(elm.getAttribute('value'));
  navigator.clipboard.writeText(elm.getAttribute("value"));
}

function showcvv() {
  let elm = document.getElementById("thiscvv");

  if (elm.getAttribute("type") == "password") {
    elm.setAttribute("type", "number");
  } else elm.setAttribute("type", "password");
}

function copycvv() {
  let elm = document.getElementById("thiscvv");

  // console.log(elm.getAttribute('value'));
  navigator.clipboard.writeText(elm.getAttribute("value"));
}

// -------------- Showing createnew categories ---------------

function showcreatenew() {
  let elm = document.getElementsByClassName("notshowcat");

  for (let i = 0; i < elm.length; i++) {
    if (elm[i].className == "notshowcat") elm[i].className += " notshow";
    else elm[i].className = "notshowcat";
    // console.log(elm[i].className);
  }
}
