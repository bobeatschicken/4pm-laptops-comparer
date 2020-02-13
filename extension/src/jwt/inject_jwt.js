var jwt = document.createElement("script");
jwt.src = browser.runtime.getURL("jwt/jwt.js");
var doc = document.head || document.documentElement;
doc.appendChild(jwt);