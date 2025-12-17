import os
import sys
import time
import random
import json
import requests

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
        "clima": "Clima",
        "jokuak": "Juegos",
        "enter": "Pulsa Enter para continuar..."
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
        "clima": "Weather",
        "jokuak": "Games",
        "enter": "Press Enter to continue..."
    },
    "eu": {
        "menu": "=== Python OS ===",
        "salir": "Irten",
        "calc": "Kalkulagailua",
        "notas": "Oharrak",
        "hora": "Ordularia",
        "egutegia": "Egutegia",
        "paint": "Marrazkiak",
        "biderketak": "Biderketak",
        "adivina": "Asmatu zenbakia",
        "capitales": "Hiriburua",
        "iritzia": "Iritziak",
        "acerca": "Honi buruz",
        "clima": "Eguraldia",
        "jokuak": "Jokoak",
        "enter": "Sakatu Enter jarraitzeko..."
    }
}

idioma_actual = "es"
usuario_actual = None
carpeta_usuario = None

def t(clave):
    return IDIOMAS[idioma_actual].get(clave, clave)

# =========================
# Selección de idioma
# =========================
def seleccionar_idioma():
    global idioma_actual
    print("Selecciona idioma / Select language / Hautatu hizkuntza")
    print("1. Español\n2. English\n3. Euskara")
    opcion = input("> ").strip()
    if opcion == "1":
        idioma_actual = "es"
    elif opcion == "2":
        idioma_actual = "en"
    elif opcion == "3":
        idioma_actual = "eu"
    else:
        print("Idioma no reconocido. Se usará Español.")
        idioma_actual = "es"
    time.sleep(0.6)

# =========================
# Utilidades
# =========================
def guardar_datos(ruta, datos):
    if os.path.dirname(ruta):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def cargar_datos(ruta):
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def ruta_usuario(archivo):
    return os.path.join(carpeta_usuario, archivo)

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
# Apps
# =========================
class Calculadora(App):
    def run(self):
        historial = cargar_datos(ruta_usuario("calc_historial.json"))
        self.titulo(t("calc"))
        print("1. +\n2. -\n3. *\n4. /\n5. Ver historial\n0.", t("salir"))
        while True:
            opcion = input("> ").strip()
            if opcion in {"1","2","3","4"}:
                try:
                    num1 = float(input("Num1: "))
                    num2 = float(input("Num2: "))
                except ValueError:
                    print("✘ Solo números")
                    continue
                if opcion == "1": resultado = num1 + num2; op = "+"
                elif opcion == "2": resultado = num1 - num2; op = "-"
                elif opcion == "3": resultado = num1 * num2; op = "*"
                elif opcion == "4":
                    if num2 == 0:
                        print("No se puede dividir entre cero")
                        continue
                    resultado = num1 / num2; op = "/"
                print(f"= {resultado}")
                historial.append(f"{num1} {op} {num2} = {resultado}")
                guardar_datos(ruta_usuario("calc_historial.json"), historial)
                self.pause()
            elif opcion == "5":
                for h in historial: print("- " + h)
                self.pause()
            elif opcion == "0":
                break
            else:
                print("✘ Opción inválida")

class Clima(App):
    def run(self):
        ciudad = input("Ciudad: ").strip()
        url = f"http://wttr.in/{ciudad}?format=%t+%C"
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                clima = r.text.strip()
                print(f"Clima en {ciudad}: {clima}")
            else:
                print(f"✘ Error {r.status_code}: {r.text}")
        except requests.exceptions.RequestException as e:
            print(f"✘ Error de conexión: {e}")
        self.pause()

class Notas(App):
    def run(self):
        notas = cargar_datos(ruta_usuario("notas.json"))
        self.titulo(t("notas"))
        print("1. Nueva\n2. Ver\n0.", t("salir"))
        while True:
            opcion = input("> ").strip()
            if opcion == "1":
                nota = input("Escribe nota: ")
                notas.append(nota)
                guardar_datos(ruta_usuario("notas.json"), notas)
            elif opcion == "2":
                if not notas:
                    print("No hay notas guardadas.")
                else:
                    for n in notas: print("- " + n)
                self.pause()
            elif opcion == "0":
                break
            else:
                print("✘ Opción inválida")

class Hora(App):
    def run(self):
        while True:
            self.titulo(t("hora"))
            print("1. Hora y fecha\n2. Fecha\n3. Cronómetro\n0.", t("salir"))
            option = input("> ").strip()
            if option == "1":
                print(time.strftime("%Y-%m-%d %H:%M:%S"))
                self.pause()
            elif option == "2":
                print("Fecha:", time.strftime("%d/%m/%Y"))
                self.pause()
            elif option == "3":
                self.kronometroa()
            elif option == "0":
                break
            else:
                print("✘ Opción inválida")

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

