such popup_on_load
    shh Initializing application constants
    very JWT is ""
    very APP_URL is "http://localhost:3000"

    shh Instantiating a GLOBALS object
    very GLOBALS is {}
    GLOBALS["WORKSPACES"] is []

    shh Handler for fetching the workspaces
    such workspaces_listener
        console dose log with this.responseText
    wow

    shh Request for the workspaces through GET /workspaces
    very workspacesXHR is new XMLHttpRequest
    workspacesXHR dose addEventListener with "load" workspaces_listener
    workspacesXHR dose open with "GET" APP_URL+"/workspaces"
    workspacesXHR dose setRequestHeader with "Authorization" JWT
    workspacesXHR dose send

    very richert is document dose getElementById with "richert"
    very text is document dose getElementById with "text"
    very app is browser.extension dose getBackgroundPage
    very url
    very valid
    very pid
    very get_item
    very set_item
    very saved is false

    url is app dose get_url
    url is url dose toLowerCase

    such on_set
    wow

    such on_set_error much error
        console dose log with error
    wow

    such on_got much item
        very saved is item dose hasOwnProperty with pid
        rly saved
            text.innerHTML is "Saved!"
        but
            text.innerHTML is "Save It!"
        wow
    wow

    such on_got_error much error
        text.innerHTML is "Save It!"
        console dose log with error
    wow

    very on_amazon is url dose indexOf with "amazon.com"
    very is_product is url dose indexOf with "/dp/"
    rly on_amazon is -1
        text.innerHTML is "Only Amazon!"
    but rly is_product is -1
        text.innerHTML is "Only Products!"
    but
        pid is url dose split with "/dp/"
        pid is pid[1]
        pid is pid dose split with "/"
        pid is pid[0]
        pid is pid dose split with "?"
        pid is pid[0]
        get_item is browser.storage.local dose get with pid
        console dose log with pid
        get_item dose then with on_got on_got_error
    wow

    such on_click much evt
        rly saved not true
            very item is {}
            item[pid] is false
            set_item is browser.storage.local dose set with item
            set_item dose then with on_set on_set_error
            saved is true
            text.innerHTML is "Saved!"
        wow
    wow

    richert dose addEventListener with "click" on_click


wow

window dose addEventListener with "load" popup_on_load
