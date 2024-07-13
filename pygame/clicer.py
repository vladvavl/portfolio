#портфолио
from random import randint
import tkinter as tk
a=0
def klic():
    global a
    a+=1
    tekst["text"]=str(a)

def portal():
    cnopka.place(x=randint(0,700),y=randint(0,500))
    window.after(1000,portal)
window= tk.Tk()
window.title("кликер")
window.geometry("800x600")
window.resizable(width=False,height=False)
window["bg"]="green2"
#счетчик текст
tekst=tk.Label(window, text="0", 
               font=("Arial",20,"bold"), 
               bg="gold", fg= "blue4")
tekst.pack()
# создаем кнопку
cnopka=tk.Button(window, 
                text="нажми",
                bg="green4", fg="blue4",
                padx="7", pady="6",
                font=("Arial",20,"bold"),
                command=klic )

cnopka.place(x=randint(0,700),y=randint(0,500))

portal()
window.mainloop()
# https://trinket.io/python