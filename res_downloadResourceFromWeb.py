def res_downloadResourceFromWeb(url, name):
	import urllib.request
	urllib.request.urlretrieve(url, f'./res/{name}')