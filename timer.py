import tkinter as tk
import time
import subprocess

class FloatingTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.geometry("200x120")
        self.root.attributes("-topmost", True)

        self.running = False
        self.end_time = 0

        self.label = tk.Label(root, text="00:00", font=("Arial", 24))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, justify="center")
        self.entry.insert(0, "60")  # default 60 sec
        self.entry.pack()

        self.start_btn = tk.Button(root, text="Start", command=self.start)
        self.start_btn.pack(pady=5)

    def start(self):
        try:
            seconds = int(self.entry.get())
            self.end_time = time.time() + seconds
            self.running = True
            self.update()
        except:
            self.label.config(text="Invalid")

    def update(self):
        if self.running:
            remaining = int(self.end_time - time.time())
            if remaining > 0:
                mins = remaining // 60
                secs = remaining % 60
                self.label.config(text=f"{mins:02}:{secs:02}")
                self.root.after(1000, self.update)
            else:
                self.label.config(text="Done!")
                self.running = False
                self.notify()

    def notify(self):
        subprocess.run([
            "notify-send",
            "Timer",
            "Time's up!"
        ])

root = tk.Tk()
app = FloatingTimer(root)
root.mainloop()