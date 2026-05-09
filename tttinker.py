import tkinter as tk
from tkinter import messagebox, filedialog
import json

ruta_json = ""

# Seleccionar archivo JSON
def seleccionar_json():
    global ruta_json
    ruta_json = filedialog.askopenfilename(
        title="Seleccionar archivo JSON",
        filetypes=[("Archivos JSON", "*.json")]
    )
    if ruta_json:
        label_archivo.config(text="Archivo cargado ✔")
    else:
        label_archivo.config(text="No se seleccionó archivo")

# Cargar datos del JSON
def cargar_datos():
    try:
        with open(ruta_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        messagebox.showerror("Error", "No se pudo cargar el archivo JSON")
        return []

# Verificar login
def verificar_login():
    if not ruta_json:
        messagebox.showwarning("Aviso", "Primero selecciona el archivo JSON")
        return

    usuario = entry_usuario.get()
    password = entry_password.get()
    
    estudiantes = cargar_datos()

    for est in estudiantes:
        # USAMOS email COMO USUARIO
        if est["email"] == usuario:
            if est["password"] == password:
                mostrar_datos(est)
                return
            else:
                messagebox.showerror("Error", "Contraseña incorrecta")
                return
    
    messagebox.showwarning("Aviso", "Usuario no existe, contacte al Administrador")

# Mostrar datos del estudiante
def mostrar_datos(est):
    info = f"""
Nombre: {est['name']}
Correo: {est['email']}
Contraseña: {est['password']}
Examen: {est['exam']}
Calificación: {est['note']}
Grado: {est['grade']}
Grupo: {est['group']}
Turno: {est['shift']}
"""
    messagebox.showinfo("Datos del Estudiante", info)

# Ventana principal
ventana = tk.Tk()
ventana.title("Login Tkinter")
ventana.geometry("350x300")

# Botón para seleccionar JSON
tk.Button(ventana, text="Seleccionar JSON", command=seleccionar_json).pack(pady=10)
label_archivo = tk.Label(ventana, text="No se ha cargado archivo")
label_archivo.pack()

# Campo usuario
tk.Label(ventana, text="Usuario (correo)").pack(pady=5)
entry_usuario = tk.Entry(ventana, width=30)
entry_usuario.pack()

# Campo contraseña
tk.Label(ventana, text="Contraseña").pack(pady=5)
entry_password = tk.Entry(ventana, show="*", width=30)
entry_password.pack()

# Botón entrar
tk.Button(ventana, text="Entrar", command=verificar_login).pack(pady=20)

ventana.mainloop()