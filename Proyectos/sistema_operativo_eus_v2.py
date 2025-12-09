# sistema operativo simple
import os
import time
import sys
import random
import json

def clear():
    os.system("cls" if os.name == "nt" else "clear")  
    # limpiar pantalla

# --- Funciones de persistencia ---
def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def cargar_datos(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []  # si no existe, devuelve lista vacía
class App:
    def run(self):
        pass

a = 0
class contra_jarri(App):
    def run(self):
        global a
        while True:
            clear()
            contra = input("Idatzi zure kontraseña: ")
            print("gordeta! ")
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

class Calculadora(App):
    def run(self):
        clear()
        print("Kalkulagailua")
        print("1. Batuketa")
        print("2. Kenketa")
        print("3. Biderketa")
        print("4. Zatiketa")
        print("5. Irten")

        while True:
            opcion = input("Aukeratu aukera bat: ")

            if opcion in {"1", "2", "3", "4"}:
                try:
                    num1 = float(input("Sartu lehen zenbakia: "))
                    num2 = float(input("Sartu bigarren zenbakia: "))
                except ValueError:
                    print("Mesedez, sartu zenbaki baliozkoak.")
                    continue

                if opcion == "1":
                    resultado = num1 + num2
                elif opcion == "2":
                    resultado = num1 - num2
                elif opcion == "3":
                    resultado = num1 * num2
                elif opcion == "4":
                    if num2 == 0:
                        print("Ezin da zeroz zatitu")
                        continue
                    resultado = num1 / num2

                print("Emaitza:", resultado)

            elif opcion == "5":
                print("Agur!")
                break
            else:
                print("Aukera baliogabea")

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


# Lista de notas

notas = cargar_datos("notas.json")

class Notas(App):
    def run(self):
        clear()
        print("Notas")
        print("1. Nota berria")
        print("2. Beste notak erakutsi")
        print("3. Atera")
        while True:
            opcion = input("Aukeratu bat: ")
            if opcion == "1":
                nota = input("Sartu nota: ")
                notas.append(nota)
                guardar_datos("notas.json", notas)
                print("Nota gordeta.")
            elif opcion == "2":
                if not notas:
                    print("Ez dago notarik.")
                else:
                    print("Zure notak:")
                    for nota in notas:
                        print("- " + nota)
            elif opcion == "3":
                break
            else:
                print("Ez du balio")

class Hora(App):
    def run(self):
        while True:
            clear()
            print("=== Ordularua ===\n")
            print("1. Ordua eta data")
            print("2. Data")
            print("3. Kronometroa")
            print("4. Atera")
            
            option = input("Aukeratu bat: ").strip()
            
            if option == "1":
                def print_current_time():
                    try:
                        current_time = time.gmtime(time.time())
                        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
                        print(formatted_time, end="\r")
                    except TypeError:
                        print("Invalid time value")
                print_current_time()
                while True:
                    time.sleep(1)
                    print_current_time()
                    input("\n1 bueltatzeko...")
            elif option == "2":
                clear()
                print("Data: ", time.strftime("%d/%m/%Y"))
                input("\n.")
                
            elif option == "3":
                self.kronometroa()
                
            elif option == "4":
                break
                
            else:
                print("Ez du balio")
                input("Enter bueltatzeko...")

    def kronometroa(self):
        clear()
        print("=== Kronometroa ===")
        print("CTRL+C sakatu gelditzeko.\n")
        segundoak = 0
        try:
            while True:
                clear()
                minutuak, segundoak_display = divmod(segundoak, 60)
                orduak, minutuak = divmod(minutuak, 60)
                print(f"Kronometroa: {orduak:02d}:{minutuak:02d}:{segundoak_display:02d}")
                time.sleep(1)
                segundoak += 1
        except KeyboardInterrupt:
            print("\nKronometroa gelditu da. Sakatu Enter menuera bueltatzeko...")
            input()

class Biderketak(App):
    def run(self):
        y = 0
        while y == 0:
            a = gaizki = ondo = zenbat = puntuazioa = 0
            if y == 0:
                print('Ongi etorri biderketen taulen errepaso jokura!')
                print()
                time.sleep(2)
                print('Gogoratu bakarrik zenbakiak idatzi behar dituzula, inolako letra edo espazio gabe!')
                time.sleep(3)
            zenbat = int(input("Zenbat ariketa nahi dituzu egin? "))
            if zenbat == 0:
                print("0 ezin da aukeratu, gutxienez bat egin behar dezu.")
                zenbat = 1
            time.sleep(1)
            print("Ados, has gaitezen!")
            time.sleep(1)
            
            while a != zenbat:
                z1 = random.randrange(1,12)
                z2 = random.randrange(1,12)
                print()
                try:
                    bere_emaitza = int(input(f"Zenbat da {z1} * {z2}? "))
                except ValueError:
                    print("Bakarrik zenbakiak idatzi mesedez.")
                    continue
                emaitza_berezkoa = z1 * z2
                if emaitza_berezkoa == bere_emaitza:
                    print("Oso ondo! :)")
                    ondo += 1
                else:
                    print(f"Gaizki! {z1} * {z2} = {emaitza_berezkoa}, ez {bere_emaitza}")
                    gaizki += 1
                
                puntuazioa = ondo - gaizki
                print(f"Ondo = {ondo}, Gaizki = {gaizki}, Puntuazioa = {puntuazioa}\n")
                a += 1
            
            portzentaia = ondo / zenbat * 100
            print("\nHauek dira zure emaitzak:")
            print(f"Ondo = {ondo}, Gaizki = {gaizki}, Puntuazioa = {puntuazioa}")
            print(f"Portzentaia = {portzentaia}%")
            if portzentaia == 100:
                print("Oso ondo! ;)")
            else:
                print("Gehiago praktikatu hurrengoan 100 ateratzeko! ;) Animo!")
            
            jarraitu = input("Jarraitu nahi duzu? (b/e) ").lower()
            if jarraitu == "b":
                y = 0
            else:
                y = 1
                print("Eskerrik asko!")


marrazkiak = []

class Paint(App):
    def run (self):
        clear()
        print("Marrazkiak")
        print("1. Marrazki berria")
        print("2. Beste marrazkiak erakutsi")
        print("3. Atera")
        while True:
            opcion = input("Aueratu bat: ")
            if opcion == "1":
                marrazki = input("Marraztu: ")
                marrazkiak.append(marrazki)
                print("Marrazkia gordeta.")
            elif opcion == "2":
                if not marrazkiak:
                    print("Ez dago marrazkirik.")
                else:
                    print("Zure marrazkiak:")
                    for marrazki in marrazkiak:
                        print("- " + marrazki)
            elif opcion == "3":
                break
            else:
                print("Ez du balio")

egutegia = cargar_datos("egutegia.json")

class Egutegia(App):
    def run(self):
        clear()
        print("Egutegia")
        print("1. Gertaera berria")
        print("2. Gertaerak erakutsi")
        print("3. Bueltatu")
        while True:
            auk = input("> ")
            if auk == "1":
                e = input("Gertaera: ")
                f = input("Data (dd/mm/yyyy): ")
                egutegia.append({"evento": e, "fecha": f})
                guardar_datos("egutegia.json", egutegia)
                print("Gordeta!")
            elif auk == "2":
                if not egutegia:
                    print("Ez dago gertaerarik.")
                else:
                    for item in egutegia:
                        print(f"- {item['fecha']}: {item['evento']}")
            elif auk == "3":
                break
            else:
                print("ez du balio!")

def main():
    apps = {
        "1": ("Kalkuladora", Calculadora()),
        "2": ("Notak", Notas()), 
        "3": ("Ordularia", Hora()),
        "4": ("Egutegia", Egutegia()),
        "5": ("Marrazkiak", Paint()),
        "6": ("Biderketak", Biderketak()),
        "7": ("Asmatu zenbakia", AdivinaNumero()),
        "8": ("Acerca de", None)
    }

    # Primero pedir contraseña
    contra_jarri().run()

    while True:
        if a == 0:
            print("ezin zara sartu! ")
            contra_jarri().run()
        else: 
            clear()
            print("=== Python OS ===")
            print("Hautatu bat:\n")
            for key, (name, _) in apps.items():
                print(f"{key}. {name}")
            print("\n0. Salir")

            choice = input("\nSelecciona un icono/app: ").strip()
            if choice == "0":
                print("Ateratzen...")
                sys.exit(0)
            elif choice in apps:
                name, app = apps[choice]
                if name == "Acerca de":
                    clear()
                    print("Sistema operatibo propioa")
                    print("Made in Jon")
                    input("\nEnter bueltatzeko...")
                else:
                    app.run()
            else:
                print("Aukeratu beste bat.")
                input("Enter bueltatzeko...")

if __name__ == "__main__":
    main()
