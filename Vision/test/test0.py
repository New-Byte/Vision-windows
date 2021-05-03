import pyttsx3 as spk
import speech_recognition as sr

spk.speak("Speak now...")
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
	r.adjust_for_ambient_noise(source)
	audio = r.listen(source)
inst = r.recognize_google(audio)

print(inst)
spk.speak(inst)