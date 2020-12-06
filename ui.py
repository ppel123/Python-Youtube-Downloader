from tkinter import *
from PIL import ImageTk, Image
from downloader import download_video
from tkinter import messagebox
from moviepy.editor import *

def clicked_video():
    try:
        download_video(url.get())
    except Exception as e:
        messagebox.showinfo('Oops!. Problem.', 'URL not found or something else..')
    
def clicked_mp3():
    try:
        download_video(url.get())
    except Exception as e:
        messagebox.showinfo('Oops!. Problem.', 'URL not found or something else..')

    
    

window = Tk()

window.title("Youtube Video Downloader")


image = PhotoImage(file=r"C:\Users\Administrator\Desktop\Youtube Scrapper\youtube_image.png")
label = Label(image=image)
label.grid(row = 0, column = 0,  pady = 2)

label_for_app = Label(window, text="This is a simple application that can be used to \n download YouTube videos.\n\n Please enjoy responsively :).", font=("Arial Bold", 10))
label_for_app.grid(row = 0, column = 1,  pady = 2) 


lbl = Label(window, text="Please enter URL : ", font=("Arial Bold", 10))
lbl.grid(row=1,column=0,  pady=2)

url = Entry(window, width=40)
url.grid(row=1,column=1,  pady=2)

btn_v = Button(window, text="Download video-mp4", command=clicked_video)
btn_v.grid(row=2, column=1, sticky=E)

btn_mp3 = Button(window, text="Download mp3", command=clicked_mp3)
btn_mp3.grid(row=2, column=1, sticky=W)




window.geometry('550x300')

window.mainloop()
