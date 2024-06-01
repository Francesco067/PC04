import requests
import sqlite3
from datetime import date

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

def obtener_tipo_cambio_moneda(moneda):
    try:
        response = requests.get("https://api.apis.net.pe/v1/tipo-cambio-sunat")
        response.raise_for_status()
        data = response.json()
        return float(data[0][moneda])
    except requests.RequestException as e:
        print(f"Error al obtener el tipo de cambio de {moneda}: {e}")
        return None

def crear_tabla_bitcoin(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                    fecha TEXT,
                    precio_usd REAL,
                    precio_gbp REAL,
                    precio_eur REAL,
                    precio_pen REAL
                )''')
    conn.commit()

def insertar_datos_bitcoin(conn, precio_usd, precio_gbp, precio_eur, precio_pen):
    fecha = date.today().strftime("%Y-%m-%d")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) VALUES (?, ?, ?, ?, ?)",
                   (fecha, precio_usd, precio_gbp, precio_eur, precio_pen))
    conn.commit()

def consultar_precio_bitcoin(conn, moneda, bitcoins):
    cursor = conn.cursor()
    cursor.execute(f"SELECT precio_{moneda.lower()} FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    precio_moneda = cursor.fetchone()[0]
    if precio_moneda:
        costo_en_moneda = bitcoins * precio_moneda
        print(f"El precio de comprar {bitcoins} bitcoins en {moneda} es: {costo_en_moneda:.4f}")
    else:
        print(f"No se encontró el precio en {moneda}")

def main():
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un número valido")
        return

    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        valor_total = n * precio_bitcoin

      
        conn = sqlite3.connect('base.db')

        crear_tabla_bitcoin(conn)

        precio_gbp = precio_bitcoin / obtener_tipo_cambio_moneda("GBP")
        precio_eur = precio_bitcoin / obtener_tipo_cambio_moneda("EUR")
        precio_pen = precio_bitcoin / obtener_tipo_cambio_moneda("PEN")

   
        insertar_datos_bitcoin(conn, precio_bitcoin, precio_gbp, precio_eur, precio_pen)

  
        consultar_precio_bitcoin(conn, "PEN", 10)
        consultar_precio_bitcoin(conn, "EUR", 10)

      
        conn.close()

        print(f"El costo actual de {n} Bitcoins es: ${valor_total:,.4f}")
    else:
        print("No se pudo consultar la API de BItcoins")

if __name__ == "__main__":
    main()