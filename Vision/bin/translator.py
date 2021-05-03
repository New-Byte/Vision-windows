import translate as tl 
import pyttsx3 as spk
import sys

def translate_file(voice,path,lang):
	file = open(path,'r')
	lines = file.readlines()
	for line in lines:
		translate_speech(line,voice,lang,'en')


def change_lang(voice,dl):
	global engine
	engine = spk.init()
	engine.setProperty('voice',voice)
	engine.setProperty('language',dl)

def translate_speech(text,voice,dl,sl):
	change_lang(voice,dl)
	newtext = tl.translate_text(text,dl,sl)
	spk.speak(newtext)
	print(newtext)

text = sys.argv[1]
dl = sys.argv[2]
sl = sys.argv[3]
voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_HemantM"

if text=="file":
	translate_file(voice,dl,sl)
else:
	translate_speech(text,voice,dl,sl)