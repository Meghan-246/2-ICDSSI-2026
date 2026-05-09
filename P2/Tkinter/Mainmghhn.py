"""
Nombre : Meghan Lopez Peña
Grupo : 2I
Fecha : 24/03/26
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
from PIL import Image, ImageTk

#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔
# COLORES 
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔

bg_color = "#fff0f5"
card_color = "#ffffff"
accent = "#fb6bb3"
btn_color = "#ffc0cb"

root = tk.Tk()
root.title("Student Manager 💗")
root.geometry("800x650")
root.configure(bg=bg_color)

data = []
ruta_imagen = ""

#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔
# FUNCIONES 
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔

def abrir_archivo():
    global data
    ruta = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if not ruta:
        return

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
        cargar_tabla()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def cargar_tabla():
    for fila in tabla.get_children():
        tabla.delete(fila)

    for alumno in sorted(data, key=lambda x: x["name"].lower()):
        tabla.insert("", "end", values=(
            alumno["name"],
            alumno["email"],
            alumno["exa"],
            alumno["calif"]
        ))

def seleccionar(event):
    item = tabla.focus()
    valores = tabla.item(item, "values")

    if valores:
        nombre = valores[0]

        name_var.set(valores[0])
        email_var.set(valores[1])
        exa_var.set(valores[2])
        calif_var.set(valores[3])

        gender_var.set("")
        age_var.set("")

        for alumno in data:
            if alumno["name"] == nombre:
                if alumno.get("gender") == "Male":
                    gender_var.set("Male")
                elif alumno.get("gender") == "Female":
                    gender_var.set("Female")

                age_var.set(alumno.get("age", ""))

def subir_imagen():
    global ruta_imagen, img_tk
    ruta_imagen = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png *.jpg *.jpeg")])

    if ruta_imagen:
        img = Image.open(ruta_imagen)
        img = img.resize((120, 120))
        img_tk = ImageTk.PhotoImage(img)
        label_img.config(image=img_tk)

#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔
#  PROMEDIO
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔

def calcular_promedio():
    try:
        exa = float(exa_var.get())
        calif = float(calif_var.get())
        return round((exa + calif) / 2, 2)
    except:
        return "Error"

#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔
#  RESULTADOS
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔

def generar():
    ventana = tk.Toplevel(root)
    ventana.title("Resultados 💖")
    ventana.geometry("320x450")
    ventana.configure(bg=bg_color)

    promedio = calcular_promedio()

    info = f"""
Name: {name_var.get()}
Age: {age_var.get()}
Email: {email_var.get()}
Exa: {exa_var.get()}
Calif: {calif_var.get()}
Promedio: {promedio} ⭐
Gender: {gender_var.get()}
Occupation: {occ_var.get()}
"""

    tk.Label(ventana, text=info, bg=bg_color,
             font=("Helvetica", 12), justify="left").pack(pady=10)

    if ruta_imagen:
        img = Image.open(ruta_imagen)
        img = img.resize((150,150))
        img_tk2 = ImageTk.PhotoImage(img)

        label = tk.Label(ventana, image=img_tk2, bg=bg_color)
        label.image = img_tk2
        label.pack()

#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔
#  VARIABLES 
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔

name_var = tk.StringVar()
email_var = tk.StringVar()
exa_var = tk.StringVar()
calif_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
c1 = tk.IntVar()
c2 = tk.IntVar()
occ_var = tk.StringVar()

#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔
# TÍTULO 
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔

tk.Label(root, text="Student Manager 💗", bg=bg_color, fg=accent,
         font=("Helvetica", 22, "bold")).pack(pady=10)

#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔
#  BOTÓN 
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔

tk.Button(root, text="Open JSON File 💾", bg=btn_color,
          font=("Helvetica", 12), command=abrir_archivo).pack(pady=10)

#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔
# TABLA 
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔

tabla = ttk.Treeview(root, columns=("Name","Email","Exa","Calif"), show="headings")
for col in ("Name","Email","Exa","Calif"):
    tabla.heading(col, text=col)

tabla.pack(pady=10, fill="x", padx=30)
tabla.bind("<<TreeviewSelect>>", seleccionar)

#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔
# FORM 
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔

form = tk.Frame(root, bg=card_color)
form.pack(pady=15, padx=30, fill="both", expand=True)

def label(text, r):
    tk.Label(form, text=text, bg=card_color,
             font=("Helvetica", 12)).grid(row=r, column=0, padx=10, pady=8, sticky="w")

def entry(var, r):
    tk.Entry(form, textvariable=var,
             font=("Helvetica", 12)).grid(row=r, column=1)

label("Name", 0); entry(name_var, 0)
label("Age", 1); entry(age_var, 1)

label("Gender", 2)
gframe = tk.Frame(form, bg=card_color)
gframe.grid(row=2, column=1)
tk.Radiobutton(gframe, text="Male", variable=gender_var,
               value="Male", bg=card_color).pack(side="left")
tk.Radiobutton(gframe, text="Female", variable=gender_var,
               value="Female", bg=card_color).pack(side="left")

label("Email", 3); entry(email_var, 3)
label("Exa", 4); entry(exa_var, 4)
label("Calif", 5); entry(calif_var, 5)

label("Occupation", 6)
ttk.Combobox(form, textvariable=occ_var,
             values=["Student","Engineer","Doctor"]).grid(row=6, column=1)

#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔
# Imagen
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔

label_img = tk.Label(form, bg=card_color)
label_img.grid(row=0, column=2, rowspan=4, padx=20)

tk.Button(form, text="Upload Image 📷", bg=btn_color,
          command=subir_imagen).grid(row=4, column=2)
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔
# Botón final
#⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔

tk.Button(root, text="Generate Results 💖", bg=accent, fg="white",
          font=("Helvetica", 13, "bold"),
          command=generar).pack(pady=15)

root.mainloop()