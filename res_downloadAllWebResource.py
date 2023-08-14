def res_downloadAllWebResource():
	from res_downloadResourceFromWeb import res_downloadResourceFromWeb
	resNmList = ['aisaka', 'blueMoon', 'earth', 'honeycomb', 'hoshino', 'hoshino2', 'naisho']
	for resNm in resNmList:
		url = f'http://small.23jhj.com/Zzajang-bro/workspace/wallpapers/{resNm}.jpg'
		fileNm = f'{resNm}.jpg'
		res_downloadResourceFromWeb(url, fileNm)

if __name__ == '__main__':
	import traceback
	try:
		input()
		res_downloadAllWebResource()
		input()
	except:
		print(traceback.format_exc())
		input()