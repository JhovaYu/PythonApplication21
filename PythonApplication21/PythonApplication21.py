#importamos la libreria de Tkinter
import tkinter as tk

#Cramos nuestra función "reset" que nos ayudara a reiniciar nuestra 
#app a valores por defecto
def reset():
    entry1.delete(0, tk.END)
    #Elimina el contenido que coloquemos posteriormente en el campo
    #de Fahrenheit
    entry1.insert(0, "0.0")
    #Estable los valores dentro del campo Fahrenheit en 0.0
    entry2.delete(0, tk.END)
    #Realiza lo mismo que entry1.delete solo que modifica el campo de
    #Celsius
    entry2.insert(0, "0.0")
    #De mismo modo solo modifica el campo de Celsius estableciendolo 
    #en 0.0
    
#Definicimos nuestra segunda función que convertira Celsius a 
#grados Fahrenheit    
def convert_to_fahrenheit():
    #Utilizamos el metodo .get para obtener el valor inscrito en 
    #el campo de Celsius
    celsius = float(entry2.get())
    #Utilizamos la formula para convertir de Celsius a Fahrenheit 
    fahrenheit = (celsius * 9 / 5) + 32
    #Borramos el contenido en el campo de Fahrenheit
    entry1.delete(0, tk.END)
    #Inserta el resultado obtenido en el campo Fahrenheit con dos 
    #decimales
    entry1.insert(0, f"{fahrenheit:.2f}")

#Creamos nuestra funcion que convierte de Fahrenheit a Celsius
def convert_to_celsius():
    #Tomamos los datos insertados en el campo de Fahrenheit
    fahrenheit = float(entry1.get())
    #Utilizamos la formula de conversión
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    #Borramos lo escrito en el campo de Celsius
    entry2.delete(0, tk.END)
    #Insertamos el resultado en Celsius
    entry2.insert(0, f"{celsius:.2f}")

#Utiliza la funcion de Tkinter para crear una ventana
app = tk.Tk()  
#Se establece el nombre de la app
app.title("Conversor de Temperatura")

#Crear un label con el texto dentro "Fahrenheit:"
label1 = tk.Label(app, text="Fahrenheit:")
#Lo coloca dentro del grid en la posición 0,0
label1.grid(row=0, column=0)

#Crear el equivalente a un TextBox para que se puedan ingresar datos
entry1 = tk.Entry(app)
#Posicinamos el TB en el Grid
entry1.grid(row=0, column=1)

#Crea un boton con el titulo "Convertir a Celsius" que al ser presionado
#ejecuta la funcion convert_to_celsius
button1 = tk.Button(app, text="Convertir a Celsius", command=convert_to_celsius)
#Lo posicionamos en el Grid
button1.grid(row=0, column=2)

#Creamos una segunda etiqueta
label2 = tk.Label(app, text="Celsius:")
#La posicionamos
label2.grid(row=1, column=0)

#Creamos otro TB 
entry2 = tk.Entry(app)
#La posicionamos
entry2.grid(row=1, column=1)

#Creamos el segundo boton que ejecuta la funcion de convert_to_fahrenheit
button2 = tk.Button(app, text="Convertir a Fahrenheit", command=convert_to_fahrenheit)
#La posicionamos
button2.grid(row=1, column=2)

#Creamos un tercer boton que ejecutara la funcion reset y limpiara los TB
button3 = tk.Button(app, text="Restablecer", command=reset)
#Lo poscionamos en el Grid
button3.grid(row=2, column=1)

#Inicia la app en bucle que espera a una accion para realizar una tarea
app.mainloop()


