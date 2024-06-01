import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    
    fuentes_disponibles = figlet.getFonts()

    fuente_seleccionada = input("Ingrese el nombre de la fuente (o presione Enter para seleccionar una fuente aleatoria): ")

    if not fuente_seleccionada:
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Fuente aleatoria seleccionada: {fuente_seleccionada}")
    elif fuente_seleccionada not in fuentes_disponibles:
        print("Fuente no válida. Seleccionando una fuente aleatoria.")
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Fuente aleatoria seleccionada: {fuente_seleccionada}")

   
    figlet.setFont(font=fuente_seleccionada)

   
    texto_imprimir = input("Ingrese el texto a imprimir: ")

    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()