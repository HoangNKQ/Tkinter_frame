from tkinter import *
from tkinter import ttk

def create_entry_frame(parent):
    frame_1 = ttk.Frame(parent)

    frame_1.columnconfigure(0, weight = 1)
    frame_1.columnconfigure(1, weight = 3)

    label_find = ttk.Label(frame_1, text="Find what:")
    label_find.grid(column = 0, row = 0, sticky=W)
    entry_find = ttk.Entry(frame_1)
    entry_find.grid(column= 1, row = 0, sticky=E)

    label_replace = ttk.Label(frame_1, text="Replace with:")
    label_replace.grid(column = 0, row = 1, sticky=W)
    entry_replace = ttk.Entry(frame_1)
    entry_replace.grid(column= 1, row = 1, sticky=E)

    return frame_1

def create_button_frame(parent):
    frame_2 = ttk.Frame(parent)

    frame_2.columnconfigure(0, weight= 1)

    button_find_next = ttk.Button(frame_2, text = "Find Next")
    button_find_next.grid(column=0, row = 0)

    button_replace = ttk.Button(frame_2, text = "Replace")
    button_replace.grid(column=0, row = 1)
    
    button_replace_all = ttk.Button(frame_2, text = "Replace All")
    button_replace_all.grid(column=0, row = 2)
    
    button_cancel = ttk.Button(frame_2, text = "Cancel")
    button_cancel.grid(column=0, row = 3)

    return frame_2

def main_window():
    root = Tk()
    root.geometry("300x150")
    root.title("FrameTest")

    root.columnconfigure(0, weight = 4)
    root.columnconfigure(1, weight = 1)

    entry_frame = create_entry_frame(root)
    entry_frame.grid(column = 0, row = 0)

    button_frame = create_button_frame(root)
    button_frame.grid(column= 1, row = 0)

    root.mainloop()

if __name__ == "__main__":
    main_window()