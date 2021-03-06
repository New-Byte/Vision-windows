from youtubesearchpython import VideosSearch
import sys
import pyttsx3 as spk
import speech_recognition as sr
from word2number import w2n 
import vlc
import pafy
import webbrowser as wb
from tkinter import *

def window():
	root=Tk()
	root.geometry("100x100")
	root.title("Vision Player")
	button=Button(text="Start",command=link,bg="#000",font="Times",fg="White",activebackground="#6b0e63",activeforeground="White")
	button.grid(row=5,column=5,stick="WE",padx=28,pady=10)
	root.mainloop()

def get_results(show,lim):
	results = []
	videosSearch = VideosSearch(show, limit = int(lim))
	result = videosSearch.result()['result']
	i = 1
	for x in result:
		video = {}
		video["ind"] = i
		video["title"] = x["title"]
		video["duration"] = x["duration"]
		video["link"] = x["link"]
		video["channel_name"] = x["channel"]["name"]
		video["channel_link"] = x["channel"]["link"]
		results.append(video)
		i += 1
		del video
	return results

def show_results(show,lim):
	results = get_results(show,lim)
	for x in results:
		print(x["ind"],end=". ")
		print("Title: ",x["title"])
		print("Duration: ",x["duration"])
		print("Video Link: ", x["link"])
		print("Channel Name: ",x["channel_name"])
		print("Channel Link: ", x["channel_link"])
		print("-"*100)

def get_response(show,lim):
	spk.speak("Which video shall i play sir ?")
	while True:
		try:
			r = sr.Recognizer()
			mic = sr.Microphone()
			with mic as source:
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
			inst = r.recognize_google(audio)
			break
		except:
			spk.speak("Sorry sir, I can not understand what you are saying..")
	return inst
def clean_title(title):
	response = list(map(str, title.split(" ")))
	punctuation = ["?",",",".","/","|",":",";",'`',"'",'"',"'s","'es"]
	result = [word for word in response if word not in punctuation]
	final = " ".join(result)
	return final

def clean_response(show, lim):
	response = list(map(str, get_response(show, lim).split(" ")))
	punctuation = ["?",",",".","/","|",":",";","'",'"',"'s"]
	result = [word for word in response if word not in punctuation]
	final = " ".join(result)
	return final

def play_video(x):
	url = x["link"]
	video = pafy.new(url)
	best = video.getbest()
	media = vlc.MediaPlayer(best.url)
	dur = media.get_length()
	media.play()
	while True:
		pass

def visit_playlist(x):
	spk.speak("Opening playlist")
	wb.open(x['channel_link'])


def check_response(show,lim):
	results = get_results(show,lim)
	response = clean_response(show,lim)
	print(response)
	global x
	for x in results:
		title = clean_title(x["title"]).lower()
		if response.lower()[:10] in title:
			spk.speak("playing " + x["title"])
			window()
			return 0
		elif "playlist" in response.lower():
			visit_playlist(x)
			return 0
		else:
			try:
				num = w2n.word_to_num(response)
				if x["ind"] == num:
					spk.speak("playing " + x["title"])
					window()
					return 0
			except:
				return 1
	return 1

def link():
	play_video(x)


show = sys.argv[1]
lim = sys.argv[2]

spk.speak("Here are the Top {lim} results for {show}".format(lim=lim,show=show))
show_results(show,lim)
if check_response(show,lim):
	spk.speak("Sorry sir, i could not find the match in the list")