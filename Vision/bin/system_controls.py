import os
import pyttsx3 as spk
import sys
import pyttsx3 as spk

cmd = sys.argv[1]
if cmd=="shutdown":
	spk.speak("Shutting down...")
	os.system(cmd + " /s /t 0")
	
#reboot
elif cmd=="restart" or "reboot":
	spk.speak("Rebooting...")
	os.system("shutdown /r /t 0")