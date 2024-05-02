# Importing Modules
import tkinter
import customtkinter
from pytube import YouTube


# Function to fetch the video detail
def get_video_details():
    try:
        youtube_link = link.get()
        youtube_object = YouTube(youtube_link, on_progress_callback=on_progress)
        video_title = youtube_object.title
        title.configure(text=video_title, text_color="#f50538")
        return youtube_object
    except:
        finish_download.configure(text="OOPS INVALID LINK or Download Error", text_color="red")


# function for downloading audio
def audio_download():
    try:
        youtube_object = get_video_details()
        audio = youtube_object.streams.get_audio_only()
        finish_download.configure(text="")
        audio.download()
        finish_download.configure(text="Downloaded", text_color="green")
    except:
        finish_download.configure(text="OOPS INVALID LINK or Download Error", text_color="#f50538")


# function for downloading video
def video_download():
    try:
        youtube_object = get_video_details()
        video = youtube_object.streams.get_highest_resolution()
        finish_download.configure(text="")
        video.download()
        finish_download.configure(text="Downloaded", text_color="green")
    except:
        finish_download.configure(text="OOPS INVALID LINK or Download Error", text_color="#f50538")


# function for proress bar
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    completion_percentage = str(int(percentage_of_completion))
    progress_percentage.configure(text=completion_percentage + "%")
    progress_percentage.update()
    progress_bar.set(float(percentage_of_completion) / 100)


# Appearance
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
app = tkinter.Tk()
app.geometry("720x480")
app.title("YouTube Video Downloader")
app.configure(bg="#000000")
app.iconbitmap("favicon.ico")

title = customtkinter.CTkLabel(app, text=" Insert the video link here ", text_color="#f50538")
title.pack(padx=10, pady=10)

# Url Insertion
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=50, textvariable=url, fg_color="#f3d0a4")
link.pack()

# Download Completion
finish_download = customtkinter.CTkLabel(app, text="")
finish_download.pack()

# Progress Percentage
progress_percentage = customtkinter.CTkLabel(app, text="", text_color="#b6042a")
progress_percentage.pack()

# Progress Bar
progress_bar = customtkinter.CTkProgressBar(app, width=400, progress_color="#f50538")
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download Button
download_mp4_highres = customtkinter.CTkButton(app, text=" Download MP4 ", command=video_download, fg_color="#79021c",
                                               hover_color="#b6042a")
download_mp4_highres.pack(padx=10, pady=10)

download_audio = customtkinter.CTkButton(app, text=" Download MP3 ", command=audio_download, fg_color="#79021c",
                                         hover_color="#b6042a")
download_audio.pack(padx=10, pady=10)

# MainLoop of the app
app.mainloop()
