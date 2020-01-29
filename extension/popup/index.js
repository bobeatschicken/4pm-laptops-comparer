function on_load() {

	var richert = document.getElementById( "richert" ),
		text = document.getElementById( "text" ),
		app = browser.extension.getBackgroundPage(),
		url,
		valid,
		pid,
		get_item,
		set_item,
		saved;

	saved = false;
	url = app.get_url().toLowerCase();
	valid = true;
	valid = valid && ( url.indexOf( "amazon.com" ) != -1 );

	function on_set() {
		
	}

	function on_set_error( error ) {
		console.log( error );
	}

	function on_got( item ) {
		if( item.hasOwnProperty( pid ) ) {
			text.innerHTML = "Saved!";
			saved = true;
		} else {
			text.innerHTML = "Save It!";
		}
	}

	function on_got_error( error ) {
		text.innerHTML = "Save It!";
		console.log( error );
	}

	if( url.indexOf( "amazon.com" ) == -1 ) {
		text.innerHTML = "Only Amazon!";
	} else {
		if( url.indexOf( "/dp/" ) == -1 ) {
			text.innerHTML = "Only Products!";
		} else {
			pid = url.split( "/dp/" )[ 1 ];
			pid = pid.split( "/" )[ 0 ];
			pid = pid.split( "?" )[ 0 ];
			get_item = browser.storage.local.get( pid );
			console.log( pid );
			get_item.then( on_got, on_got_error);
		}
	}

	function on_click( evt ) {
		app.logger( "yeet" );
		if( !saved ) {
			var item = {};
			item[ pid ] = false;
			set_item = browser.storage.local.set( item );
			set_item.then( on_set, on_set_error );
			saved = true;
			text.innerHTML = "Saved!";
		}
	}

	richert.addEventListener( "click", on_click );

}

window.addEventListener( "load", on_load );