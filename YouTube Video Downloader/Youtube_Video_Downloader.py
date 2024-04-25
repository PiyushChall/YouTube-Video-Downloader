# Importing Modules
import tkinter
import customtkinter
from pytube import YouTube


def video_download():
    try:
        youtube_link = link.get()
        youtube_object = YouTube(youtube_link, on_progress_callback=on_progress)
        video_title = youtube_object.title
        video = youtube_object.streams.get_highest_resolution()
        title.configure(text=video_title, text_color="#1B4242")
        finish_download.configure(text="")
        video.download()
        finish_download.configure(text="Downloaded", text_color="green")
    except:
        finish_download.configure(text="OOPS INVALID LINK or Download Error", text_color="red")


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
customtkinter.set_default_color_theme("green")
app = tkinter.Tk()
app.geometry("720x480")
app.title("YouTube Video Downloader")
app.configure(bg="#8daea1")

title = customtkinter.CTkLabel(app, text=" Insert the video link here ", text_color="#1B4242")
title.pack(padx=10, pady=10)

# Url Insertion
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=50, textvariable=url,fg_color="#EEE7DA")
link.pack()

# Download Completion
finish_download = customtkinter.CTkLabel(app, text="")
finish_download.pack()

# Progress Percentage
progress_percentage = customtkinter.CTkLabel(app, text="")
progress_percentage.pack()

# Progress Bar
progress_bar = customtkinter.CTkProgressBar(app, width=400, progress_color="#1B4242")
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text=" Download ", command=video_download, fg_color="#092635", hover_color="#1B4242")
download.pack(padx=10, pady=10)

# MainLoop of the app
app.mainloop()
