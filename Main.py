#Librerias GUI
import tkinter 
from  tkinter import ttk
from tkinter import *

#Mis Modulos
from BaseDatos import BaseDatos


def iniciarVentana():
    ancho=500
    alto=500
    tamanioVentana=str(ancho)+"x"+str(alto)
    ventana=Tk()
    ventana.geometry(tamanioVentana)
    ventana.title("MongoDB")
    ventana['bg'] = '#484644'

    notebook=ttk.Notebook(ventana)
    notebook.pack(expand=True)
    ventana1=ttk.Frame(notebook, width=ancho, height=alto,)
    ventana1.pack(fill='both', expand=True)
    ventana2=ttk.Frame(notebook, width=ancho, height=alto)
    ventana2.pack(fill='both', expand=True)
    notebook.add(ventana1,text="Inicio")
    notebook.add(ventana2,text="Registro")

    etiquetaTitulo = Label(ventana1, text="Login MongoDB")
    etiquetaTitulo.pack(fill="x",side="top")
    etiquetaTitulo.config(fg="white",  bg="#0c2145", font=("Roboto",30),anchor="nw") 

    etiquetaTitulo2 = Label(ventana2, text="Registro MongoDB")
    etiquetaTitulo2.place(x=0,y=0)
    etiquetaTitulo2.config(fg="white",  bg="#0c2145", font=("Roboto",30),anchor="nw") 
     
    etiquetaUsuario =Label(ventana1, text="Usuario")
    etiquetaUsuario.place(x=(ancho/3)-100, y=alto/3)
    etiquetaUsuario.config(font=("Verdana",10)) 
    
    etiquetaContra = Label(ventana1, text="Contraseña")
    etiquetaContra.place(x=(ancho/3)-100, y=(alto/3)+30)
    etiquetaContra.config(font=("Verdana",10)) 

    etiquetaUsuario= Label(ventana1, text="Ingreso")  
    etiquetaUsuarioInc = Label(ventana1, text="Usuario o Contraseña Incorrecto")

    etiquetaUsuarioExt = Label(ventana2, text="Usuario Existente")
    etiquetaUsuarioNoExt = Label(ventana2, text="Registro Correcto")

    etiquetaRegUsuario =Label(ventana2, text="Usuario")
    etiquetaRegUsuario.place(x=(ancho/3)-100, y=alto/3)
    etiquetaRegUsuario.config(font=("Verdana",10)) 
    
    etiquetaRegContra = Label(ventana2, text="Contraseña")
    etiquetaRegContra.place(x=(ancho/3)-100, y=(alto/3)+30)
    etiquetaRegContra.config(font=("Verdana",10))   

    def tomarDatos():  
        usuario=cajaTextoUsuario.get(1.0, tkinter.END+"-1c") 
        contra=cajaTextoContra.get(1.0, tkinter.END+"-1c")
        validarUsuario=objetoBD.validarUsuario(str(usuario),str(contra))
        etiquetaUsuario.place_forget()
        etiquetaUsuarioInc.place_forget()

        if validarUsuario:
            etiquetaUsuario.place(x=(ancho/3), y=(alto/3)+100)
            etiquetaUsuario.config(fg="green", font=("Verdana",10)) 
        else: 
            etiquetaUsuarioInc.place(x=(ancho/3), y=(alto/3)+100)
            etiquetaUsuarioInc.config(fg="red", font=("Verdana",10)) 

    def mostrarUsuarios():
        usuarios=objetoBD.getUsuarios()
        etiquetaMost=Label(ventana1, text="Usuarios Registrados")   
        etiquetaMost.place(x=(ancho/3)-100, y=((alto/3)+180)) 
        etiquetaMost.config(font=("Verdana",10))
        etiqueta=Label(ventana1, text=usuarios)   
        etiqueta.place(x=(ancho/3)-100, y=((alto/3)+200)) 
        etiqueta.config(font=("Verdana",10))    
    
    def registrar():
        etiquetaUsuarioExt.place_forget()
        etiquetaUsuarioNoExt.place_forget()
        usuario=cajaTextoRegUsuario.get(1.0, tkinter.END+"-1c") 
        contra=cajaTextoRegContra.get(1.0, tkinter.END+"-1c")
        validarUsuario=objetoBD.validarNombreUsuario(str(usuario))      
        if validarUsuario:  
            etiquetaUsuarioExt.place(x=(ancho/3), y=(alto/3)+100)
            etiquetaUsuarioExt.config(fg="red", font=("Verdana",10)) 
        else:
            etiquetaUsuarioNoExt.place(x=(ancho/3), y=(alto/3)+100)
            etiquetaUsuarioNoExt.config(fg="green", font=("Verdana",10)) 
            objetoBD.setUsuario(str(usuario),str(contra))

    cajaTextoRegUsuario =Text(ventana2,width=20,height=1)
    cajaTextoRegUsuario.place(x=ancho/2, y=alto/3)
    cajaTextoRegContra =Text(ventana2,width=20,height=1)
    cajaTextoRegContra.place(x=ancho/2, y=(alto/3)+30)  

    
    cajaTextoUsuario =Text(ventana1,width=20,height=1)
    cajaTextoUsuario.place(x=ancho/2, y=alto/3)
    cajaTextoContra =Text(ventana1,width=20,height=1)
    cajaTextoContra.place(x=ancho/2, y=(alto/3)+30)
    
    botonAceptar=Button(ventana1,text="Aceptar",command=tomarDatos, bg="#0c2145",fg="white",activebackground="red").place(x=(ancho/2), y=(alto/3)+60)
    botonMostrarUsuarios=Button(ventana1,text="Mostrar Usuarios",command=mostrarUsuarios, bg="#0c2145",fg="white",activebackground="red").place(x=(ancho/3)-100, y=(alto/3)+150)
    botonRegUsuarios=Button(ventana2,text="Registrar",command=registrar, bg="#0c2145",fg="white",activebackground="red").place(x=(ancho/3)-100, y=(alto/3)+150)
    ventana.mainloop()


if __name__=="__main__":
    objetoBD=BaseDatos()
    iniciarVentana()