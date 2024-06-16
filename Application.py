import tkinter as tk
import customtkinter
import imageDetector
import videoDetector
from tkinter import Label, filedialog as fd, messagebox as mbox

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# Create the root window
root = customtkinter.CTk()
root.title('Potholes Detection')
root.resizable(False, False)
root.geometry('400x200')

# Create heading label
HeadingText = Label(root, text="Select Image or Video to Identify Pothole", font=("poppins", 16))

def select_image_file():
    # Restricting only Image files to be selected through the application
    filetypes = (('Image files', '*.jpg'),)
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if len('D:\Pothole_detection\project_files\buzzer.mp3') > 0:
        mbox.showinfo(title='Selected Image File', message=filename)
        if imageDetector.detectPotholeonImage(filename):  # Assuming detectPotholeonImage returns True if a pothole is detected
            root.bell('D:\Pothole_detection\project_files\buzzer.mp3')  # Play system bell sound

def select_video_file():
    # Restricting only Video files to be selected through the application
    filetypes = (('Video files', '*.mp4'),)
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if len('D:\Pothole_detection\project_files\buzzer.mp3') > 0:
        mbox.showinfo(title='Selected Video File', message=filename)
        if videoDetector.detectPotholeonVideo(filename):  # Assuming detectPotholeonVideo returns True if a pothole is detected
            root.bell('D:\Pothole_detection\project_files\buzzer.mp3')  # Play system bell sound

# Create buttons
image_open_button = customtkinter.CTkButton(root, text='Image', command=select_image_file, hover_color="green")
video_open_button = customtkinter.CTkButton(root, text='Video', command=select_video_file, hover_color="green")
liveCamera_button = customtkinter.CTkButton(root,
                                            text='Live Camera',
                                            command=lambda: videoDetector.detectPotholeonVideo(0),
                                            hover_color="green",
                                            border_color="black",
                                            border_width=2.5,
                                            fg_color="red",
                                            font=("poppins", 14))

# Place widgets
HeadingText.place(x=50, y=15)
image_open_button.place(x=40, y=80)
video_open_button.place(x=220, y=80)
liveCamera_button.pack(side='bottom', pady=20)

# Run the application
root.mainloop()
