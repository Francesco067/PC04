def contar_lineas_codigo(ruta_archivo):
    try:
        
        if not ruta_archivo.endswith('.py'):
            print("El archivo no tiene la extensión .py.")
            return

        with open(ruta_archivo, 'r  ') as archivo:
            lineas = archivo.readlines()

        lineas_codigo = 0
        for linea in lineas:
           
            linea = linea.strip()
            if linea and not linea.startswith('#'):
                lineas_codigo += 1

        print(f"Número de líneas de código: {lineas_codigo}")

    except FileNotFoundError:
        print("El archivo no se encuentra o la ruta es inválida.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()