from tkinter import *
from PIL import ImageTk, Image
from downloader import download_video
from downloader import download_mp3
from tkinter import messagebox


def clicked_video():
    try:
        title, views, length, description, rating, status = download_video(url.get())

        lbl_title = Label(window, text="Title : ", font=("Arial Bold", 10))
        lbl_title.grid(row=4,column=0,  pady=2)

        lbl_title_value = Label(window, text=title, font=("Arial Bold", 10))
        lbl_title_value.grid(row=4,column=1,  pady=2)

        lbl_views = Label(window, text="Views : ", font=("Arial Bold", 10))
        lbl_views.grid(row=5,column=0,  pady=2)

        lbl_views_value = Label(window, text=views, font=("Arial Bold", 10))
        lbl_views_value.grid(row=5,column=1,  pady=2)

        lbl_length = Label(window, text="Length : ", font=("Arial Bold", 10))
        lbl_length.grid(row=6,column=0,  pady=2)

        lbl_length_value = Label(window, text=length, font=("Arial Bold", 10))
        lbl_length_value.grid(row=6,column=1,  pady=2)

        """lbl_description = Label(window, text="Description : ", font=("Arial Bold", 10))
        lbl_description.grid(row=7,column=0,  pady=2)

        lbl_description_value = Label(window, text=description, font=("Arial Bold", 10))
        lbl_description_value.grid(row=7,column=1,  pady=2)

        lbl_rating = Label(window, text="Rating : ", font=("Arial Bold", 10))
        lbl_rating.grid(row=8,column=0,  pady=2)

        lbl_rating_value = Label(window, text=rating, font=("Arial Bold", 10))
        lbl_rating_value.grid(row=8,column=1,  pady=2)

        lbl_status = Label(window, text=status, font=("Arial Bold", 15))
        lbl_status.grid(row=9,column=1,  pady=2)"""
    except Exception as e:
        messagebox.showinfo('Oops!. Problem.', 'URL not found or something else..')
    
def clicked_mp3():
    try:
        print(url.get())
        download_mp3(url.get())
    except Exception as e:
        messagebox.showinfo('Oops!. Problem.', 'URL not found or something else..')

    
    

window = Tk()

window.title("Youtube Video Downloader")


image = PhotoImage(file=r"youtube_image.png")
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




window.geometry('700x400')

window.mainloop()
