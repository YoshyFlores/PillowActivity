# Create project with: Tkiner, Pillow

from tkinter import Button, Label, Tk, messagebox, filedialog, simpledialog
from PIL import Image, ImageTk, ImageFilter

# Variables
root = Tk()

# Settings for the window
root.title("Photo App")
# Size of the window
root.geometry("500x500")
# Center the window
root.eval('tk::PlaceWindow . center')
# Disable resize
root.resizable(False, False)
#Color of the window
root.config(bg="#72BBAE")

#Funcion de la seleccion de imagen
def selectImage():
    
    global loadImage
    loadImage = filedialog.askopenfilename()
    image = Image.open(loadImage)

    # Open the image in label
    renderImage = ImageTk.PhotoImage(
        image.resize((300, 300), Image.Resampling.LANCZOS))

    labelImage.configure(image=renderImage)
    labelImage.image = renderImage


def setImage():
    
    try:
        image = Image.open(loadImage)
    except:
        messagebox.showerror("Error", "Please select an image first")
    return image


#Funcion de conversion a Black and White
def convertBlackAndWhite():
    message = messagebox.showinfo("Info", "This will convert the image to black and white")
    
    imageBN = setImage().convert("L")

    # nameImage = simpledialog.askstring("Input", "Name to save the image", parent=root)
    imageBN.save("blackandwhite.jpg")
    imageBN.show()

#Funcion para la generación de la imagen en Blur 
def generateBlur():
    
    message = messagebox.showinfo("Info", "This will blur the image")

    imageBlur = setImage().filter(ImageFilter.GaussianBlur(25))
    imageBlur.save("blur.jpg")
    imageBlur.show()


#Funcion para generar la imagen en Outline
def generateOutline():
    
    message = messagebox.showinfo("Info", "This will outline the image")

    imageOutline = setImage().filter(ImageFilter.FIND_EDGES)
    imageOutline.save("outline.jpg")
    imageOutline.show()


#Función para generar la imagen en HighLight
def generateHighLight():
    
    message = messagebox.showinfo("Info", "This will highlight the image")
    
    imageHighLight = setImage().filter(ImageFilter.EMBOSS)
    imageHighLight.save("highlight.jpg")
    imageHighLight.show()

#Procedemos a asignar el texto tanto de los labels como de los botones
#Asignamos color 
labelImage = Label(root, text="Temporary Image")

buttonSelectImage = Button(root, text="Select Image", command=selectImage, bg="#91B6EE")

buttonConvertBlackWhite = Button(root, text="Convert to Black and White", command=convertBlackAndWhite, bg="#91B6EE")

buttonBlurImage = Button(root, text="Blur Image", command=generateBlur, bg="#91B6EE")

buttonOutline = Button(root, text="Outline", command=generateOutline, bg="#91B6EE")

buttonHighLight = Button(root, text="Highlight", command=generateHighLight, bg="#91B6EE")


# Order of the widgets
#Detenerminamos el espacio que tendran entre botones y labels.
labelImage.pack(padx=(0,0), pady=(20,0))

buttonSelectImage.pack(padx=(0,0), pady=(20,0))

buttonConvertBlackWhite.pack(padx=(0,0), pady=(20,0))

buttonBlurImage.pack(padx=(0,0), pady=(20,0))

buttonOutline.pack(padx=(0,0), pady=(20,0))

buttonHighLight.pack(padx=(0,0), pady=(20,0))

# Window app
root.mainloop()
