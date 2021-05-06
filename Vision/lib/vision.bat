@echo off
set ver=%1
set app=%2
set dl=%3
set sl=%4
if [%ver%]==[] (python C:\Vision\Vision-windows\Vision\gui\gui_support_python.py) else (
if "%ver%"=="--cli" (python C:\Vision\Vision-windows\Vision\bin\main.py) else (if "%ver%"=="version" (echo 0.0.7) else (
if "%ver%"=="install" OR "%ver%"=="uninstall" OR "%ver%"=="update" OR "%ver%"=="info" (python C:\Vision\Vision-windows\Vision\bin\add-remove.py %ver% %app%) 
	) 
	)
)
if "%ver%"=="translate" (translate %app% %dl% %sl%) else (if "%ver%"=="browse" (python C:\Vision\Vision-windows\Vision\bin\browse.py %app%) else (
	if "%ver%"=="wiki" (python C:\Vision\Vision-windows\Vision\bin\wiki.py %app%) else (
		if "%ver%"=="telljoke" (python C:\Vision\Vision-windows\Vision\bin\jokes.py) else (
			if "%ver%"=="quote" (python C:\Vision\Vision-windows\Vision\bin\quotes.py) else (
				if "%ver%"=="readpdf" (python C:\Vision\Vision-windows\Vision\bin\reading.py %app% %dl%) else (
					if "%ver%"=="searchasset" (python C:\Vision\Vision-windows\Vision\bin\search_file.py %app%) else (
						if "%ver%"=="sleep" (python C:\Vision\Vision-windows\Vision\bin\system_controls.py "shutdown") else (
							if "%ver%"=="sleep" (python C:\Vision\Vision-windows\Vision\bin\system_controls.py "restart") else (
								if "%ver%"=="refresh" (python C:\Vision\Vision-windows\Vision\bin\training_bot.py) else (
									if "%ver%"=="watch" (python C:\Vision\Vision-windows\Vision\bin\youtube.py %app% %dl%) else (
										if "%ver%"=="--help" (command_list) else (
											if "%ver%"=="init" (set_env %app%) else (
												if "%ver%"=="checkstat" (envstat) else (
													if "%ver%"=="plot" (python C:\Vision\Vision-windows\Vision\bin\dav.py %app%)

													)

												)

											)
										)
									)
								)
							)
						)
					)
				)
			)
		)
	) 

	)
