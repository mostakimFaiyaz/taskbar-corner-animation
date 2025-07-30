import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import pyautogui
import time

# Path helper for bundled GIF
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Load and resize GIF
gif_path = resource_path("planet.gif")

# Setup window
root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "white")

img = Image.open(gif_path)

# Resize to fit taskbar
taskbar_height = 35
aspect_ratio = img.width / img.height
new_width = int(taskbar_height * aspect_ratio)

frames = []
try:
    while True:
        resized = img.copy().resize((new_width, taskbar_height), Image.LANCZOS)
        frames.append(ImageTk.PhotoImage(resized))
        img.seek(len(frames))
except EOFError:
    pass

label = tk.Label(root, bd=0, bg='white')
label.pack()

window_width = frames[0].width()
window_height = frames[0].height()
root.geometry(f"{window_width}x{window_height}+0+0")

# Animation variables
last_mouse_pos = pyautogui.position()
last_move_time = time.time()
is_moving = False
current_frame = 0

def update_frame():
    global current_frame, is_moving
    if is_moving:
        label.config(image=frames[current_frame])
        current_frame = (current_frame + 1) % len(frames)
    root.after(100, update_frame)

def check_mouse():
    global last_mouse_pos, last_move_time, is_moving
    current_pos = pyautogui.position()
    if current_pos != last_mouse_pos:
        last_move_time = time.time()
        is_moving = True
    else:
        if time.time() - last_move_time > 0.1:  # 1 second idle = stop animation
            is_moving = False
    last_mouse_pos = current_pos
    root.after(100, check_mouse)

def keep_on_top():
    root.lift()
    root.attributes("-topmost", True)
    root.after(1000, keep_on_top)  # check every 1 second

# Start animation and motion checker
update_frame()
check_mouse()
keep_on_top()
root.mainloop()
