from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox

def accion():
    enlace = videos.get()
    try:
        video = YouTube(enlace)
        descarga = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        descarga.download()
        MessageBox.showinfo("Descarga completada", "El video ha sido descargado con éxito, para convertirlo en mp3, esta este link, escribilo al pie de la letra https://www.freeconvert.com/es/mp4-to-mp3")
    except Exception as e:
        MessageBox.showerror("Error", str(e))

def popup():
    MessageBox.showinfo("Sobre mi", "Ghost, enlace de Instagram:\nhttps://www.instagram.com/ghost_007_23")

root = Tk()
root.config(bd=15)
root.title("Script descargar videos")

imagen = PhotoImage(file="yt.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Más Información", menu=helpmenu)
helpmenu.add_command(label="Info del Autor", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

instrucciones = Label(root, text="Pega la url del video de YouTube y descargalo\n")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)

root.mainloop()