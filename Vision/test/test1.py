from tkinter import *
def play_video(x):
	print(x)

def tkw():
	global x
	x = "playing"
	root=Tk()
	root.geometry("1200x300")
	root.title("Vision Player")
	button=Button(text="Start",command=link,bg="#000",font="Times",fg="White",activebackground="#6b0e63",activeforeground="White")
	button.grid(row=1,column=0,stick="WE",padx=28,pady=10)
	root.mainloop()

def link():
	play_video(x)
tkw()