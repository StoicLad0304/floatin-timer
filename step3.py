#Tkinter is a built-in Python library for creating graphical user interfaces (GUIs).
import tkinter as tk

# Root is the main window of the application.
# tk.Tk() creates window
root = tk.Tk()

#Label is a widget in Tkinter that is used to display text or images.
label = tk.Label(root, text="Start Now")

# The pack() method is used to add the label to the window.
label.pack()

# The mainloop() method is called to start the event loop of the app.
# This loop keeps the application running.
root.mainloop()