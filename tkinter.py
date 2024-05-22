from tkinter import *


window = Tk()
window.geometry("500x500")
window.title("My App")

intro_frame = Frame(background="#8094dc", width=500, height=500)
intro_frame.grid()

intro_title = Label(intro_frame, background="#8094dc", text="Welcome to...", font=25)
intro_title.grid(row=0, column=0)

redirect_button = Button(intro_frame, text="Continue", height=3, width=7)
redirect_button.grid()


window.mainloop()