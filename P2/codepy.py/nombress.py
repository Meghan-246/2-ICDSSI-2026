"""
Nombre : Meghan Lopez Peña
Grupo : 2I
Fecha : 18/03/26
"""
from Student import User

import json
import xml.etree.ElementTree as ET



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

    def get_last_names(self, name):
        parts = name.strip().lower().split()
        if len(parts) >= 2:
            return parts[-2] + " " + parts[-1]
        return parts[-1]

    def create_dataset(self, data_lines):
        students = []
        for i, line in enumerate(data_lines):
            if i == 0:
                continue

            parts = line.split("|")
            user = User(
                parts[0].strip(),
                parts[1].strip(),
                parts[2].strip(),
                parts[3].strip(),
                "2",
                "I",
                "V"
            )
            students.append(user)

        return sorted(students, key=lambda u: self.get_last_names(u.name))

    #guardar JSON
    def save_json(self, users):
        with open("students.json", "w", encoding="utf-8") as f:
            json.dump(users, f, default=self.obj_dict, indent=4, ensure_ascii=False)

    #guardar XML
    def save_xml(self, users):
        root = ET.Element("students")
        for u in users:
            user_elem = ET.SubElement(root, "user")
            for key, value in u.__dict__.items():
                ET.SubElement(user_elem, key).text = str(value)

        tree = ET.ElementTree(root)
        tree.write("students.xml", encoding="utf-8", xml_declaration=True)

    # guardar CSV
    def save_csv(self, users):
        with open("students.csv", "w", encoding="utf-8") as f:
            f.write("name,email,exam,note,grade,group,shift\n")
            for u in users:
                f.write(f"{u.name},{u.email},{u.exam},{u.note},{u.grade},{u.group},{u.shift}\n")

    # guardar INI
    def save_ini(self, users):
        with open("students.ini", "w", encoding="utf-8") as f:
            for i, u in enumerate(users):
                f.write(f"[student{i}]\n")
                for key, value in u.__dict__.items():
                    f.write(f"{key}={value}\n")
                f.write("\n")

    #guardar YAML
    def save_yaml(self, users):
        with open("students.yaml", "w", encoding="utf-8") as f:
            i=0
            for u in users:
                i+=1
                f.write(f"- id {i}\n")
                for key, value in u.__dict__.items():
                    f.write(f"  {key}: {value}\n")


# ────୨ৎ────
# DATOS COMPLETOS
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

# CREAR ARCHIVOS
main.save_json(users)
main.save_xml(users)
main.save_csv(users)
main.save_ini(users)
main.save_yaml(users)

print("\n Archivos creados correctamente")
