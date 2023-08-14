import traceback
try:
	from mainTotal import mainTotal
	mainTotal()
except:
	print(traceback.format_exc())
	input()