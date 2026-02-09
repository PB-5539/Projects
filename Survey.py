# ----addons----
import tkinter as tk
from datetime import datetime
print("Addons loaded")

#----setup Gui----
root = tk.Tk()
root.title("GUI")
root.geometry("400x400")
start_time = datetime.now()
print("GUI Loaded")

#----define variables----
GUI_open = False
print("Variables defined")

#----define functions----
def on_button_click():
    print("Button Clicked!")

def elapsed_time():
    if GUI_open==True:
        elapsed = datetime.now() - start_time
        seconds = int(elapsed.total_seconds())
        timer_label.config(text=f"Timer: {seconds} seconds")
        root.after(1000, elapsed_time)
print("Functions defined")

#----create widgets----
label = tk.Label(root, text="Welcome to the GUI Application")
label.pack(pady=20)
timer_label = tk.Label(root, text="Timer: 0 seconds")
timer_label.pack(pady=10)
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)
print("Widgets Loaded")

#----ititialize functions----
elapsed_time()
#----run Gui----
print("Running Mainloop")
print("Opening GUI")
GUI_open = True
root.mainloop()
#----end of file----
GUI_open = False
print("GUI application has been closed.")
input("Press Enter to exit...")