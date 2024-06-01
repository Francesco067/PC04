import requests


def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        datos = response.json()
        precio_usd = datos['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al consultar la API de Bitcoins: {e}")
        return None

def main():
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un número valido")
        return

    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        valor_total = n * precio_bitcoin
        print(f"El costo actual de {n} Bitcoins es: ${valor_total:,.4f}")
    else:
        print("No se pudo consultar la API de BItcoins")

if __name__ == "__main__":
    main()