// Initialize all tab variables 
var current_tab = undefined;
var current_bookmark = undefined;

function get_url() {
    if (current_tab) {
        return current_tab.url;
    }
    return null;
}

function update_icon() {}

function toggle_bookmark() {
    if (current_tab) {
        console.log("Running, on, " + current_tab.url);
    } else {
        console.log("No, active, tab");
    }
}

browser.browserAction.onClicked.addListener(toggle_bookmark);

function update_active_tab(tabs) {
    function update_tab(tabs) {
        if (tabs[0]) {
            current_tab = tabs[0]
        }
    }

    var getting_active_tab = browser.tabs.query({
        active: true,
        currentWindow: true
    });

    getting_active_tab.then(update_tab);
}

browser.tabs.onUpdated.addListener(update_active_tab);
browser.tabs.onActivated.addListener(update_active_tab);
browser.windows.onFocusChanged.addListener(update_active_tab);

update_active_tab();