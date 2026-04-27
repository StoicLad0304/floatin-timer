import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="0", font=("Arial", 30))
label.pack()

count = 5

def update():
    global count
    if count > 0:
        label.config(text=str(count))
        count -= 1
        root.after(1000, update)
    else:
        label.config(text="Time's up!")
update()
root.mainloop()