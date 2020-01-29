function on_load() {

	var richert = document.getElementById( "richert" ),
		text = document.getElementById( "text" );

	function on_click( evt ) {
		var background_page = browser.extension.getBackgroundPage();
		console.log( background_page.get_url() );
		background_page.logger( "yeet" );
	}

	richert.addEventListener( "click", on_click );

}

window.addEventListener( "load", on_load );