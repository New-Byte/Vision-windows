import sys
import pyttsx3 as spk
import wikipedia
import webbrowser

def search_wiki(inst):
	print("Searching " + inst + ".....")
	spk.speak("Searching " + inst + ".....")
	try:
		results = wikipedia.summary(inst, sentences = 4)
		link = wikipedia.page(inst)
		link = link.url
		webbrowser.open(link)
		spk.speak("According to wikipedia ")
		spk.speak(results)
	except:
		spk.speak("Sorry sir i could not find information about {inst} on wikipedia".format(inst=inst))
		print(wikipedia.search(inst))

query = sys.argv[1]
search_wiki(query)