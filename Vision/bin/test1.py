from docx import *
import subprocess as sb
import string
import random

string.ascii_letters
'1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def fetch_user():
	uname = sb.getoutput("whoami")
	return uname.split("\\")[-1]

def creat_Directory(dir_name,dest):
	user = fetch_user()
	if dest=='desktop':
		dest='C:\\Users\\'+user+'\\Desktop'
	pth=sb.getoutput("mkdir "+dest+":\\"+dir_name)
	if len(pth) == 0:
		print('Created Succesfully')
	else:
		if 'syntax is incorrect' in pth:
			pth=sb.getoutput("mkdir "+dest+"\\"+dir_name)
			if len(pth) == 0:
				print('Created Succesfully')
			elif 'syntax is incorrect' in pth:
				print(pth)
			elif 'already exists' in pth:
				while len(pth)!=0:
					new=random.choice(string.ascii_letters)
					pth=sb.getoutput("mkdir "+dest+"\\"+dir_name+'-New-'+new)
					if len(pth) == 0:
						print('Created Succesfully')
		elif 'already exists' in pth:
			while len(pth)!=0:
				new=random.choice(string.ascii_letters)
				pth=sb.getoutput("mkdir "+dest+":\\"+dir_name+'-New-'+new)
				if len(pth) == 0:
					print('Created Succesfully')

def creat_any_file(filename,dest):
	user = fetch_user()
	if dest.lower()=='desktop':
		dest='C:\\Users\\'+user+'\\Desktop'
	document = Document()
	try:
		document.save(dest+'\\'+filename+'.py')
	except Exception as e:
		print(e)

creat_any_file('data.csv','desktop')
# creat_Directory('Saurabh','desktop')