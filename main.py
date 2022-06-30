
from concurrent.futures import process
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.pyplot import text
from asistant import *

process = 0
class ventana:
   
    label = ''
    def __init__(self,root1):
        self.root = root1
        self.root.title("hola")
        self.root.configure(background="green")
        app_width = 1330
        app_height= 670
        screen_width = self.root.winfo_screenwidth()
        screen_heigth = self.root.winfo_screenheight()
        x= (screen_width/2)-(app_width/2)
        y= (screen_heigth/2)-(app_height/2)
        self.root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.root.resizable(0,0)
        self.bg = ImageTk.PhotoImage(file="Aula definitivo.png")
        canvas = Canvas(self.root)
        canvas.create_image(0,0,image=self.bg,anchor=NW)
        canvas.pack(fill=BOTH, expand=True)

        def inicio():
            text = listen()
        #    global process
        #    text = 'aa'
        #    process = int(process)+1
        #    if process > 1:
        #    text='bvbb'
            canvas.delete("some_tag")
            showText(text)

        def showText(text):
            global label
            canvas.create_text(700, 280, text=text, font=("Comic Sans MS", 20, "bold"),fill="black", tag="some_tag")
        def listen():
           return run()


        # botonIngreso = Button(self.root,text="INICIO",background="aquamarine2",width=10,height=2, font=("Comic Sans MS", 15, "bold"),command=inicio).place(x=900,y=550)
        self.loadimage = PhotoImage(file="boton-click-aqui.png")
        self.roundedbutton = Button(self.root, image=self.loadimage, command=inicio).place(x=900,y=550)
       
root = Tk()
obj = ventana(root)
root.mainloop()




#botonLista = Button(ventana,text="Llamar a lista",background="aquamarine2",width=20,height=3,font=("Comic Sans MS", 9, "bold")).place(x=325,y=280)
#botonReporte = Button(ventana,text="Generar Reporte",background="aquamarine2",width=20,height=3,font=("Comic Sans MS", 9, "bold")).place(x=550,y=280)
