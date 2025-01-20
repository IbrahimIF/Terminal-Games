from PIL import Image
import tkinter as tk
from tkinter import scrolledtext

# Load and process the image
im = Image.open("Untitled.jpg")

pixels = list(im.getdata())
pixel_matrix = [pixels[i:i + im.width] for i in range(0, len(pixels), im.width)]

brightness_matrix = []
ASCII_matrix = []
for row in pixel_matrix:
    brightness_row = []
    ASCII_row = []
    for (r, g, b) in row:
        mavs = (r + g + b) / 3  # Average brightness
        brightness_row.append(mavs)

        # Map brightness to ASCII characters
        if mavs == 0:
            ASCII_row.append("^")
        elif mavs <= 25.5:
            ASCII_row.append(":")
        elif mavs <= 76.5:
            ASCII_row.append("~")
        elif mavs <= 102:
            ASCII_row.append("|")
        elif mavs <= 127.5:
            ASCII_row.append("x")
        elif mavs <= 153:
            ASCII_row.append("L")
        elif mavs <= 178.5:
            ASCII_row.append("m")
        elif mavs <= 204:
            ASCII_row.append("#")
        elif mavs <= 229.5:
            ASCII_row.append("8")
        else:
            ASCII_row.append("B")

    brightness_matrix.append(brightness_row)
    ASCII_matrix.append(ASCII_row)

# Convert the ASCII matrix to a single string
ascii_art = "\n".join("".join(row) for row in ASCII_matrix)

# Function to display the ASCII art in a separate pop-up
def display_ascii_art():
    # Create a new Tkinter window
    root = tk.Tk()
    root.title("ASCII Art Viewer")

    # Set the size of the window and make it resizable
    root.geometry("800x600")  # Adjust window size as needed
    root.resizable(True, True)

    # Add a scrollable text area
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 3), background="black", foreground="white")
    text_area.pack(expand=True, fill=tk.BOTH)

    # Insert the ASCII art into the text area
    text_area.insert(tk.END, ascii_art)

    # Disable editing of the text area
    text_area.configure(state="disabled")

    # Run the Tkinter event loop
    root.mainloop()

# Call the function to display the ASCII art
display_ascii_art()