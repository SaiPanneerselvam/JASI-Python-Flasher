import tkinter as tk
window=tk.Tk()
window.title(" JASI ")
window.geometry("600x400")
newlabel = tk.Label(text = " JASI Manager ")
img = PhotoImage(file="loading.gif")
canvas.create_image(20,20, anchor=NW, image=img)
newlabel.grid(column=0,row=0)
window.mainloop()