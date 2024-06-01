import requests
from datetime import datetime

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        datos = response.json()
        precio_usd = datos['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al consultar la API de CoinDesk: {e}")
        return None

def guardar_datos_en_txt(cantidad, precio_bitcoin, valor_total):
    try:
        with open('precio_bitcoin.txt', 'a') as file:
            file.write(f"Fecha y hora: {datetime.now()}\n")
            file.write(f"Cantidad de Bitcoins: {cantidad}\n")
            file.write(f"Precio de Bitcoin en USD: ${precio_bitcoin:,.4f}\n")
            file.write(f"Valor total en USD: ${valor_total:,.4f}\n")
            file.write("-" * 40 + "\n")
        print("Datos guardados en precio_bitcoin.txt")
    except Exception as e:
        print(f"Error al guardar los datos en el archivo: {e}")

def main():
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        valor_total = n * precio_bitcoin
        print(f"El costo actual de {n} Bitcoins es: ${valor_total:,.4f}")
        guardar_datos_en_txt(n, precio_bitcoin, valor_total)
    else:
        print("No se pudo obtener el precio actual del Bitcoin. Inténtelo más tarde.")

if __name__ == "__main__":
    main()