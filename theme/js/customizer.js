/**
 * Theme Customizer enhancements for a better user experience.
 *
 * Contains handlers to make Theme Customizer preview reload changes asynchronously.
 */

( function( $ ) {
	// Site title and description.
	wp.customize( 'blogname', function( value ) {
		value.bind( function( to ) {
			$( '.site-title a' ).text( to );
		} );
	} );
	wp.customize( 'blogdescription', function( value ) {
		value.bind( function( to ) {
			$( '.site-description' ).text( to );
		} );
	} );
	// Link color.
	wp.customize( 'graphy_link_color', function( value ) {
		value.bind( function( newval ) {
			$( '.entry-content a, .entry-summary a, .comment-content a, .comment-respond a, .navigation a, .comment-navigation a, .current-menu-item > a' ).css('color', newval );
		} );
	} );
} )( jQuery );
