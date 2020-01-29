var currentTab;
var currentBookmark;

function logger( yeet ) {

}

function get_url() {
    if( currentTab ) {
        return currentTab.url;
    } else {
        return "null";
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
    if( currentBookmark ) {
        console.log( "we clicked" );
    } else {
        console.log( "we clicked but nope" );
    }
}

browser.browserAction.onClicked.addListener(toggleBookmark);

function updateActiveTab( tabs ) {

    console.log( tabs );

    function updateTab( tabs ) {
        if( tabs[ 0 ] ) {
            currentTab = tabs[ 0 ];
            console.log( currentTab.url );
        }
    }

    var gettingActiveTab = browser.tabs.query( { active: true, currentWindow: true } );
    
    gettingActiveTab.then( updateTab );
}

browser.tabs.onUpdated.addListener( updateActiveTab );

browser.tabs.onActivated.addListener( updateActiveTab );

browser.windows.onFocusChanged.addListener( updateActiveTab );

updateActiveTab();
