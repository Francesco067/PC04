import os

class TablaMultiplicar:
    def __init__(self, numero):
        self.numero = numero
        self.nombre_archivo = f"tabla-{numero}.txt"

    def generar_tabla(self):
        try:
            with open(self.nombre_archivo, 'w') as file:
                for i in range(1, 11):
                    file.write(f"{self.numero} x {i} = {self.numero * i}\n")
            print(f"Tabla de multiplicar del {self.numero} guardada en {self.nombre_archivo}")
        except Exception as e:
            print(f"Error al generar la tabla de multiplicar: {e}")

    def mostrar_tabla(self):
        try:
            with open(self.nombre_archivo, 'r') as file:
                contenido = file.read()
            print(contenido)
        except FileNotFoundError:
            print(f"El archivo {self.nombre_archivo} no existe.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def mostrar_linea(self, linea):
        try:
            with open(self.nombre_archivo, 'r') as file:
                lineas = file.readlines()
            if 1 <= linea <= 10:
                print(lineas[linea - 1].strip())
            else:
                print("Número de línea fuera de rango. Debe estar entre 1 y 10.")
        except FileNotFoundError:
            print(f"El archivo {self.nombre_archivo} no existe.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Generar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea específica de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            n = solicitar_numero("Ingrese un número entero entre 1 y 10: ")
            if n:
                tabla = TablaMultiplicar(n)
                tabla.generar_tabla()
        elif opcion == '2':
            n = solicitar_numero("Ingrese un número entero entre 1 y 10: ")
            if n:
                tabla = TablaMultiplicar(n)
                tabla.mostrar_tabla()
        elif opcion == '3':
            n = solicitar_numero("Ingrese un número entero entre 1 y 10: ")
            m = solicitar_numero("Ingrese el número de línea que desea mostrar (1-10): ")
            if n and m:
                tabla = TablaMultiplicar(n)
                tabla.mostrar_linea(m)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")

def solicitar_numero(mensaje):
    try:
        numero = int(input(mensaje))
        if 1 <= numero <= 10:
            return numero
        else:
            print("El número debe estar entre 1 y 10.")
            return None
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return None

if __name__ == "__main__":
    menu()