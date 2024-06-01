import sqlite3
import requests


url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
params = {
    "fecha": "2023-01-01",
    "hasta": "2023-12-31",
    "moneda": "USD"
}
response = requests.get(url, params=params)
data = response.json()

conn = sqlite3.connect('base.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                    fecha TEXT,
                    precio_compra REAL,
                    precio_venta REAL
                )''')

for item in data:
    fecha = item['fecha']
    precio_compra = item['precio_compra']
    precio_venta = item['precio_venta']
    cursor.execute("INSERT INTO sunat_info (fecha, precio_compra, precio_venta) VALUES (?, ?, ?)",
                   (fecha, precio_compra, precio_venta))

conn.commit()


cursor.execute("SELECT * FROM sunat_info")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()