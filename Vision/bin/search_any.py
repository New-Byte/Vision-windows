import os
from word2number import w2n

def search_any_file(filename):
	pths=''
	print(filename)
	print('Searching File....')
	pth=os.popen("wmic logicaldisk get caption").read()
	disks = pth.split("\n\n")
	for y in range(1,len(disks)):
		disks[y]=disks[y].strip()
		pths+=os.popen("dir "+disks[y]+"\\"+filename+".* /b/s").read()
	paths = pths.split("\n")
	return paths

def get_index(inst):
	return w2n.word_to_num(inst)