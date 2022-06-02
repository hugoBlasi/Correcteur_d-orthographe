from tkinter import *
from tkinter import filedialog
import Main


mainapp = Tk()

mainapp.title("Molière 100")
mainapp.geometry("1000x600")
mainapp.configure(bg = "#9e9e9e")

def getText() : 
    res = entry0.get("1.0","end")
    return(res)

def open_txt() :
    text_file = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ))
    text_file = open(text_file, 'r' )
    stuff = text_file.read()

    entry0.insert(END,stuff)
    text_file.close()

canvas = Canvas(
    mainapp,
    bg = "#9e9e9e",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"image/background.png")
background = canvas.create_image(
    522.0, 293.0,
    image=background_img)

entry0 = Text(mainapp ,bg = "#c4c4c4", font = ("Helvetica", 10))
entry0.pack()
entry0.place(x= 30,y= 204 ,w= 407, h= 219)


img0 = PhotoImage(file = f"image/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :Main.Moliere(getText(),l_Nerror,l_Showerror,l_error,l_Pcorrection,l_correction,l_note),
    relief = "flat")

b0.place(
    x = 249, y = 480,
    width = 181,
    height = 53)

img1 = PhotoImage(file = f"image/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = open_txt,
    relief = "flat")

b1.place(
    x = 35, y = 438,
    width = 119,
    height = 43)

l_Nerror = Label(mainapp, text="",bg="#c4c4c4")
l_Showerror = Label(mainapp, text="",bg="#c4c4c4" )
l_error = Label(mainapp, text="",bg="#c4c4c4" )
l_Pcorrection = Label(mainapp, text="",bg="#c4c4c4" )
l_correction = Label(mainapp, text="",bg="#c4c4c4" )

l_Nerror.place(x=557, y=204, w=407, h=43.7)
l_Showerror.place(x=557, y=248, w=407, h=43.7)
l_error.place(x=557, y=292, w=407, h=43.7)
l_Pcorrection.place(x=557, y=336, w=407, h=43.7)
l_correction.place(x=557, y=380, w=407, h=43.7)

l_note = Label(mainapp, text="100",bg = "#9e9e9e",font = ("Oleo Script Swash Caps", 36))
l_note.place(x=668, y=499, w=92, h=54)

mainapp.resizable(False, False)
mainapp.mainloop()
