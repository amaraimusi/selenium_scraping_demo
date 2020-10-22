<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="UTF-8">
	<meta name="google" content="notranslate" />
   	<meta http-equiv="X-UA-Compatible" content="IE=edge">
   	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Seleniumスクレイピングのテスト用ページ | ワクガンス</title>
	<link rel='shortcut icon' href='/home/images/favicon.ico' />
	
	<link href="/note_prg/css/bootstrap.min.css" rel="stylesheet">
	<link href="/note_prg/css/highlight/default.css" rel="stylesheet">
	<link href="/note_prg/css/common2.css" rel="stylesheet">
	<script src="/note_prg/js/jquery3.js"></script>	<!-- jquery-3.3.1.min.js -->
	<script src="/note_prg/js/bootstrap.min.js"></script>
	<script src="/note_prg/js/vue.min.js"></script>
	<script src="/note_prg/js/highlight.pack.js"></script>
	<script src="/note_prg/js/livipage.js"></script>
	<script src="/note_prg/js/ImgCompactK.js"></script>

	<script>hljs.initHighlightingOnLoad();</script>
</head>
<body>
<div id="header" ><h1>Seleniumスクレイピングのテスト用ページ | ワクガンス</h1></div>
<div class="container">



<form action="test2.php" method="post">
	<div data-id="101">
		<input id="neko1" type="text" name="neko_name" class="neko_class" value="新入りの帽子猫" >
	</div>
	<input type="submit" value="Submit">
</form>

<a href="https://ja.wikipedia.org/">Wikipedia</a>

<hr>
<div>
	<script>
	function clickBtn1(){
		let html = `
			<input id='btn2' type='button' value='テストボタン2' onclick='clickBtn2()' />
		`;
		jQuery('#div1').html(html);
	}
	function clickBtn2(){
		alert('ボタン２をクリックしました。');
	}
	</script>
	<input id="btn1" type="button" value="テストボタン" onclick="clickBtn1()"/>
	<div id="div1"></div>
</div>


<hr />
<ol id="plant_list">
	<li>アサガオ</li>
	<li>ヒルガオ</li>
	<li>グンバイヒルガオ</li>
	<li>リュウキュウシャリンバイ</li>
</ol>

<div class="yohaku"></div>
<ol class="breadcrumb">
	<li><a href="/">ホーム</a></li>
</ol>
</div><!-- content -->
<div id="footer">(C) kenji uehara 2020-10-17</div>
</body>
</html>