import tkinter as tk
import os
from tkinter import font as ft, filedialog as fd

class App:
    def __init__(self):
        root = tk.Tk()
        root.title("Captions maker")
        root.geometry("500x500+400+100")
        root['bg'] = 'steel blue'
        root.resizable(False, False)

        def select_video():
            #asking user to select a video file
            path = fd.askopenfilename(title="Select video file",
                                              filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")])
            if path:
                print(f"Selected video path: {path}")
                select_video_label.config(text=f"Selected video: {os.path.basename(path)}")

        tk.Label(text="Captions maker", font=('Arial', 40, 'bold'), bg='steel blue').pack(pady=10)

        #select video button
        select_video = tk.Button(root, text="Select video", font=('Arial', 14), bg='steel blue', width=20, height=2, command=select_video)
        select_video.pack(pady=20)

        #display selected video label
        select_video_label = tk.Label(text="Selected video:", font=('Arial', 28), bg='steel blue')
        select_video_label.pack()

        #create captions button
        create_subtitle = tk.Button(root, text="Create captions", font=('Arial', 14), bg='steel blue', width=20, height=2)
        create_subtitle.pack(pady=20)
        root.mainloop()


App()
