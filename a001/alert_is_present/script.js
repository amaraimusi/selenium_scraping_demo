
$(()=>{

	window.setTimeout(function(){
		$('#test1').html('猫のしっぽ');
		
		let url = 'https://www.youtube.com/embed/Gwkx8DIWxsc';
		$('#test2').attr('src', url);
		
		alert('アラートテスト');
	}, 4000);
	
})