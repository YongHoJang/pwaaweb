//var dataStr = " sample text "

$(document).ready(function(){
    $("#navigation li a").on("click", function(e){
        e.preventDefault();
        var hrefval = $(this).attr("href");

        if(hrefval == "#panel") {
            var distance = $('#main-content').css('right');
            if(distance == "auto" || distance == "0px") {
               // $(this).addClass("open");                
                openSidePanel();
            } else {
                closeSidePanel();
            }
        }
    }); // end click event handler
    
    $("#closebtn").on("click", function(e){
        e.preventDefault();
        closeSidePanel();
    }); // end close button event handler


}); 



function openSidePanel() {
	$('#main-content').animate(
		{
			right: '400px'
		}, 
		400, 'easeOutQuint'
	); 
	$('#panel-button').html('close&nbsp;&raquo;');
}

function closeSidePanel(){
	//$("#navigation li a").removeClass("open");
	$('#main-content').animate(
		{
			right: '0px'
		}, 400, 'easeOutQuint'
	);
	$('#panel-button').html('&laquo;&nbsp;open');
}

// sil data search
function getSilDataOne(iso_code){
	var param = "iso_code="+iso_code;
	var url = "/f/getsildata";
	$.ajax({
		url: url,
		data: param,
		type: 'get',
		dataType: 'json',	// html   json
		cache: false,
		success: function( response ) {
			// callback
			getSilDataOneCallback(response);
		},
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			alert('Ajax failure');
		}
	});
}

// jfm data search
function getJfmDescData( languageIds ){
	var param = "languageIds="+languageIds;
	var url = "/f/jfmdescdata";
	$.ajax({
		url: url,
		data: param,
		type: 'get',
		dataType: 'json',	// html   json  jsonp
		cache: false,
		success: function( response ) {
			// callback
			getJfmDescDataCallback(response);
		},
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			alert('Ajax failure');
		}
	});
}

