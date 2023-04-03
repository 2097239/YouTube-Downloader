import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from turtle import left
from pytube import *




window = tk.Tk()
window.title("Youtube Downloader")
window.minsize(450, 220)
window.configure(bg="#EEEEDD")
window.resizable(False, False)



def browse():
    directory = askdirectory(initialdir="Yor directory path", title="save")
    download_dir.set(directory)

def download():
    link = video_link.get()
    save_dir = download_dir.get()
    yt = YouTube(link)
    yt.streams.filter(file_extension="mp4").get_highest_resolution().download(save_dir)
    messagebox.showinfo(title="Success", message="Your video has been downloaded successfully!") 
         

download_dir = tk.StringVar() 
video_link = tk.StringVar()   

link_label = tk.Label(window, text="Video link:")
link_label.grid(row=0, column=0, padx=20, pady=20)
link_label.config(font=("bold", 14), fg="Brown", bg="#EEEEDD" )

link_input = tk.Entry(window, width=30, textvariable=video_link)
link_input.grid(row=0, column=1)


place_label = tk.Label(window, text="Directory:")
place_label.grid(row=1, column=0)
place_label.config(font=("bold", 14), fg="Brown", bg="#EEEEDD")

place_input = tk.Entry(window, width=28, textvariable=download_dir)
place_input.grid(row=1, column=1, sticky="w")

place_btn = tk.Button(window, text="Save As", width="5", bg="orange", font=("bold", 9), fg="black", command=browse)
place_btn.grid(row=1, column=2, pady=15)
place_btn.config(height=1, width=8)


download_btn = tk.Button(text="Download", command=download)
download_btn.grid(row=2, column=1, pady=15)
download_btn.config(height=1, width=12, font=("bold", 9), bg="orange", fg="black")



window.mainloop()