class Jokuak(App):
    def __init__(self):
        self.paises = {
            "España": "Madrid", "Francia": "Paris", "Alemania": "Berlin", "Italia": "Roma",
            "Portugal": "Lisboa", "Grecia": "Atenas", "Reino Unido": "Londres", "Rusia": "Moscu"
        }
        self.marrazkiak = cargar_datos(ruta_usuario("paint.json"))

    def multiplication_game(self):
        try:
            zenbat = int(input("¿Cuántos ejercicios? "))
        except ValueError:
            print("✘ Solo números")
            return
        ondo = gaizki = 0
        for _ in range(zenbat):
            z1, z2 = random.randint(1, 12), random.randint(1, 12)
            try:
                ans = int(input(f"{z1} * {z2} = "))
            except ValueError:
                print("✘ Solo números.")
                continue
            if ans == z1 * z2:
                print("✔ Correcto")
                ondo += 1
            else:
                print(f"✘ Incorrecto. Era {z1*z2}")
                gaizki += 1
        print(f"Correctas={ondo}, Incorrectas={gaizki}, %={ondo/zenbat*100:.2f}")
        self.pause()

    def capital_game(self):
        while True:
            pais = random.choice(list(self.paises.keys()))
            print("País:", pais)
            print("sin tildes porfavor ")
            respuesta = input("Capital?: ")
            if respuesta.strip().lower() == self.paises[pais].lower():
                print("✔ Correcto")
            else:
                print(f"✘ Incorrecto. Es: {self.paises[pais]}")
            while True:
                c = input("¿Otra vez? (s/n): ").lower()
                if c == "s":
                    break
                elif c == "n":
                    return

    def guess_number(self):
        numero = random.randint(1, 100)
        while True:
            try:
                intento = int(input("Adivina (1-100): "))
            except ValueError:
                print("✘ Solo números.")
                continue
            if intento == numero:
                print("🎉 ¡Correcto!")
                break
            elif intento < numero:
                print("Demasiado bajo")
            else:
                print("Demasiado alto")
        self.pause()

    def paint(self):
        marrazkiak = cargar_datos(ruta_usuario("marrazkiak.json"))
        self.titulo(t("notas"))
        print("1. Nueva\n2. Ver\n0.", t("salir"))
        while True:
            opcion = input("> ").strip()
            if opcion == "1":
                marrazkia = input("Dibuja: ")
                marrazkiak.append(marrazkia)
                guardar_datos(ruta_usuario("marrazkiak.json"), marrazkiak)
            elif opcion == "2":
                if not marrazkiak:
                    print("No hay dibujos guardados.")
                else:
                    for n in marrazkiak: print("- " + n)
                self.pause()
            elif opcion == "0":
                break
            else:
                print("✘ Opción inválida")

    def run(self):
        while True:
            self.titulo(t("jokuak"))
            print("1. Multiplication Game\n2. Capital Game\n3. Guess the Number\n4. Paint\n0.", t("salir"))
            opcion = input("> ").strip()
            if opcion == "1":
                self.multiplication_game()
            elif opcion == "2":
                self.capital_game()
            elif opcion == "3":
                self.guess_number()
            elif opcion == "4":
                self.paint()
            elif opcion == "0":
                break
            else:
                print("✘ Opción inválida")
                self.pause()

# =========================
# Calendario
# =========================
class Egutegia(App):
    def run(self):
        egutegia = cargar_datos(ruta_usuario("egutegia.json"))
        self.titulo(t("egutegia"))
        print("1. Nuevo evento\n2. Ver eventos\n0.", t("salir"))
        while True:
            opcion = input("> ").strip()
            if opcion == "1":
                evento = input("Evento: ")
                fecha = input("Fecha (dd/mm/yyyy): ")
                egutegia.append({"evento": evento, "fecha": fecha})
                guardar_datos(ruta_usuario("egutegia.json"), egutegia)
            elif opcion == "2":
                if not egutegia:
                    print("No hay eventos guardados.")
                else:
                    for item in egutegia:
                        print(f"- {item['fecha']}: {item['evento']}")
                self.pause()
            elif opcion == "0":
                break
            else:
                print("✘ Opción inválida")

# =========================
# Opiniones
# =========================
class Iritzia(App):
    def run(self):
        iritziak = cargar_datos(ruta_usuario("iritziak.json"))
        self.titulo(t("iritzia"))
        print("1. Nueva opinión\n2. Ver opiniones\n0.", t("salir"))
        while True:
            opcion = input("> ").strip()
            if opcion == "1":
                iritzia = input("Escribe tu opinión: ")
                iritziak.append(iritzia)
                guardar_datos(ruta_usuario("iritziak.json"), iritziak)
            elif opcion == "2":
                if not iritziak:
                    print("No hay opiniones guardadas.")
                else:
                    for i in iritziak:
                        print("- " + i)
                self.pause()
            elif opcion == "0":
                break
            else:
                print("✘ Opción inválida")

# =========================
# Sistema de usuarios
# =========================
def login_usuario():
    global usuario_actual, carpeta_usuario
    os.makedirs("usuarios", exist_ok=True)
    usuario = input("Nombre de usuario / Username / Erabiltzaile izena: ").strip()
    carpeta = os.path.join("usuarios", usuario)
    os.makedirs(carpeta, exist_ok=True)
    usuario_actual = usuario
    carpeta_usuario = carpeta
    print(f"✔ Sesión iniciada como {usuario}")
    time.sleep(0.6)

# =========================
# Menú principal
# =========================
def main():
    base = App()
    base.clear()
    seleccionar_idioma()
    login_usuario()

    apps = {
        "1": (t("calc"), Calculadora()),
        "2": (t("notas"), Notas()), 
        "3": (t("hora"), Hora()),
        "4": (t("egutegia"), Egutegia()),
        "5": (t("jokuak"), Jokuak()),
        "6": (t("iritzia"), Iritzia()),
        "7": (t("clima"), Clima()),
        "8": (t("acerca"), None)          
    }

    while True:
        base.clear()
        print(t("menu"))
        for k,(n,_) in apps.items():
            print(f"{k}. {n}")
        print("0.", t("salir"))
        print("=================")
        choice = input("> ").strip()
        if choice == "0":
            sys.exit(0)
        elif choice in apps:
            name, app = apps[choice]
            if name == t("acerca"):
                base.clear()
                print("Sistema operativo simple\nMade in Jon")
                base.pause()
            else:
                app.run()
        else:
            print("✘ Opción inválida")
            base.pause()

if __name__ == "__main__":
    main()
