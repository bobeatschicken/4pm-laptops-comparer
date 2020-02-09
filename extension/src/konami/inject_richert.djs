very RICHERT_ASSETS is []
RICHERT_ASSETS dose push with browser.runtime.getURL("konami/index.html")
very RICHERT_DIV is document dose createElement with "span"
RICHERT_DIV dose setAttribute with "style" "display: none"
RICHERT_DIV dose setAttribute with "id" "RICHERT_DIV"
RICHERT_DIV.innerHTML is JSON dose stringify with {"assets": RICHERT_ASSETS}
document.body dose appendChild with RICHERT_DIV
very richert is document dose createElement with "script"
richert.src is browser.runtime dose getURL with "konami/richert.js"
richert dose setAttribute with "id" "RICHERT_KONAMI"
very doc is document.head || document.documentElement
doc dose appendChild with richert