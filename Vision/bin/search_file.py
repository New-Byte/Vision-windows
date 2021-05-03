import os
import sys
import pyttsx3 as spk
import speech_recognition as sr
import search_any as sa

def get_response(y):
	spk.speak("Which file shall i open for you sir ?")
	r = sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	inst = r.recognize_google(audio)
	if "exit" in inst or "quit" in inst or inst == "bye" or inst == "good bye":
		spk.speak("Good bye sir...")
		exit()
	else:
		ind = inst.index("number")
		num = sa.get_index(inst[ind + 7:])
		spk.speak("Opening file number " + str(num))
		os.popen("start /wait {pth}".format(pth=y[num-1]))

file ='"'+sys.argv[1]+'"'

y=sa.search_any_file(file)

if len(y) > 1:
	spk.speak("I found the following files for you...")
	print("List of files")
	print("---" * 35)
	for z in range(len(y[:-1])):
		print(z+1," | ",y[z])
	print("---" * 35)
	while True:
		try:
			get_response(y)
			break
		except:
			spk.speak("I can not understand what you are saying...")

else:
	spk.speak("{file} does not exist in your system.".format(file=file))