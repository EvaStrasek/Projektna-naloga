from tkinter import *

okno = Tk()
okno.title("Hitrostno tipkanje")
okno.configure(bg = "dark green")
okno.configure(width = 800, height = 600)

#centrira okno
winWidth = okno.winfo_reqwidth()
winwHeight = okno.winfo_reqheight()
posRight = int(okno.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(okno.winfo_screenheight() / 2 - winwHeight / 2)
okno.geometry("+{}+{}".format(posRight, posDown))
#

#gumb za start


okno.mainloop()
