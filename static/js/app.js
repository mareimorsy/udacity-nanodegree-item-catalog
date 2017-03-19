$(document).ready(function() {
	$(".del-post-link").click(function(e){
		// prevent link redirection even if it was just a #
		e.preventDefault();
		// submit the next form
		$(this).next().submit();
	});

	$(".critical-frm").submit(function(e){
		if( !confirm('Are you sure?') )
			e.preventDefault();
	});
});