def init_taskbarIconEnable():
	import ctypes
	appId = 'mycompany.myproduct.subproduct.version'
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)