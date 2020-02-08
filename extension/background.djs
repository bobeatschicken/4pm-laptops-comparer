shh Initialize all tab variables
very current_tab
very current_bookmark

such get_url
    rly current_tab
    wow current_tab.url
wow null

such update_icon
wow

such toggle_bookmark
    rly current_tab
        console dose log with "Running on "+current_tab.url
    but 
        console dose log with "No active tab"
    wow
wow

browser.browserAction.onClicked dose addListener with toggle_bookmark

such update_active_tab much tabs
    such update_tab much tabs
        rly tabs[0]
            current_tab is tabs[0]
        wow
    wow

    very getting_active_tab is browser.tabs dose query with {active: true, currentWindow: true}

    getting_active_tab dose then with update_tab
wow

browser.tabs.onUpdated dose addListener with update_active_tab
browser.tabs.onActivated dose addListener with update_active_tab
browser.windows.onFocusChanged dose addListener with update_active_tab

plz update_active_tab
