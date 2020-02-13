function on_load() {

    var richert = document.getElementById("richert");
    var text = document.getElementById("text");
    var app = browser.extension.getBackgroundPage();
    var url = undefined;
    var valid = undefined;
    var pid = undefined;
    var get_item = undefined;
    var set_item = undefined;
    var saved = false;

    url = app.get_url();
    url = url.toLowerCase();

    function on_set() {}

    function on_set_error(error) {
        console.log(error);
    }

    function on_got(item) {
        var saved = item.hasOwnProperty(pid);
        if (saved) {
            text.innerHTML = "Saved!"
        } else {
            text.innerHTML = "Save It!"
        }
    }

    function on_got_error(error) {
        text.innerHTML = "Save It!"
        console.log(error);
    }

    var on_amazon = url.indexOf("amazon.com");
    var is_product = url.indexOf("/dp/");
    if (on_amazon === -1) {
        text.innerHTML = "Only Amazon!"
    } else if (is_product === -1) {
        text.innerHTML = "Only Products!"
    } else {
        pid = url.split("/dp/");
        pid = pid[1]
        pid = pid.split("/");
        pid = pid[0]
        pid = pid.split("?");
        pid = pid[0]
        get_item = browser.storage.local.get(pid);
        console.log(pid);
        get_item.then(on_got, on_got_error);
    }

    function on_click(evt) {
        if (saved !== true) {
            var item = {};
            item[pid] = false
            set_item = browser.storage.local.set(item);
            set_item.then(on_set, on_set_error);
            saved = true
            text.innerHTML = "Saved!"
        }
    }

    richert.addEventListener("click", on_click);


}

window.addEventListener("load", on_load);