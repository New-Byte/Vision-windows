@echo off
set opt=%1
if "%opt%"=="-v" (
	echo Installing chocolatey....
	@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin" > C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing numpy....
	pip install numpy > C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing pandas....
	pip install pandas >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing pyttsx3....
	pip install pyttsx3 >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing pipwin....
	pip install pipwin >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing pyaudio....
	pipwin install pyaudio >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing SpeechRecognition....
	pip install SpeechRecognition >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing beautifulsoup4....
	pip install beautifulsoup4 >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing google....
	pip install google >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing webbrowser....
	pip install webbrowser >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing NLTK....
	pip install nltk >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	python C:\Vision\Vision-windows\Vision\lib\nl.py
	echo Installing tensorflow....
	pip install tensorflow >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing keras....
	pip install keras >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing word2number....
	pip install word2number >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing pyjokes....
	pip install pyjokes >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing wikipedia....
	pip install wikipedia >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing PyPDF2....
	pip install PyPDF2 >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing google-trans-new....
	pip install google-trans-new >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing keyboard....
	pip install keyboard >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing pafy....
	pip install pafy >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing python-vlc....
	pip install python-vlc >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing python-docx....
	pip install python-docx >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing youtube-search-python....
	pip install youtube-search-python >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing PyQt5....
	pip install PyQt5 >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo Installing PyQtWebEngine....
	pip install PyQtWebEngine >> C:\Vision\Vision-windows\Vision\lib\stop.txt
	echo To check installation status run "vision checkstat"

	) else (
	@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
	pip install numpy 
	pip install pandas
	pip install pyttsx3
	pip install pipwin
	pipwin install pyaudio
	pip install SpeechRecognition
	pip install beautifulsoup4
	pip install google
	pip install webbrowser
	pip install nltk
	python C:\Vision\Vision-windows\Vision\lib\nl.py
	pip install tensorflow
	pip install keras
	pip install word2number
	pip install pyjokes
	pip install wikipedia
	pip install PyPDF2
	pip install google-trans-new
	pip install keyboard
	pip install pafy
	pip install python-vlc
	pip install python-docx
	pip install youtube-search-python
	pip install PyQt5
	pip install PyQtWebEngine
	)