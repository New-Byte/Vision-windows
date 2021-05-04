import os
import subprocess
import sys
import pyttsx3 as spk

def serach(app):# Function for the seraching app in C drive & adding path in pth file
	try:
		spk.speak("Searching for  "+app)
		print('10%...')
		pth=os.popen("dir C:\\{ap}.exe /b/s".format(ap=app)).read()
	except Exception as e:
		print(e)
	if pth != "File Not Found":
		f=open("E:\\pth.txt", 'a')
		f.write('{pth}'.format(pth=pth))
		f.close()
		print('100%...')
		return True
	print('100%...')
	return False

def launch(app):#Launching app using path in the pth file
	try:
		f=open("E:\\pth.txt","r")
		l=f.readlines()
	except:
		f=open("E:\\pth.txt","w")
		l=[]
	pth=None
	for i in l:
		if app.upper() in i.upper():
			pth=i[:-1]
			spk.speak("Launching  "+app)
			p=subprocess.Popen("{pth}".format(pth=pth))
			spk.speak(app + " launched successfully....")
			p.communicate()
			f.close()
			return True
	return False

app=sys.argv[1] #App to open
if launch(app):
	spk.speak("Closing  "+app)
else:
	if serach(app):
		if launch(app):
			spk.speak("Closing  "+app)
		else:
			spk.speak("App may not be installed yet")
	else:
		spk.speak("App may not be installed yet")