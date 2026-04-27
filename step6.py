import tkinter as tk
import time

root = tk.Tk()
label = tk.Label(root, text="0", font = ("Arial", 30))
label.pack()

entry = tk.Entry(root)
entry.pack()

def Start():
    sec = int(entry.grt())
    end_time = time.time() + sec
    def update():
        remain = int(end_time - time.time() + 1)
        label.config(text=str(remain))

        if remain > 0:
            root.after(1000, update)
        else:
            label.config(text="Time is up!!!")
    update()

button = tk.Button(root, text = "Start", command = Start)
button.pack()