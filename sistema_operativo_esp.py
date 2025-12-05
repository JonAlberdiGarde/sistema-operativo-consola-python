# sistema operativo simple
import os
import time
import sys
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear")  
    # limpiar pantalla

class App:
    def run(self):
        pass

class Calculadora(App):
    def run(self):
        clear()
        print("Calculadora")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        while True:
            opcion = input("Elige una opción: ")

            if opcion in {"1", "2", "3", "4"}:
                try:
                    num1 = float(input("Introduce el primer número: "))
                    num2 = float(input("Introduce el segundo número: "))
                except ValueError:
                    print("Por favor introduce números válidos.")
                    continue

                if opcion == "1":
                    resultado = num1 + num2
                elif opcion == "2":
                    resultado = num1 - num2
                elif opcion == "3":
                    resultado = num1 * num2
                elif opcion == "4":
                    if num2 == 0:
                        print("No se puede dividir entre cero")
                        continue
                    resultado = num1 / num2

                print("Resultado:", resultado)

            elif opcion == "5":
                print("¡Adiós!")
                break
            else:
                print("Opción inválida")



# Lista de notas
notas = []

class Notas(App):
    def run (self):
        clear()
        print("Notas")
        print("1. Nueva nota")
        print("2. Mostrar notas")
        print("3. Salir")
        while True:
            opcion = input("Elige una opción: ")
            if opcion == "1":
                nota = input("Escribe la nota: ")
                notas.append(nota)
                print("Nota guardada.")
            elif opcion == "2":
                if not notas:
                    print("No hay notas.")
                else:
                    print("Tus notas:")
                    for nota in notas:
                        print("- " + nota)
            elif opcion == "3":
                break
            else:
                print("Opción inválida")

class Hora(App):
    def run(self):
        while True:
            clear()
            print("=== Reloj ===\n")
            print("1. Hora y fecha")
            print("2. Fecha")
            print("3. Cronómetro")
            print("4. Salir")
            
            option = input("Elige una opción: ").strip()
            
            if option == "1":
                def print_current_time():
                    try:
                        current_time = time.gmtime(time.time())
                        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
                        print(formatted_time, end="\r")
                    except TypeError:
                        print("Valor de tiempo inválido")
                print_current_time()
                while True:
                    time.sleep(1)
                    print_current_time()
                    input("\nPulsa Enter para volver...")
            elif option == "2":
                clear()
                print("Fecha: ", time.strftime("%d/%m/%Y"))
                input("\nEnter para volver.")
                
            elif option == "3":
                self.kronometroa()
                
            elif option == "4":
                break
                
            else:
                print("Opción inválida")
                input("Enter para volver...")

    def kronometroa(self):
        clear()
        print("=== Cronómetro ===")
        print("Pulsa CTRL+C para detener.\n")
        segundoak = 0
        try:
            while True:
                clear()
                minutuak, segundoak_display = divmod(segundoak, 60)
                orduak, minutuak = divmod(minutuak, 60)
                print(f"Cronómetro: {orduak:02d}:{minutuak:02d}:{segundoak_display:02d}")
                time.sleep(1)
                segundoak += 1
        except KeyboardInterrupt:
            print("\nCronómetro detenido. Pulsa Enter para volver al menú...")
            input()

class Biderketak(App):
    def run(self):
        y = 0
        while y == 0:
            a = incorrecto = correcto = total = puntuacion = 0
            if y == 0:
                print('¡Bienvenido al juego de repaso de tablas de multiplicar!')
                print()
                time.sleep(2)
                print('Recuerda que solo debes escribir números, sin letras ni espacios.')
                time.sleep(3)
            total = int(input("¿Cuántos ejercicios quieres hacer? "))
            if total == 0:
                print("No puedes elegir 0, mínimo 1.")
                total = 1
            time.sleep(1)
            print("¡De acuerdo, empecemos!")
            time.sleep(1)
            
            while a != total:
                z1 = random.randrange(1,12)
                z2 = random.randrange(1,12)
                print()
                try:
                    respuesta = int(input(f"¿Cuánto es {z1} * {z2}? "))
                except ValueError:
                    print("Escribe solo números, por favor.")
                    continue
                resultado_correcto = z1 * z2
                if resultado_correcto == respuesta:
                    print("¡Muy bien! :)")
                    correcto += 1
                else:
                    print(f"Incorrecto. {z1} * {z2} = {resultado_correcto}, no {respuesta}")
                    incorrecto += 1
                
                puntuacion = correcto - incorrecto
                print(f"Correctas = {correcto}, Incorrectas = {incorrecto}, Puntuación = {puntuacion}\n")
                a += 1
            
            porcentaje = correcto / total * 100
            print("\nAquí están tus resultados:")
            print(f"Correctas = {correcto}, Incorrectas = {incorrecto}, Puntuación = {puntuacion}")
            print(f"Porcentaje = {porcentaje}%")
            if porcentaje == 100:
                print("¡Excelente! ;)")
            else:
                print("Practica más para sacar 100 la próxima vez. ¡Ánimo!")
            
            seguir = input("¿Quieres continuar? (s/n) ").lower()
            if seguir == "s":
                y = 0
            else:
                y = 1
                print("¡Gracias!")

marrazkiak = []

class Paint(App):
    def run (self):
        clear()
        print("Dibujos")
        print("1. Nuevo dibujo")
        print("2. Ver dibujos")
        print("3. Salir")
        while True:
            opcion = input("Elige una opción: ")
            if opcion == "1":
                marrazki = input("Dibuja: ")
                marrazkiak.append(marrazki)
                print("Dibujo guardado.")
            elif opcion == "2":
                if not marrazkiak:
                    print("No hay dibujos.")
                else:
                    print("Tus dibujos:")
                    for marrazki in marrazkiak:
                        print("- " + marrazki)
            elif opcion == "3":
                break
            else:
                print("Opción inválida")

egutegia = []

class Egutegia(App):
    def run(self):
        clear()
        print("Calendario")
        print("1. Nuevo evento")
        print("2. Ver eventos")
        print("3. Volver")
        while True:
            auk = input("> ")
            if auk == "1":
                e = input("Evento: ")
                f = input("Fecha (dd/mm/yyyy): ")
                egutegia.append((e,f))
                print("Guardado!")
            elif auk == "2":
                for e,f in egutegia:
                    print(f"- {f}: {e}")
            elif auk == "3":
                break
            else:
                print("Opción inválida!")
            

def main():
    apps = {
    "1": ("Calculadora", Calculadora()),
    "2": ("Notas", Notas()), 
    "3": ("Reloj", Hora()),
    "4": ("Calendario", Egutegia()),
    "5": ("Dibujos", Paint()),
    "6": ("Multiplicaciones", Biderketak()),
    "7": ("Acerca de", None)
    }

    
    while True:
        clear()
        print("=== Python OS ===")
        print("Elige una opción:\n")
        for key, (name, _) in apps.items():
            print(f"{key}. {name}")
        print("\n0. Salir")

        choice = input("\nSelecciona una app: ").strip()
        if choice == "0":
            print("Saliendo...")
            sys.exit(0)
        elif choice in apps:
            name, app = apps[choice]
            if name == "Acerca de":
                clear()
                print("Sistema operativo propio")
                print("Hecho por Jon")
                input("\nEnter para volver...")
            else:
                app.run()
        else:
            print("Elige otra opción.")
            input("Enter para volver...")

if __name__ == "__main__":
    main()
