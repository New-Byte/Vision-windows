import os
import pyttsx3 as spk
import sys

cmd = sys.argv[1]
if cmd=="shutdown":
	os.system(cmd + " /s")
#reboot
elif cmd=="restart" or "reboot":
	os.system("shutdown /r")