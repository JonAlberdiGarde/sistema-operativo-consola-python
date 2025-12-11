import os
import sys
import time
import random
import json

# =========================
# Idiomas
# =========================
IDIOMAS = {
    "es": {
        "menu": "=== Python OS ===",
        "salir": "Salir",
        "calc": "Calculadora",
        "notas": "Notas",
        "hora": "Reloj",
        "egutegia": "Calendario",
        "paint": "Dibujos",
        "biderketak": "Multiplicaciones",
        "adivina": "Adivina el número",
        "capitales": "Capitales",
        "iritzia": "Opiniones",
        "acerca": "Acerca de",
        "enter": "Pulsa Enter para continuar..."
    },
    "eu": {
        "menu": "=== Python OS ===",
        "salir": "Irten",
        "calc": "Kalkulagailua",
        "notas": "Notak",
        "hora": "Ordularia",
        "egutegia": "Egutegia",
        "paint": "Marrazkiak",
        "biderketak": "Biderketak",
        "adivina": "Asmatu zenbakia",
        "capitales": "Capitalak",
        "iritzia": "Iritziak",
        "acerca": "Honi buruz",
        "enter": "Sakatu Enter jarraitzeko..."
    },
    "en": {
        "menu": "=== Python OS ===",
        "salir": "Exit",
        "calc": "Calculator",
        "notas": "Notes",
        "hora": "Clock",
        "egutegia": "Calendar",
        "paint": "Drawings",
        "biderketak": "Multiplications",
        "adivina": "Guess the number",
        "capitales": "Capitals",
        "iritzia": "Opinions",
        "acerca": "About",
        "enter": "Press Enter to continue..."
    }
}

idioma_actual = "es"

def t(clave):
    return IDIOMAS[idioma_actual].get(clave, clave)

def reset_json_files():
    guardar_datos("notas.json", [])
    guardar_datos("egutegia.json", [])
    guardar_datos("iritziak.json", [])
    guardar_datos("paint.json", [])

def seleccionar_idioma():
    global idioma_actual
    print("Selecciona idioma / Hautatu hizkuntza / Select language")
    print("1. Español\n2. Euskara\n3. English")
    opcion = input("> ")
    if opcion == "1":
        idioma_actual = "es"
    elif opcion == "2":
        idioma_actual = "eu"
    elif opcion == "3":
        idioma_actual = "en"
    else:
        idioma_actual = "es"

