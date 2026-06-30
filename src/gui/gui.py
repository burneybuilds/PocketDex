import tkinter as tk

"""
Not working in this rn.

"""
def StringVar():

    pass

root = tk.Tk()
root.title("Pocket-Dex`s") # Name of the applications
root.minsize(200, 200)
root.geometry("900x590+50+50")
tk.Label(root, text="Hey How are you").pack(side="top")
username = StringVar()
name = tk.Entry(root, textvariable=username).pack()
root.mainloop()