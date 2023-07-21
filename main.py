import cv2
import pyperclip
import tkinter as tk
from tkinter import filedialog


# Define the font settings (font family, font size)
font_settings = ("Helvetica", 4)
# Define ASCII chars
ASCII_CHARS = ['⠀', '⢀', '⠄', '⠤', '⠶', '⡆', '⡖', '⣆', '⣤', '⣶', '⣿']


def resize_image(image, new_width=200):
    height, width = image.shape[:2]
    ratio = new_width / float(width)
    new_height = int(height * ratio)*3//5
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

def rgb_to_gray(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def pixels_to_ascii(image):
    ascii_str = ''
    for row in image:
        for pixel_value in row:
            index = pixel_value // 28
            ascii_str += ASCII_CHARS[index]
        ascii_str += '\n'
    return ascii_str

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global image
        image = cv2.imread(file_path)
        width_entry.delete(0, tk.END)
        width_entry.insert(tk.END, '200')
        show_result()

def show_result():
    global ascii_art
    if image is None:
        return
    new_width = int(width_entry.get())
    new_image = resize_image(image, new_width=new_width)
    gray_image = rgb_to_gray(new_image)
    ascii_art = pixels_to_ascii(gray_image)
    # Resize the ASCII art based on the desired output width
    ascii_lines = ascii_art.split('\n')
    output_width = int(width_entry.get())
    resized_ascii_lines = [line[:output_width] for line in ascii_lines]
    ascii_art = '\n'.join(resized_ascii_lines)
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, ascii_art)
    result_text.config(state=tk.DISABLED)

def copy_to_clipboard():
    if ascii_art:
        pyperclip.copy(ascii_art)


# GUI
root = tk.Tk()
root.title("ImgToASCII")

# Input settings
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

width_label = tk.Label(input_frame, text="Width:")
width_label.pack(side=tk.LEFT)

width_entry = tk.Entry(input_frame, width=10)
width_entry.insert(tk.END, '200')
width_entry.pack(side=tk.LEFT, padx=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

open_button = tk.Button(button_frame, text="Open Image", command=open_image)
open_button.pack(side=tk.LEFT, padx=5)

show_result_button = tk.Button(button_frame, text="Show Result", command=show_result)
show_result_button.pack(side=tk.LEFT, padx=5)

copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT, padx=5)

result_text = tk.Text(root, width=267, height=75, wrap=tk.WORD, state=tk.DISABLED, font=font_settings)
result_text.pack(pady=10)


image = None
ascii_art = None


root.mainloop()
