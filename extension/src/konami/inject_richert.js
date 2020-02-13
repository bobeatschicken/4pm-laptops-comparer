var RICHERT_ASSETS = [];
RICHERT_ASSETS.push(browser.runtime.getURL("konami/index.html"));
var RICHERT_DIV = document.createElement("span");
RICHERT_DIV.setAttribute("style", "display: none");
RICHERT_DIV.setAttribute("id", "RICHERT_DIV");
RICHERT_DIV.innerHTML = JSON.stringify({
    "assets": RICHERT_ASSETS
});
document.body.appendChild(RICHERT_DIV);
var richert = document.createElement("script");
richert.src = browser.runtime.getURL("konami/richert.js");
richert.setAttribute("id", "RICHERT_KONAMI");
var doc = document.head || document.documentElement;
doc.appendChild(richert);