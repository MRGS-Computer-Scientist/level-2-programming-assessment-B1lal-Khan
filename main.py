from tkinter import *

w_width = 500
w_height = 700

window = Tk()
window.geometry(str(w_width) + "x" + str(w_height))
window.title("My App")

main_frame = Frame(background="red", width=w_width, height=w_height)
main_frame.pack()

hello_label = Label(text="Hello. world")
hello_label.place(x=300, y=300)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
window.mainloop()