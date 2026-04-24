import itertools
from random import randint
from statistics import mean

from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

"""
win
python -m venv .venv
mac/linux
python3 -m venv .venv
Yo must install reportlab with this command:
pip install reportlab
or
pip3 install reportlab
"""

class MyFirstPDF:

    def grouper(self, iterable, n):
        args = [iter(iterable)] * n
        return itertools.zip_longest(*args)


    def export_to_pdf(self, data):
        c = canvas.Canvas("grilla-alumnos.pdf", pagesize=LETTER)
        w, h = LETTER
        max_rows_per_page = 45
        # Margin.
        x_offset = 50
        y_offset = 50
        # Space between rows.
        padding = 15
        
        xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
        
        for rows in self.grouper(data, max_rows_per_page):
            rows = tuple(filter(bool, rows))
            c.grid(xlist, ylist[:len(rows) + 1])
            for y, row in zip(ylist[:-1], rows):
                for x, cell in zip(xlist, row):
                    c.drawString(x + 2, y - padding + 3, str(cell))
            c.showPage()
        
        c.save()


data = [("NOMBRE", "NOTA 1", "NOTA 2", "NOTA 3", "PROM.", "ESTADO")]
for i in range(1, 101):
    exams = [randint(0, 10) for _ in range(3)]
    avg = round(mean(exams), 2)
    state = "Aprobado" if avg >= 4 else "Desaprobado"
    data.append((f"Alumno {i}", *exams, avg, state))


my_pdf = MyFirstPDF()
my_pdf.export_to_pdf(data)