# =========================
# Utilidades
# =========================
def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def cargar_datos(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# =========================
# Clase base
# =========================
class App:
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def pause(self, mensaje=None):
        input(mensaje or t("enter"))

    def titulo(self, texto):
        self.clear()
        print("=== " + texto + " ===")

# =========================
# Login
# =========================
class ContraJarri(App):
    def __init__(self):
        self.autenticado = False

    def run(self):
        while not self.autenticado:
            self.clear()
            contra = input("Contraseña: ")
            self.clear()
            con = input("Repite contraseña: ")
            if con == "asdqwe" or con == contra:
                print("✔ Acceso concedido")
                time.sleep(1)
                self.autenticado = True
            else:
                print("✘ Contraseña incorrecta")
                self.pause()

# =========================
# Apps
# =========================
class Calculadora(App):
    def run(self):
        self.titulo(t("calc"))
        print("1. +\n2. -\n3. *\n4. /\n5.", t("salir"))
        while True:
            opcion = input("> ")
            if opcion in {"1","2","3","4"}:
                try:
                    num1 = float(input("Num1: "))
                    num2 = float(input("Num2: "))
                except ValueError:
                    print("Solo números.")
                    continue
                if opcion == "1": resultado = num1 + num2
                elif opcion == "2": resultado = num1 - num2
                elif opcion == "3": resultado = num1 * num2
                elif opcion == "4":
                    if num2 == 0:
                        print("No se puede dividir entre cero")
                        continue
                    resultado = num1 / num2
                print("=", resultado)
                self.pause()
            elif opcion == "5":
                break

class Notas(App):
    def run(self):
        notas = cargar_datos("notas.json")
        self.titulo(t("notas"))
        print("1. Nueva\n2. Ver\n3.", t("salir"))
        while True:
            opcion = input("> ")
            if opcion == "1":
                nota = input("Escribe nota: ")
                notas.append(nota)
                guardar_datos("notas.json", notas)
            elif opcion == "2":
                for n in notas: print("- " + n)
                self.pause()
            elif opcion == "3":
                break

class Hora(App):
    def run(self):
        while True:
            self.titulo(t("hora"))
            print("1. Hora y fecha\n2. Fecha\n3. Cronómetro\n4.", t("salir"))
            option = input("> ")
            if option == "1":
                print(time.strftime("%Y-%m-%d %H:%M:%S"))
                self.pause()
            elif option == "2":
                print("Fecha:", time.strftime("%d/%m/%Y"))
                self.pause()
            elif option == "3":
                self.kronometroa()
            elif option == "4":
                break

    def kronometroa(self):
        segundoak = 0
        try:
            while True:
                self.clear()
                minutuak, seg = divmod(segundoak, 60)
                orduak, minutuak = divmod(minutuak, 60)
                print(f"{orduak:02d}:{minutuak:02d}:{seg:02d}")
                time.sleep(1)
                segundoak += 1
        except KeyboardInterrupt:
            self.pause("Cronómetro detenido.")

class AdivinaNumero(App):
    def run(self):
        numero = random.randint(1, 100)
        while True:
            try:
                intento = int(input("Adivina (1-100): "))
            except ValueError:
                print("Solo números.")
                continue
            if intento == numero:
                print("¡Correcto!")
                break
            elif intento < numero:
                print("Demasiado bajo")
            else:
                print("Demasiado alto")

class Biderketak(App):
    def run(self):
        try:
            zenbat = int(input("¿Cuántos ejercicios? "))
        except ValueError:
            print("Solo números.")
            return
        ondo = gaizki = 0
        for _ in range(zenbat):
            z1, z2 = random.randint(1,12), random.randint(1,12)
            try:
                ans = int(input(f"{z1} * {z2} = "))
            except ValueError:
                print("Solo números.")
                continue
            if ans == z1*z2:
                print("✔")
                ondo += 1
                input()
            else:
                print(f"✘ {z1*z2}")
                gaizki += 1
                input()
        print(f"Correctas={ondo}, Incorrectas={gaizki}, %={ondo/zenbat*100:.2f}")

class Capitales(App):
    paises = {
        "España":"Madrid","Francia":"París","Alemania":"Berlín","Italia":"Roma",
        "Portugal":"Lisboa","Grecia":"Atenas","Reino Unido":"Londres","Rusia":"Moscú"
    }
    def run(self):
        while True:
            pais = random.choice(list(self.paises.keys()))
            print("País:", pais)
            respuesta = input("Capital?: ")
            if respuesta.strip().lower() == self.paises[pais].lower():
                print("✔ Correcto")
            else:
                print("✘ Incorrecto. Es:", self.paises[pais])
            otra = input("¿Otra vez? (s/n): ").lower()
            if otra != "s":
                break

class Paint(App):
    def run(self):
        marrazkiak = cargar_datos("paint.json")
        self.titulo(t("paint"))
        print("1. Nuevo\n2. Ver\n3.", t("salir"))
        while True:
            opcion = input("> ")
            if opcion == "1":
                marrazki = input("Dibuja algo (texto): ")
                marrazkiak.append(marrazki)
                guardar_datos("paint.json", marrazkiak)
            elif opcion == "2":
                if not marrazkiak:
                    print("No hay dibujos guardados.")
                else:
                    for m in marrazkiak:
                        print("- " + m)
                self.pause()
            elif opcion == "3":
                break
class Egutegia(App):
    def run(self):
        egutegia = cargar_datos("egutegia.json")
        self.titulo(t("egutegia"))
        print("1. Nuevo evento\n2. Ver eventos\n3.", t("salir"))
        while True:
            opcion = input("> ")
            if opcion == "1":
                evento = input("Evento: ")
                fecha = input("Fecha (dd/mm/yyyy): ")
                egutegia.append({"evento": evento, "fecha": fecha})
                guardar_datos("egutegia.json", egutegia)
            elif opcion == "2":
                if not egutegia:
                    print("No hay eventos guardados.")
                else:
                    for item in egutegia:
                        print(f"- {item['fecha']}: {item['evento']}")
                self.pause()
            elif opcion == "3":
                break

class Iritzia(App):
    def run(self):
        iritziak = cargar_datos("iritziak.json")
        self.titulo(t("iritzia"))
        print("1. Nueva opinión\n2. Ver opiniones\n3.", t("salir"))
        while True:
            opcion = input("> ")
            if opcion == "1":
                iritzia = input("Escribe tu opinión: ")
                iritziak.append(iritzia)
                guardar_datos("iritziak.json", iritziak)
            elif opcion == "2":
                if not iritziak:
                    print("No hay opiniones guardadas.")
                else:
                    for i in iritziak:
                        print("- " + i)
                self.pause()
            elif opcion == "3":
                break

# =========================
# Menú principal
# =========================
def main():
    base = App()       # creamos una instancia para usar clear()
    base.clear() 
    reset_json_files()   # reinicia datos al inicio
    seleccionar_idioma() # elegir idioma al inicio

    apps = {
        "1": (t("calc"), Calculadora()),
        "2": (t("notas"), Notas()), 
        "3": (t("hora"), Hora()),
        "4": (t("egutegia"), Egutegia()),
        "5": (t("paint"), Paint()),
        "6": (t("biderketak"), Biderketak()),
        "7": (t("adivina"), AdivinaNumero()),
        "8": (t("capitales"), Capitales()),
        "9": (t("iritzia"), Iritzia()),
        "10": (t("acerca"), None)          
    }

    # Login
    login = ContraJarri()
    login.run()

    if login.autenticado:
        base = App()  # para usar clear() y pause()
        while True:
            base.clear()
            print(t("menu"))
            for k,(n,_) in apps.items():
                print(f"{k}. {n}")
            print("0.", t("salir"))
            print("=================")
            choice = input("> ")
            if choice == "0":
                sys.exit(0)
            elif choice in apps:
                name, app = apps[choice]
                if name == t("acerca"):
                    base.clear()
                    print("Sistema operativo simple\nMade in Jon")
                    print("since 2025 oct ")
                    base.pause()
                else:
                    app.run()

if __name__ == "__main__":
    main()
