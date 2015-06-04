
// global
var G_JFM_COUNTRIES = {};

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

	// get_jfm_countries
	setJfmCountries();

});		// END: $(document).ready(function(){


function setJfmCountries(){
	var param = "";
	var url = "/f/get_jfm_countries";
	$.ajax({
		url: url,
		data: param,
		type: 'get',
		dataType: 'json',	// html   json
		cache: false,
		success: function( response ) {
			G_JFM_COUNTRIES = response;
			//alert( G_JFM_COUNTRIES["aai"] );
		},
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			alert('Ajax failure');
		}
	});
}

// side open
function openSidePanel() {
	$('#main-content').animate(	{right: '400px'}, 400, 'easeOutQuint'	); 
	$('#panel-button').html('close&nbsp;&raquo;');
}

// side close
function closeSidePanel(){
	//$("#navigation li a").removeClass("open");
	$('#main-content').animate(	{right: '0px'}, 400, 'easeOutQuint'	);
	$('#panel-button').html('&laquo;&nbsp;open');
}




// loadingBar
function loadingBarShow(){
	var maskHeight = $(document).height();
	var maskWidth = $(window).width();
	$('#mask').css({'width': maskWidth,'height': maskHeight});
	$("#mask").show();
	var $layerObj = $("#loading_window");
	var left = ($(window).scrollLeft() + ($(window).width() - $layerObj.width()) / 2);
	var top = ($(window).scrollTop() + ($(window).height() - $layerObj.height()) / 2);	 
	left = left - 100;
	top = top - 100;
	$layerObj.css({'left' : left, 'top' : top, 'position' : 'absolute'});
	$layerObj.show();
} 
function loadingBarHide(){
	 $("#mask, #loading_window").hide();
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

// right panel data search
function getPanelData( iso_code ){
    $('#div_iso_code').html( iso_code ); // test
    loadingBarShow();  // loading
    $('#div_sildata').html( "<p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p>" );
    $('#div_jfmdata').html( "<p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p>" );
    getSilDataOne( iso_code );
	var languageIds = G_JFM_COUNTRIES[iso_code];	
	if( !languageIds ) languageIds = "";
	$('#div_languageIds').html( languageIds ); // test	
	if( languageIds ){
		getJfmDescData( languageIds );
	}else{
		loadingBarHide();  // loading
	}
}   


// sil data search callback
function getSilDataOneCallback(response){
    var re_html = "";
    if( response.iso_code ){
        re_html += "Reference name: "+ response.reference_name + " ("+ response.iso_code +")</br>";
        re_html += "Bible translation status: "+ response.existing_scripture + "</br>";
        re_html += "Existing scripture: "+ response.existing_scripture_dis + "</br>";
        $('#div_sildata').html( re_html );
        openSidePanel();
    }else{
        //alert("no data!");
    }
}

// jfm desc data
function getJfmDescDataCallback(response){
    var re_html = "";
    // shortDescription      longDescription
    var obj_1 = response.data[0];
    var obj_2 = response.data[1];
    if( obj_1  && obj_1._embedded && obj_1._embedded.mediaComponents[0] ){
        openSidePanel();
        re_html = obj_1._embedded.mediaComponents[0].longDescription;
        re_html = re_html.replace(/(?:\r\n|\r|\n)/g, '<br />');
        re_html += "</br></br>";
        re_html += "<img src='"+obj_1._embedded.mediaComponents[0].imageUrls.videoStill+"' width='100%'>";
        if( obj_2.downloadUrls.high.url ){
            var webPlayer_str = obj_2.webEmbedPlayer;
            if( webPlayer_str ){
                webPlayer_str = webPlayer_str.replace("640", "100%");
                webPlayer_str = webPlayer_str.replace("360", "240");
                re_html += "<br>"+webPlayer_str;
            }
            re_html += "<br><a href='"+obj_2.downloadUrls.high.url+"' >mp4 video file download</a>";
        }
        re_html += "<p>&nbsp;</p><p>&nbsp;</p>";
        $('#div_jfmdata').html( re_html );
    }    
    loadingBarHide();  // loading
}

