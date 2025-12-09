import os
import time
import sys
import random
import json

def clear():
    os.system("cls" if os.name == "nt" else "clear")  

# --- Persistencia ---
def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def cargar_datos(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# --- Clase base ---
class App:
    def run(self):
        pass

# --- Contraseña ---
a = 0
class ContraJarri(App):
    def run(self):
        global a
        while True:
            clear()
            contra = input("Idatzi zure kontraseña: ")
            clear()
            con = input("zein da zure kontraseña? ")
            if con == contra:
                print("Hori da!")
                a = 1
                break
            else:
                print("kontraseña ez da zuzena!")
                a = 0
                input("Sakatu Enter berriro saiatzeko...")

# --- Calculadora ---
class Calculadora(App):
    def run(self):
        clear()
        print("Kalkulagailua")
        print("1. Batuketa\n2. Kenketa\n3. Biderketa\n4. Zatiketa\n5. Irten")
        while True:
            opcion = input("Aukeratu aukera bat: ")
            if opcion in {"1","2","3","4"}:
                try:
                    num1 = float(input("Lehen zenbakia: "))
                    num2 = float(input("Bigarren zenbakia: "))
                except ValueError:
                    print("Zenbakiak bakarrik.")
                    continue
                if opcion == "1": resultado = num1 + num2
                elif opcion == "2": resultado = num1 - num2
                elif opcion == "3": resultado = num1 * num2
                elif opcion == "4":
                    if num2 == 0:
                        print("Ezin da zeroz zatitu")
                        continue
                    resultado = num1 / num2
                print("Emaitza:", resultado)
            elif opcion == "5":
                break

# --- Adivina número ---
class AdivinaNumero(App):
    def run(self):
        numero = random.randint(1, 100)
        while True:
            intento = int(input("Adivina el número (1-100): "))
            if intento == numero:
                print("¡Correcto!")
                break
            elif intento < numero:
                print("Demasiado bajo")
            else:
                print("Demasiado alto")

# --- Notas ---
notas = cargar_datos("notas.json")
class Notas(App):
    def run(self):
        clear()
        print("Notas\n1. Nota berria\n2. Beste notak\n3. Atera")
        while True:
            opcion = input("> ")
            if opcion == "1":
                nota = input("Sartu nota: ")
                notas.append(nota)
                guardar_datos("notas.json", notas)
            elif opcion == "2":
                for nota in notas: print("- " + nota)
            elif opcion == "3": break

# --- Hora ---
class Hora(App):
    def run(self):
        while True:
            clear()
            print("Ordularia\n1. Ordua eta data\n2. Data\n3. Kronometroa\n4. Atera")
            option = input("> ")
            if option == "1":
                print(time.strftime("%Y-%m-%d %H:%M:%S"))
                input("Enter...")
            elif option == "2":
                print("Data:", time.strftime("%d/%m/%Y"))
                input("Enter...")
            elif option == "3":
                self.kronometroa()
            elif option == "4": break

    def kronometroa(self):
        segundoak = 0
        try:
            while True:
                clear()
                minutuak, seg = divmod(segundoak, 60)
                orduak, minutuak = divmod(minutuak, 60)
                print(f"{orduak:02d}:{minutuak:02d}:{seg:02d}")
                time.sleep(1)
                segundoak += 1
        except KeyboardInterrupt:
            input("Gelditu. Enter...")

# --- Biderketak ---
class Biderketak(App):
    def run(self):
        zenbat = int(input("Zenbat ariketa? "))
        ondo = gaizki = 0
        for _ in range(zenbat):
            z1, z2 = random.randint(1,12), random.randint(1,12)
            try:
                ans = int(input(f"{z1} * {z2} = "))
            except ValueError:
                print("Zenbakiak bakarrik.")
                continue
            if ans == z1*z2:
                print("✔")
                ondo += 1
            else:
                print(f"✘ {z1*z2}")
                gaizki += 1
        print(f"Ondo={ondo}, Gaizki={gaizki}, Portzentaia={ondo/zenbat*100:.2f}%")

# --- Paint ---
marrazkiak = []
class Paint(App):
    def run(self):
        clear()
        print("Marrazkiak\n1. Berria\n2. Ikusi\n3. Atera")
        while True:
            opcion = input("> ")
            if opcion == "1":
                marrazki = input("Marraztu: ")
                marrazkiak.append(marrazki)
            elif opcion == "2":
                for m in marrazkiak: print("- " + m)
            elif opcion == "3": break

# --- Egutegia ---
egutegia = cargar_datos("egutegia.json")
class Egutegia(App):
    def run(self):
        clear()
        print("Egutegia\n1. Gertaera berria\n2. Ikusi\n3. Atera")
        while True:
            auk = input("> ")
            if auk == "1":
                e = input("Gertaera: ")
                f = input("Data (dd/mm/yyyy): ")
                egutegia.append({"evento": e, "fecha": f})
                guardar_datos("egutegia.json", egutegia)
            elif auk == "2":
                for item in egutegia: print(f"- {item['fecha']}: {item['evento']}")
            elif auk == "3": break

# --- Juego de capitales ---
paises = {
    "España":"Madrid","Francia":"París","Alemania":"Berlín","Italia":"Roma",
    "Portugal":"Lisboa","Grecia":"Atenas","Reino Unido":"Londres","Rusia":"Moscú"
}
class Capitales(App):
    def run(self):
        while True:
            pais = random.choice(list(paises.keys()))
            print("País:", pais)
            respuesta = input("¿Cuál es su capital?: ")
            if respuesta.strip().lower() == paises[pais].lower():
                print("✔ Correcto")
            else:
                print("✘ Incorrecto. Es:", paises[pais])
            if input("¿Otra vez? (s/n): ").lower() != "s":
                break

# --- Main ---
def main():
    apps = {
        "1": ("Kalkuladora", Calculadora()),
        "2": ("Notak", Notas()), 
        "3": ("Ordularia", Hora()),
        "4": ("Egutegia", Egutegia()),
        "5": ("Marrazkiak", Paint()),
        "6": ("Biderketak", Biderketak()),
        "7": ("Asmatu zenbakia", AdivinaNumero()),
        "8": ("Capitalak", Capitales()),
        "9": ("Acerca de", None)
    }
    ContraJarri().run()
    while True:
        if a == 0: ContraJarri().run()
        else:
            clear()
            print("=== Python OS ===")
            for k,(n,_) in apps.items(): print(f"{k}. {n}")
            print("0. Salir")
            choice = input("> ")
            if choice == "0": sys.exit(0)
            elif choice in apps:
                name, app = apps[choice]
                if name == "Acerca de":
                    print("Sistema operativo simple\nMade in Jon")
                    input("Enter...")
                else: app.run()

if __name__ == "__main__":
    main()
