from tkinter import *
from pytube import YouTube
from tkinter import ttk
from tkinter import filedialog
import threading
import re

# Función para iniciar la descarga en un hilo separado
def start_download():
    threading.Thread(target=Downloader).start()

# Función para actualizar la barra de progreso
def update_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = (bytes_downloaded / total_size) * 100
    progress_var.set(percentage_completed)
    bar_progresiva.update()

# Función para seleccionar la carpeta de destino
def select_folder():
    folder = filedialog.askdirectory()
    folder_var.set(folder)

# Función para manejar la descarga
def Downloader():
    try:
        # Parches manuales para el manejo de throttling
        url = YouTube(str(link.get()), on_progress_callback=update_progress)
        video = url.streams.get_highest_resolution()
        destination = folder_var.get() if folder_var.get() else '.'
        video.download(output_path=destination)
        Label(root, text='DESCARGADO', font='arial 13 bold', bg='#CD5C5C', fg='#9B0E0E').place(x=200, y=220)
        link.set("")  # Resetea el campo del enlace
    except Exception as e:
        Label(root, text=f'ERROR: {e}', font='arial 13 bold', bg='#CD5C5C', fg='#9B0E0E').place(x=200, y=220)
    finally:
        progress_var.set(0)  # Resetea la barra de progreso

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('Tu propio downloader de YouTube by DJ')
root.configure(bg='#3E3E3E')

Label(root, text='Pega el enlace aquí:', font='arial 20 bold', bg='#666666').place(x=90, y=30)

link = StringVar()
folder_var = StringVar()

Entradalink = Entry(root, width=70, textvariable=link)
Entradalink.place(x=32, y=90)

Label(root, text="Carpeta de destino:", font='arial 15', bg='#666666').place(x=32, y=130)
Button(root, text='Seleccionar Carpeta', font='arial 10 bold', bg='#CD5C5C', padx=2, command=select_folder).place(x=300, y=130)
folder_display = Label(root, textvariable=folder_var, font='arial 10', bg='#666666')
folder_display.place(x=32, y=160)

progress_var = DoubleVar()
bar_progresiva = ttk.Progressbar(root, variable=progress_var, maximum=100)
bar_progresiva.place(x=32, y=190, width=400)

Button(root, text='DESCARGAR', font='arial 13 bold italic', bg='#CD5C5C', padx=2, command=start_download).place(x=32, y=220)

root.mainloop()
