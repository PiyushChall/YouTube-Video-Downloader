import tkinter
import customtkinter
from pytube import YouTube


def start_download():
    try:
        youtube_link = link.get()
        youtube_object = YouTube(youtube_link)
        video = youtube_object.streams.get_highest_resolution()
        video.download()
    except:
        print("Invalid Link")
    print("Congratulations the Video is downloaded")


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("|YouTube Video Downloader|")

title = customtkinter.CTkLabel(app, text=" Just Insert that link here ")
title.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=50, textvariable=url)
link.pack()

finish_download = customtkinter.CTkLabel(app, text="")
finish_download.pack()

download = customtkinter.CTkButton(app, text="<Download>", command=start_download)
download.pack(padx=10, pady=10)

app.mainloop()
