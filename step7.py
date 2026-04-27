import tkinter as tk
import time

root = tk.Tk()
# root.overrideredirect(True)
root.attributes("-topmost", True)
root.configure(bg="grey")
root.focus_force()

label =tk.Label(root, text="0", font=("Arial", 30))
label.pack()

entry=tk.Entry(root)
entry.pack()

def Start():
    sec = int(entry.get())
    end_time = time.time() + sec
    def update():
        remain = int(end_time - time.time() + 1)
        label.config(text=str(remain))

        if remain > 0:
            root.after(1000, update)
        else:
            label.config(text="Time Up!!...")
    update()

offset_x=0
offset_y=0

def st_move(event):
    global offset_x, offset_y
    offset_x=event.x
    offset_y=event.y

def st_drag(event):
    x=event.x_root - offset_x
    y=event.y_root - offset_y
    root.geometry(f"+{x}+{y}")

root.bind("<Button-1>", st_move)
root.bind("<B1-Motion>", st_drag)
root.bind("<Button-3>", lambda e: root.destroy())

button = tk.Button(root, text="Start", command=Start)
button.pack()

root.mainloop()