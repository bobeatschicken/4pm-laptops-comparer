function on_load() {
	var DEBUG = true;

	var CONSTANTS = {};

	CONSTANTS[ "KONAMI" ] = [];
	CONSTANTS[ "KEYCODE" ] = {};

	CONSTANTS.KEYCODE[ "LEFT" ] = 37;
	CONSTANTS.KEYCODE[ "UP" ] = 38;
	CONSTANTS.KEYCODE[ "RIGHT" ] = 39;
	CONSTANTS.KEYCODE[ "DOWN" ] = 40;
	CONSTANTS.KEYCODE[ "A" ] = 65;
	CONSTANTS.KEYCODE[ "B" ] = 66;
	CONSTANTS.KEYCODE[ "RETURN" ] = 13;

	CONSTANTS.KONAMI.push( CONSTANTS.KEYCODE.UP );
	CONSTANTS.KONAMI.push( CONSTANTS.KEYCODE.UP );
	CONSTANTS.KONAMI.push( CONSTANTS.KEYCODE.DOWN );
	CONSTANTS.KONAMI.push( CONSTANTS.KEYCODE.DOWN );
	CONSTANTS.KONAMI.push( CONSTANTS.KEYCODE.LEFT );
	CONSTANTS.KONAMI.push( CONSTANTS.KEYCODE.RIGHT );
	CONSTANTS.KONAMI.push( CONSTANTS.KEYCODE.LEFT );
	CONSTANTS.KONAMI.push( CONSTANTS.KEYCODE.RIGHT );
	CONSTANTS.KONAMI.push( CONSTANTS.KEYCODE.A );
	CONSTANTS.KONAMI.push( CONSTANTS.KEYCODE.B );
	CONSTANTS.KONAMI.push( CONSTANTS.KEYCODE.RETURN );

	CONSTANTS[ "KEYS_ARR" ] = Object.keys( CONSTANTS.KEYCODE );

	var GLOBALS = {};

	GLOBALS[ "assets" ] = JSON.parse( document.getElementById( "RICHERT_DIV" ).innerHTML );

	GLOBALS[ "keys" ] = {};

	GLOBALS.keys[ "idx" ] = 0;
	var i = 0;
	for( ; i < CONSTANTS.KEYS_ARR.length; i++ ) {
		GLOBALS.keys[ CONSTANTS.KEYCODE[ CONSTANTS.KEYS_ARR[ i ] ] ] = { "pressed" : false, "last_pressed" : false };
	}

	function update_key( code, pressed ) {
		if( GLOBALS.keys[ code ] === undefined ) {
			GLOBALS.keys[ code ] = { "pressed" : pressed, "last_pressed" : !pressed };
			return;
		}
		GLOBALS.keys[ code ].pressed = pressed;
	}

	function on_key_down( evt ) {
		update_key( evt.keyCode, true );
	}

	function on_key_up( evt ) {
		update_key( evt.keyCode, false );
	}

	document.addEventListener( "keydown", on_key_down );
	document.addEventListener( "keyup", on_key_up );

	function konami_game_loop() {
		var key_obj;
		var keys = Object.keys( GLOBALS.keys );
		for( var j = 0; j < keys.length; j++ ) {
			key_obj = GLOBALS.keys[ keys[ j ] ];
			if( keys[ j ] == CONSTANTS.KONAMI[ GLOBALS.keys.idx ] ) {
				if( key_obj.pressed && !key_obj.last_pressed ) {
					GLOBALS.keys.idx++;
				}
			}
			key_obj.last_pressed = key_obj.pressed;	
		}
		if( GLOBALS.keys.idx == 11 ) {
			document.body.innerHTML = "";
		}
		window.requestAnimationFrame( GLOBALS.game_loop );
	}

	GLOBALS.game_loop = konami_game_loop;

	window.requestAnimationFrame( GLOBALS.game_loop )

	if( DEBUG ) {
		window.RICHERT_DEBUG = {};
		window.RICHERT_DEBUG[ "CONSTANTS" ] = CONSTANTS;
		window.RICHERT_DEBUG[ "GLOBALS" ] = GLOBALS;
	}
}

on_load();