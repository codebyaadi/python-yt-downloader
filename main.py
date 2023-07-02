import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=onProgress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Error!")

def onProgress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_of_completion = (bytes_downloaded / total_size) * 100
    per = str(int(percent_of_completion))
    progressPercent.configure(text=per + "%")
    progressPercent.update()

    # Update Progress Bar
    progressBar.set(float(percent_of_completion)/100)




# System setting
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Our app fram
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI Element
title = customtkinter.CTkLabel(app, text="Insert the YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var =tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Loading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progres Percent
progressPercent = customtkinter.CTkLabel(app, text="0%")
progressPercent.pack()

# Progress Bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()