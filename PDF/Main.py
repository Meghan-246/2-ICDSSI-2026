from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import json

# Crear PDF
pdf = SimpleDocTemplate("students.pdf", pagesize=letter)

# Estilos de texto
styles = getSampleStyleSheet()
title = Paragraph("Lista de Alumnos - CBTis 246", styles['Title'])

# Leer JSON
with open("Students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

# Encabezados
data = [["Nombre", "Email", "Exa", "Calif"]]

# Llenar tabla con datos
for s in students:
    data.append([
        s["name"],
        s["email"],
        s["exa"],
        s["calif"]
    ])

# Crear tabla
table = Table(data, repeatRows=1)

# Estilo bonito
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),

    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),

    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),

    ('GRID', (0, 0), (-1, -1), 1, colors.black)
])

table.setStyle(style)

# Elementos del PDF
elements = []
elements.append(title)
elements.append(Spacer(1, 20))
elements.append(table)

# Construir PDF
pdf.build(elements)

print("PDF generado correctamente 💅")