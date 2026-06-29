# =========================
# CARGAR CSV
# =========================
import os
import csv

def cargar_csv(nombre_archivo):
    ruta = os.path.join(os.path.dirname(__file__), "..", "datos", nombre_archivo)
    ruta = os.path.abspath(ruta)
    print("Ruta detectada:", ruta)  # solo para verificar
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)

def main():
    paises = cargar_csv("paises.csv")
    print(paises)

    


   


# =========================
# MOSTRAR
# =========================

def mostrar_paises(paises):
    if not paises:
        print("No hay países cargados.")
        return

    for pais in paises:
        print("Nombre:", pais["nombre"])
        print("Población:", pais["poblacion"])
        print("Superficie:", pais["superficie"])
        print("Continente:", pais["continente"])
        print("-------------------------")


# =========================
# AGREGAR
# =========================

def agregar_pais(paises):
    nombre = input("Nombre del país: ").strip()
    if nombre == "":
        print("Error: nombre vacío.")
        return

    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print("Ese país ya existe.")
            return

    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie: "))
    except ValueError:
        print("Error: debe ingresar números.")
        return

    continente = input("Continente: ").strip()

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)
    print("País agregado.")


# =========================
# ACTUALIZAR
# =========================

def actualizar_pais(paises):
    nombre = input("Nombre del país a actualizar: ").strip()

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            try:
                nueva_pob = int(input("Nueva población: "))
                nueva_sup = int(input("Nueva superficie: "))
            except ValueError:
                print("Error: números inválidos.")
                return

            pais["poblacion"] = nueva_pob
            pais["superficie"] = nueva_sup
            print("Datos actualizados.")
            return

    print("País no encontrado.")


# =========================
# BUSCAR
# =========================

def buscar_pais(paises):
    nombre = input("Buscar país: ").strip().lower()
    encontrado = False

    for pais in paises:
        if nombre in pais["nombre"].lower():
            print("Encontrado:", pais["nombre"])
            encontrado = True

    if not encontrado:
        print("No se encontró.")


# =========================
# FILTROS
# =========================

def filtrar_continente(paises):
    cont = input("Continente: ").strip().lower()
    encontrados = []

    for pais in paises:
        if cont in pais["continente"].lower():
            encontrados.append(pais)

    if not encontrados:
        print("No hay países en ese continente.")
    else:
        for p in encontrados:
            print(p["nombre"])


def filtrar_mayor_poblacion(paises):
    try:
        valor = int(input("Población mínima: "))
    except ValueError:
        print("Número inválido.")
        return

    for pais in paises:
        if pais["poblacion"] >= valor:
            print(pais["nombre"])


def filtrar_menor_poblacion(paises):
    try:
        valor = int(input("Población máxima: "))
    except ValueError:
        print("Número inválido.")
        return

    for pais in paises:
        if pais["poblacion"] <= valor:
            print(pais["nombre"])


# =========================
# ORDENAR
# =========================

def ordenar_paises(paises):
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    opcion = int(input("Opción: "))

    print("1. Ascendente")
    print("2. Descendente")
    orden = int(input("Orden: "))
    reverse = (orden == 2)

    if opcion == 1:
        clave = "nombre"
    elif opcion == 2:
        clave = "poblacion"
    elif opcion == 3:
        clave = "superficie"
    else:
        print("Opción inválida.")
        return

    ordenados = sorted(paises, key=lambda p: p[clave], reverse=reverse)

    for p in ordenados:
        print(p)


# =========================
# ESTADÍSTICAS
# =========================

def estadisticas(paises):
    if not paises:
        print("No hay datos.")
        return

    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])

    print("Mayor población:", mayor["nombre"])
    print("Menor población:", menor["nombre"])

    suma_pob = sum(p["poblacion"] for p in paises)
    suma_sup = sum(p["superficie"] for p in paises)

    print("Promedio población:", suma_pob / len(paises))
    print("Promedio superficie:", suma_sup / len(paises))

    continentes = {}
    for p in paises:
        c = p["continente"]
        continentes[c] = continentes.get(c, 0) + 1

    print("Países por continente:")
    for c, cant in continentes.items():
        print(c, ":", cant)


# =========================
# MENÚ
# =========================

def main():
    paises = cargar_csv("paises.csv")


    

    opcion = 0
    while opcion != 11:
        print("\n===== MENÚ =====")
        print("1. Cargar CSV")
        print("2. Mostrar países")
        print("3. Agregar país")
        print("4. Actualizar país")
        print("5. Buscar país")
        print("6. Filtrar por continente")
        print("7. Filtrar por mayor población")
        print("8. Filtrar por menor población")
        print("9. Ordenar países")
        print("10. Estadísticas")
        print("11. Salir")

        try:
            opcion = int(input("Opción: "))
        except ValueError:
            print("Debe ingresar un número.")
            continue

        if opcion == 1:
            paises = cargar_csv("paises.csv")
        elif opcion == 2:
            mostrar_paises(paises)
        elif opcion == 3:
            agregar_pais(paises)
        elif opcion == 4:
            actualizar_pais(paises)
        elif opcion == 5:
            buscar_pais(paises)
        elif opcion == 6:
            filtrar_continente(paises)
        elif opcion == 7:
            filtrar_mayor_poblacion(paises)
        elif opcion == 8:
            filtrar_menor_poblacion(paises)
        elif opcion == 9:
            ordenar_paises(paises)
        elif opcion == 10:
            estadisticas(paises)
        elif opcion == 11:
            print("Fin del programa.")


main()


