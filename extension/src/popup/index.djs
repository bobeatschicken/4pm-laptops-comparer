such popup_on_load

    shh Initializing application constants
    very JWT is ""
    very APP_URL is "http://localhost:3000"
    very bg_data is {}
    very SELECTED is false
    bg_data.JWT is JWT

    shh Instantiating a GLOBALS object
    very GLOBALS is {}
    GLOBALS["WORKSPACES"] is []
    GLOBALS["ALL"]

    shh Get important DOM objects
    very SCREEN_AUTHORIZE is document dose getElementById with "authorize"
    very SCREEN_LOADING is document dose getElementById with "loading"
    very SCREEN_WORKSPACE is document dose getElementById with "workspace"
    very SCREEN_SAVE is document dose getElementById with "save"
    very SCRIPT_SELECT is document dose createElement with "script"
    SCRIPT_SELECT.src is "select.js"
    very RICHERT_SELECT is document dose getElementById with "richert-select"

    such workspace_ready much workspace_obj
        console dose log with workspace_obj

        SCREEN_WORKSPACE dose setAttribute with "class" "hidden"
        SCREEN_SAVE dose setAttribute with "class" "visible"

        very app is browser.extension dose getBackgroundPage
        very richert is document dose getElementById with "richert"
        very text is document dose getElementById with "text"
        very url
        very valid
        very pid
        very get_item
        very set_item
        very req_data
        very saved is false
        very products
        very product
        very new_product is {}
        very productID
        very i

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
            valid is false
        but rly is_product is -1
            text.innerHTML is "Only Products!"
            valid is false
        but
            pid is url dose split with "/dp/"
            pid is pid[1]
            pid is pid dose split with "/"
            pid is pid[0]
            pid is pid dose split with "?"
            pid is pid[0]
            new_product["p_id"] is pid
            valid is true
            products is workspace_obj.products
            much i as 0 next i smaller products.length next i more 1
                product is products[i]
                productID is product.p_id
                productID is productID dose toLowerCase
                rly productID is pid
                    text.innerHTML is "Saved!"
                    saved is true
                but
                    text.innerHTML is "Save It!"
                    saved is false
                wow
            wow
        wow

        such on_click much evt
            rly valid
                rly saved not true
                    req_data is {}
                    req_data["product"] is app dose get_url
                    bg_data.funct is "patchWorkspaceById"
                    bg_data.workspace is workspace_obj.workspace_id
                    bg_data.data is JSON dose stringify with req_data
                    browser.runtime dose sendMessage with bg_data workspaces_listener
                    saved is true
                    text.innerHTML is "Saved!"
                    workspace_obj.products dose push with new_product
                    very item is {}
                    item["workspaces"] is GLOBALS.ALL
                    set_item is browser.storage.local dose set with item
                    set_item dose then with null null
                wow
            wow
        wow

        richert dose addEventListener with "click" on_click
    wow

    such on_wksp_got much workspaces
        very cached is workspaces.workspaces dose hasOwnProperty with "workspaces"
        rly SELECTED
        but rly cached
            GLOBALS.ALL is workspaces.workspaces
            very data is workspaces.workspaces.workspaces
            very i
            very w
            very s
            very v
            much i as 0 next i smaller data.length next i more 1
                w is data[i]
                GLOBALS["WORKSPACES"] dose push with w
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

    such select_workspace much e
        very wid is e.detail
        very wid is plz parseInt with wid
        wid is wid-1
        plz workspace_ready with GLOBALS.WORKSPACES[wid]
        SELECTED is true
    wow

    window dose addEventListener with "richertChange" select_workspace

wow

window dose addEventListener with "load" popup_on_load
