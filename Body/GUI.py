import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import pygame

import logging

# Configure Pygame to suppress informational messages
logging.basicConfig(level=logging.WARNING)

# Your existing Pygame code here

def play_opening_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("D:\MyData\Documents\CODING\Python\Jarvis\Data\Music\GUI-Sound.mp3")
    pygame.mixer.music.play()


def gui():
    # Create the main window
    root = tk.Tk()
    root.title("J A R V I S")

    # Play the opening sound
    play_opening_sound()

    # Load the GIF image
    gif_path = "D:\MyData\Documents\CODING\Python\Jarvis\Data\GIF\Siri.gif"
    gif = Image.open(gif_path)
    gif_width, gif_height = gif.width, gif.height

    # Create a tkinter-compatible image from the PIL image
    tk_gif = ImageTk.PhotoImage(gif)

    # Create a label to display the GIF
    label = Label(root, image=tk_gif)
    label.pack()

    def update_label(frame=0):
        if not root.winfo_exists():  # Check if the window has been closed
            return
        frame = (frame + 1) % gif.n_frames
        gif.seek(frame)
        tk_gif_new = ImageTk.PhotoImage(gif)
        label.configure(image=tk_gif_new)
        label.image = tk_gif_new
        root.after(1, update_label, frame)  # Increase the delay time to 100 milliseconds

    # Start the GIF animation
    update_label()

    # Start the GUI event loop
    root.mainloop()


# Call the gui function to start the GUI
gui()
