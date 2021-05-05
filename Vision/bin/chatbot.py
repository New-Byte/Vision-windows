import random
import json
import pickle
import numpy as np 
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import pyttsx3 as spk
import os
from word2number import w2n

lemmatizer = WordNetLemmatizer()

intents = json.loads(open("C:\\Vision\\Vision-windows\\Vision\\bin\\intents.json").read())

words = pickle.load(open("C:\\Vision\\Vision-windows\\Vision\\models\\words.pkl", 'rb'))
classes = pickle.load(open("C:\\Vision\\Vision-windows\\Vision\\models\\classes.pkl", 'rb'))
model = load_model("C:\\Vision\\Vision-windows\\Vision\\models\\chatbot_model.h5")

def clean_up(sentence):
	sen_words = nltk.word_tokenize(sentence)
	sen_words = [lemmatizer.lemmatize(word) for word in sen_words]
	return sen_words

def extract_num(msg,ind,s):
	if "of" in msg:
		index = msg.index("of")
	elif "from" in msg:
		index = msg.index("from")
	else:
		index = msg.index("in")
	num = msg[ind + s:index-1]
	try:
		return w2n.word_to_num(num)
	except:
		return 1

# def pos_tag(sentence):
# 	pos_list = []
# 	tokens = nltk.word_tokenize(sentence)
# 	for w in tokens:
# 		pos_list.extend(nltk.pos_tag([w]))

# 	return pos_list

def bag_of_words(sentence):
	sen_words = clean_up(sentence)
	bag = [0] * len(words)
	for w in sen_words:
		for i, word in enumerate(words):
			if word == w:
				bag[i] = 1
	return np.array(bag)

def predict_class(sentence):
	bow = bag_of_words(sentence)
	res = model.predict(np.array([bow]))[0]
	ERROR_THRESHOLD = 0.25
	result = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
	result.sort(key=lambda x: x[1], reverse=True)
	return_list = []
	for r in result:
		return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
	return return_list

def get_responses(intents_list, intents_json):
	tag = intents_list[0]['intent']
	list_of_intents = intents_json['intents']
	for i in list_of_intents:
		if i['tag'] == tag:
			result = random.choice(i['responses'])
			break
	return result

def run(msg):
	ints = predict_class(msg)
	if ints[0]['intent'] == "launchapp":
		res = get_responses(ints, intents)
		cmd = list(map(str,msg.split(" ")))
		spk.speak(cmd[0] + "ing" + cmd[-1])
		os.system(res + " " + cmd[-1])
		return 0

	elif ints[0]['intent'] == "add-remove":
		res = get_responses(ints, intents)
		if "install" in msg:
			ind = msg.index("install")
			process = "install"
			app = msg[ind + 8:]
		elif "uninstall" in msg:
			ind = msg.index("uninstall")
			process = "uninstall"
			app = msg[ind + 10:]
		elif "remove" in msg:
			ind = msg.index("remove")
			process = "uninstall"
			app = msg[ind + 7:]
		elif "update" in msg:
			ind = msg.index("update")
			process = "update"
			app = msg[ind + 7:]
		elif "upgrade" in msg:
			ind = msg.index("upgrade")
			process = "update"
			app = msg[ind + 8:]
		elif "inform" in msg:
			process = "info"
			app = list(map(str,msg.split(" ")))[-1]

		os.system("vision " + process + " " + app)
		return 0

	elif ints[0]['intent'] == "translate":
		res = get_responses(ints, intents)
		ind = msg.index("translate")
		text = msg[ind + 10:-8]
		if "hindi" in msg.lower():
			lang_code = 'hi'
		elif "hindi" not in msg.lower():
			spk.speak("language is not supported...")
		os.system(res + " " + '"'+ text + '"' + " " +  lang_code + " " + "en")
		return 0

	elif ints[0]['intent'] == "jokes":
		res = get_responses(ints, intents)
		os.system(res)
		return 0

	elif ints[0]['intent'] == "quotes":
		res = get_responses(ints, intents)
		os.system(res)
		return 0

	elif ints[0]['intent'] == "readpdf":
		res = get_responses(ints, intents)
		if "page" not in msg:
			page = 1
		elif "page number" in msg:
			ind = msg.index("page number")
			page = extract_num(msg,ind,12)
		elif "page" in msg:
			ind = msg.index("page")
			page = extract_num(msg,ind,5)
		pdfind = msg.index("pdf")
		pdf = msg[pdfind + 4:]
		if "dot" in pdf:
			pdf_name = pdf[:pdf.index("dot")-1] + ".pdf"
		else:
			pdf_name = pdf + ".pdf"

		os.system(res + " " + pdf_name + " " + str(page))
		return 0

	elif ints[0]['intent'] == "searchdoc":
		res = get_responses(ints, intents)
		if "file" in msg.lower():
			ind = msg.index("file")
			file = msg[ind + 5:]
		elif "folder" in msg.lower():
			ind = msg.index("folder")
			file = msg[ind + 7:]
		elif "directory" in msg.lower():
			ind = msg.index("directory")
			file = msg[ind + 10:]
		if "dot" in file:
			name = file[:file.index("dot")-1]
		else:
			name = file

		os.system(res + " " + '"' + name + '"')
		return 0

	elif ints[0]['intent'] == "goodbye":
		res = get_responses(ints, intents)
		spk.speak(res)
		return 1

	elif ints[0]['intent'] == "youtube":
		res = get_responses(ints, intents)
		if "result" in msg.lower():
			ind2 = msg.index("result") - 1
			if "top" in msg.lower():
				ind1 = msg.index("top") + 4
			elif "first" in msg.lower():
				ind1 = msg.index("first") + 6
			else:
				ind1 = ind2 - 3
			try:
				num = w2n.word_to_num(msg[ind1:ind2])
			except:
				num = 3
			if "of" in msg.lower():
				show = msg[ind2 + 3:]
			else:
				show = msg[ind2 + 5:]
		else:
			num = 3
			if "watch" in msg.lower():
				show = msg[msg.index("watch") + 6:]
			elif "show" in msg:
				show = msg[msg.index("show") + 5:]
			else:
				show = msg

		os.system(res + " " + '"' + show + '"' + " " + str(num))
		return 0

	elif ints[0]['intent'] == "wikipedia":
		res = get_responses(ints, intents)
		os.system(res)
		return 0

	elif ints[0]['intent'] == "browser":
		res = get_responses(ints, intents)
		if "about" in msg:
			ind = msg.index("about") + 6
			query = msg[ind:]
		elif "search" in msg:
			ind = msg.index("search") + 7
			query = msg[ind:]
		else:
			query = msg

		os.system(res + ' ' + '"'+query+'"')
		return 0

	elif ints[0]['intent'] == "goodbye":
		res = get_responses(ints, intents)
		spk.speak(res)
		return 1

	elif ints[0]['intent'] == "system":
		res = get_responses(ints, intents)
		if "shut" in msg.lower() or "power" in msg.lower():
			cmd = "shutdown"
		elif "reboot" in msg.lower() or "restart" in msg.lower():
			cmd = "restart"

		os.system(res + cmd)
		return 0


	else:
		res = get_responses(ints, intents)
		spk.speak(res)
		return 0