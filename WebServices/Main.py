import requests

print("⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔")

pokemon_name = input("Pokemon favorito: ")
hero_name = input("Heroe favorito: ")
city_name = input("Ciudad: ")

print("\n--- RESULTADOS ---\n")

# POKEMON
try:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()

        print("=== POKEMON ===")
        print(f"Nombre: {data['name']}")
        print(f"Altura: {data['height']}")
        print(f"Peso: {data['weight']}")

        # imagen
        img_url = data['sprites']['front_default']
        print(f"Imagen: {img_url}")

        img = requests.get(img_url)
        with open(f"{pokemon_name}.png", "wb") as f:
            f.write(img.content)

        print("Imagen descargada ✔")
    else:
        print("   Pokemon no encontrado")

except:
    print(" Pokemon error")


print("\n")

# HEROE
try:
    url = f"https://superheroapi.com/api/7252591128153666/search/{hero_name}"
    res = requests.get(url)
    data = res.json()

    if data["response"] == "success":
        h = data["results"][0]

        print("=== HEROE ===")
        print(f"Nombre: {h['name']}")
        print(f"Inteligencia: {h['powerstats']['intelligence']}")
        print(f"Fuerza: {h['powerstats']['strength']}")
        print(f"Velocidad: {h['powerstats']['speed']}")
    else:
        print("❌ Heroe no encontrado")

except:
    print("❌ Heroe error")


print("\n")

# CLIMA
try:
    url = f"https://wttr.in/{city_name}?format=j1"
    res = requests.get(url)
    data = res.json()

    temp = data["current_condition"][0]["temp_C"]
    desc = data["current_condition"][0]["weatherDesc"][0]["value"]

    print("=== CLIMA ===")
    print(f"Ciudad: {city_name}")
    print(f"Temperatura: {temp}°C")
    print(f"Clima: {desc}")

except:
    print(" Ciudad no encontrada")