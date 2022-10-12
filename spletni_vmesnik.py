from tkinter import *
import time

okno = Tk()
okno.title("Hitrostno tipkanje")
okno.configure(bg = "dark green")
okno.geometry("{0}x{1}+0+0".format(okno.winfo_screenwidth(), okno.winfo_screenheight()))

zacetna_vrstica = Label(okno, text = "Za začetek igre klikni gumb Start")
zacetna_vrstica.pack()

#gumb za start
def start_button():
    vrstica = Label(okno, text = "Igra se je začela!")
    vrstica.pack()

start_button = Button(okno, text = 'Start',padx = 70,pady = 30, command = start_button)
start_button.pack()

type_box = Entry(okno,width = 60)
type_box.pack()

def casovnik(cas):
    while cas > 0:
        time.sleep(1)
        cas -=1
    konec = Label(okno,text ='Čas se je iztekel. Igre je konec!').pack()

#izbira za casovnik
vrstica_za_izbiro = Label(okno, text = 'Izberi pojubno časovno omejitev za igro:')
vrstica_za_izbiro.pack()
moznosti_za_casovnik = ['1 min', '2 min', '5 min']

def nastavitev_casovnika(event):
    vrstica1 = Label(okno, text=moznosti.get())
    if moznosti.get() == '1 min':
        #casovnik(60)
        pass
    if moznosti.get() == '2 min':
        #casovnik(120)
        pass
    else:
        #casovnik(300)
        pass

moznosti = StringVar()
moznosti.set(moznosti_za_casovnik[0])

izbira = OptionMenu(okno, moznosti, *moznosti_za_casovnik, command = nastavitev_casovnika)
izbira.pack()




okno.mainloop()
