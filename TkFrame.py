from tkinter import *
from tkinter import ttk

frame1_on = True

def hide_frame():
    global frame_1, frame1_on

    if frame1_on:
        frame_1.grid_forget()
        frame1_on = False

def show_frame():
    global frame_1, frame1_on

    if not frame1_on:
        frame_1.grid()
        frame1_on = True

def create_entry_frame(parent):
    global frame_1

    frame_1 = ttk.Frame(parent)

    frame_1.columnconfigure(0, weight = 1)
    frame_1.columnconfigure(1, weight = 3)

    label_find = ttk.Label(frame_1, text="Find what:")
    label_find.grid(column = 0, row = 0, sticky=W, padx=5, pady=5)
    entry_find = ttk.Entry(frame_1)
    entry_find.grid(column= 1, row = 0, sticky=E, padx=5, pady=5)

    label_replace = ttk.Label(frame_1, text="Replace with:")
    label_replace.grid(column = 0, row = 1, sticky=W, padx=5, pady=5)
    entry_replace = ttk.Entry(frame_1)
    entry_replace.grid(column= 1, row = 1, sticky=E, padx=5, pady=5)

    match = StringVar()
    check_button1 = ttk.Checkbutton(frame_1, text = "Match case", variable=match, command= lambda: print(match.get()))
    check_button1.grid(column=0, row=2, pady=1, padx=10, columnspan=2, sticky=W)
    
    check_button2 = ttk.Checkbutton(frame_1, text = "Wrap around")
    check_button2.grid(column=0, row=3, pady=1, padx=10, columnspan=2, sticky=W)

    return frame_1

def create_button_frame(parent):
    frame_2 = ttk.Frame(parent)

    frame_2.columnconfigure(0, weight= 1)

    # button_hide = ttk.Button(frame_2, text = "Hide", command= hide_frame)
    # button_hide.grid(column=0, row = 2, padx=0, pady=3)

    button_cancel = ttk.Button(frame_2, text = "Cancel", command= parent.destroy)
    button_cancel.grid(column=0, row = 3, padx=0, pady=3)

    return frame_2

def main_window():

    root = Tk()
    
    root.title("FrameTest")

    root.columnconfigure(0, weight = 4)
    root.columnconfigure(1, weight = 1)

    entry_frame = create_entry_frame(root)
    entry_frame.grid(column = 0, row = 0)

    button_frame = create_button_frame(root)
    button_frame.grid(column= 1, row = 0)

    button_hide = ttk.Button(root, text = "Hide", command= hide_frame)
    button_hide.grid(column=1, row = 2, padx=0, pady=3)

    button_show = ttk.Button(root, text = "Show", command= show_frame)
    button_show.grid(column=1, row = 3, padx=0, pady=3)
    root.mainloop()

if __name__ == "__main__":
    main_window()