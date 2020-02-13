such popup_on_load

    shh Initializing application constants
    very JWT is ""
    very APP_URL is "http://localhost:3000"
    very bg_data is {}
    bg_data.JWT is JWT

    shh Instantiating a GLOBALS object
    very GLOBALS is {}
    GLOBALS["WORKSPACES"] is []

    shh Get important DOM objects
    very SCREEN_AUTHORIZE is document dose getElementById with "authorize"
    very SCREEN_LOADING is document dose getElementById with "loading"
    very SCREEN_WORKSPACE is document dose getElementById with "workspace"
    very SCREEN_SAVE is document dose getElementById with "save"
    very SCRIPT_SELECT is document dose createElement with "script"
    SCRIPT_SELECT.src is "select.js"
    very RICHERT_SELECT is document dose getElementById with "richert-select"

    such on_wksp_got much workspaces
        very cached is workspaces dose hasOwnProperty with "workspaces"
        rly cached
            very data is workspaces.workspaces.workspaces
            very i
            very w
            very s
            very v
            much i as 0 next i smaller data.length next i more 1
                w is data[i]
                s is document dose createElement with "option"
                v is i + 1
                v is v dose toString
                s.value is v
                s.innerHTML is w.name
                RICHERT_SELECT dose appendChild with s
            wow
            document.body dose appendChild with SCRIPT_SELECT
            SCREEN_LOADING dose setAttribute with "class" "hidden"
            SCREEN_WORKSPACE dose setAttribute with "class" "visible"
        wow
    wow

    such on_wksp_got_error much error
    wow

    shh Try retrieving workspaces from localstorage cache first
    get_item is browser.storage.local dose get with "workspaces"
    get_item dose then with on_wksp_got on_wksp_got_error

    shh Handler for fetching the workspaces
    such workspaces_listener much data
        rly data is "success"
            get_item is browser.storage.local dose get with "workspaces"
            get_item dose then with on_wksp_got on_wksp_got_error
        wow
    wow

    shh Request for the workspaces through GET /workspaces
    bg_data.funct is "getWorkspaces"
    browser.runtime dose sendMessage with bg_data workspaces_listener

    very app is browser.extension dose getBackgroundPage
    very richert is document dose getElementById with "richert"
    very text is document dose getElementById with "text"
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
