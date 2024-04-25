import tkinter
import customtkinter
from pytube import YouTube


def start_download():
    try:
        youtube_link = link.get()
        youtube_object = YouTube(youtube_link, on_progress_callback=on_progress)
        video_title = youtube_object.title
        video = youtube_object.streams.get_highest_resolution()
        title.configure(text=video_title,text_color="white")
        finish_download.configure(text="")
        video.download()
        finish_download.configure(text="Downloaded",text_color="green")
    except:
        finish_download.configure(text="INVALID LINK or Download Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    completion_percentage = str(int(percentage_of_completion))
    progress_percentage.configure(text=completion_percentage + "%")


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

progress_percentage = customtkinter.CTkLabel(app, text="")
progress_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="<Download>", command=start_download)
download.pack(padx=10, pady=10)

app.mainloop()
