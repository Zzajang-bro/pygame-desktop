import traceback
try:
	from res_downloadAllWebResource import res_downloadAllWebResource
	res_downloadAllWebResource()
	input('done')
except:
	print(traceback.format_exc())
	input()