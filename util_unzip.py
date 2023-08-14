def util_unzip(filePath):
	import zipfile
	with zipfile.ZipFile(filePath, 'r') as f:
		f.extractAll('./res')