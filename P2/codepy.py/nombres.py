"""
Nombre : Meghan Lopez Peña
Grupo : 2I
Fecha : 18/03/26
"""

import json
import xml.etree.ElementTree as ET

#────୨ৎ────
# USER
#────୨ৎ────
class User:
    def __init__(self, name, email, exam, note, grade, group, shift):
        self.name = name
        self.email = email
        self.exam = exam
        self.note = note
        self.grade = grade
        self.group = group
        self.shift = shift

# ────୨ৎ────
# MAIN PROGRAM
# ────୨ৎ────
class MainProgram:

    def obj_dict(self, obj):
        return obj.__dict__

    def object_to_json(self, obj):
        json_pretty = json.dumps(obj, default=self.obj_dict, indent=4)
        print(json_pretty)

    def object_to_xml(self, obj):
        root = ET.Element("User")
        for key, value in obj.__dict__.items():
            ET.SubElement(root, key).text = str(value)
        print(ET.tostring(root, encoding='unicode'))

    #  obtener apellidos para ordenar
    def get_last_names(self, name):
        parts = name.strip().lower().split()
        if len(parts) >= 2:
            return parts[-2] + " " + parts[-1]
        return parts[-1]

    # crear dataset desde lista de datos
    def create_dataset(self, data_lines):
        students = []
        for i, line in enumerate(data_lines):
            if i == 0:
                continue  # saltar encabezado

            parts = line.split("|")
            user = User(
                parts[0].strip(),  # nombre completo
                parts[1].strip(),
                parts[2].strip(),
                parts[3].strip(),
                "2",
                "I",
                "V"
            )
            students.append(user)

        # ordenar por apellido 
        return sorted(students, key=lambda u: self.get_last_names(u.name))


# ────୨ৎ────
# DATOS
# ────୨ৎ────
data_lines = [
    "Name                                 |email                                      |exa|calif|grado|grupo|turno |",
    "david alejandro franco garcia        |david.franco.2025.tmp@mit.edu              |  5|    1|     |     |      |",
    "Julissa Espinosa Luna                |julissa.espinosa.2025.tmp@mit.edu          |  0|    0|     |     |      |",
    "sebastian ponce delgado              |sebastian.ponce.2025.tmp@mit.edu           |  5|    1|     |     |      |",
    "maximo dante sandoval delgado        |maximo.sandoval.2025.tmp@mit.edu           |  6|    3|     |     |      |",
    "victoria ramirez martinez            |victoria.ramirez.2025.tmp@mit.edu          |  4|    3|     |     |      |",
    "Miguel Angel Corrales Iñiguez        |miguel.corrales.2025.tmp@mit.edu           |  5|    1|     |     |      |",
    "Zoe Fernanda Garcia López            |zoe.garcia.2025.tmp@mit.edu                |  4|    2|     |     |      |",
    "Joshua Asael Ramirez Cuellar         |joshua.ramirez.2025.tmp@mit.edu            |  3|    6|     |     |      |",
    "Luis Manuel Rodriguez Rodriguez      |luis.rodriguez.2025.tmp@mit.edu            |  5|    3|     |     |      |",
    "Cesar Omar Enriquez Aguilar          |cesar.enriquez.2025.tmp@mit.edu            |  4|    1|     |     |      |",
    "Juan Diedo Vargas Villegas           |juan.vargas.2025.tmp@mit.edu               |  4|    2|     |     |      |",
    "Yoel Rodriguez Valdenegro            |yoel.rodriguez.2025.tmp@mit.edu            |  3|    1|     |     |      |",
    "alondra yanin martinez reygadas      |alondra.martinez.2025.tmp@mit.edu          |  5|    1|     |     |      |",
    "yurem alejandro rodriguez sanchez    |yurem.rodriguez.2025.tmp@mit.edu           |  6|    5|     |     |      |",
    "Rubén Luquin Sánchez                 |ruben.luquin.2025.tmp@mit.edu              |  7|    6|     |     |      |",
    "Angel Antonio Cazares Nuñez          |angel.cazares.2025.tmp@mit.edu             |  4|    1|     |     |      |",
    "Meghan Lopez Peña                    |meghan.lopez.2025.tmp@mit.edu              | 10|   10|     |     |      |",
    "Dayana Ivonne Alcala Neri            |dayana.alcala.2025.tmp@mit.edu             |  3|    6|     |     |      |",
    "angel geovanni sanchez de la cruz    |angel.sanchez.2025.tmp@mit.edu             |  6|    1|     |     |      |",
    "diego alfonso lopez rodriguez        |diego.lopez.2025.tmp@mit.edu               |  6|    1|     |     |      |",
    "Miriam Daniela Barajas Marin         |miriam.barajas.2025.tmp@mit.edu            |  4|    1|     |     |      |",
    "Diego Montiel Cabrera                |diego.montiel.2025.tmp@mit.edu             |  6|    3|     |     |      |",
    "Gael Santiago Carrillo Castillo      |gael.carrillo.2025.tmp@mit.edu             |  1|    8|     |     |      |",
    "Dulce Anahi Alcala Neri              |dulce.alcala.2025.tmp@mit.edu              |  5|    2|     |     |      |",
    "alexa xiadany martinez talavera      |alexa.martinez.2025.tmp@mit.edu            |  4|    1|     |     |      |",
    "Diego Perez Melesio                  |diego.perez.2025.tmp@mit.edu               |  5|    9|     |     |      |",
    "Eduardo Tadeo Valenzuela Villa       |eduardo.valenzuela.2025.tmp@mit.edu        |  5|    4|     |     |      |",
    "Angel Santiago Coronel Hernández     |angel.coronel.2025.tmp@mit.edu             |  5|    4|     |     |      |",
    "Emily Sandoval Madero                |emily.sandoval.2025.tmp@mit.edu            |  6|    9|     |     |      |",
    "OSCAR EDUARDO SANDOVAL VIZCAINO      |sandoval.oscar.2024.tmp@mit.edu            |  0|    0|     |     |      |",
    "jesus mateo reyes barron             |jesus.reyes.2025.tmp@mit.edu               |  0|    0|     |     |      |",
    "carlos adrian murillo ramos          |carlos.murillo.2025.tmp@mit.edu            |  0|    0|     |     |      |"
]

# ────୨ৎ────
# EJECUCIÓN
# ────୨ৎ────
main = MainProgram()
users = main.create_dataset(data_lines)

print("\n===== JSON =====")
main.object_to_json(users)

print("\n===== XML (primeros 5) =====")
for u in users[:5]:
    main.object_to_xml(u)