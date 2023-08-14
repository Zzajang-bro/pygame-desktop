def res_downloadFontD2coding():
	from res_downloadResourceFromWeb import res_downloadResourceFromWeb
	url = 'https://github.com/naver/d2codingfont/releases/download/VER1.3.2/D2Coding-Ver1.3.2-20180524.zip'
	fileNm = 'D2.zip'
	res_downloadResourceFromWeb(url, fileNm)
