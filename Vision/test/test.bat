@echo off
set ver=%1
set app=%2
set dl=%3
set sl=%4
if [%ver%]==[] (python C:\Users\POOJA\Desktop\Vision\Vision-windows\Vision\bin\main.py) else (
if "%ver%"=="version" (echo 0.0.3) else (
if "%ver%"=="install" OR "%ver%"=="uninstall" OR "%ver%"=="update" OR "%ver%"=="info" (python C:\Users\POOJA\Desktop\Vision\Vision-windows\Vision\bin\add-remove.py %ver% %app%)
	) 
	)
if "%ver%"=="translate" (translate %app% %dl% %sl%) else (echo Enter a valid command)
