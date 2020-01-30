var currentTab;
var currentBookmark;

function get_url() {
    if( currentTab ) {
        return currentTab.url;
    } else {
        return null;
    }
}


function updateIcon() {
    browser.browserAction.setTitle({
    // Screen readers can see the title
    title: currentBookmark ? 'Unbookmark it!' : 'Bookmark it!',
    tabId: currentTab.id
    }); 
}

function toggleBookmark() {
    if( currentTab ) {
        console.log( "Running on " + currentTab.url );
    } else {
        console.log( "No active tab" );
    }
}

browser.browserAction.onClicked.addListener(toggleBookmark);

function updateActiveTab( tabs ) {

    //console.log( tabs );

    function updateTab( tabs ) {
        if( tabs[ 0 ] ) {
            currentTab = tabs[ 0 ];
        }
    }

    var gettingActiveTab = browser.tabs.query( { active: true, currentWindow: true } );
    
    gettingActiveTab.then( updateTab );
}

browser.tabs.onUpdated.addListener( updateActiveTab );

browser.tabs.onActivated.addListener( updateActiveTab );

browser.windows.onFocusChanged.addListener( updateActiveTab );

updateActiveTab();
