import pyodbc
import json

# Configuración de la conexión
servidor = 'ACT_40000029135\\ESTADISTICAS'
base_de_datos = 'Estadistica'
conexion_string = f'DRIVER={{SQL Server}};SERVER={servidor};DATABASE={base_de_datos};Trusted_Connection=yes;'

# Conectar a la base de datos
conexion = pyodbc.connect(conexion_string)

# Consulta SQL
consulta = """
SELECT DISTINCT(C.CODCliente), NombreClienteLegal, NombreComercial, NumeroIdentidadCliente, DirecciónNegocio 
FROM Clientes C
JOIN VentaMensual V ON V.CODCliente = C.CODCliente 
JOIN Territorios T ON T.CODTerritorio = V.CODTerritorio
WHERE T.Zona = '01#Zona Metro' AND V.Año='2024'
"""

# Ejecutar consulta y guardar resultados
cursor = conexion.cursor()
cursor.execute(consulta)
filas = cursor.fetchall()

# Crear lista de diccionarios
clientes = []
for fila in filas:
    clientes.append({
        "CODCliente": fila.CODCliente,
        "NombreClienteLegal": fila.NombreClienteLegal,
        "NombreComercial": fila.NombreComercial,
        "NumeroIdentidadCliente": fila.NumeroIdentidadCliente,
        "DireccionNegocio": fila.DirecciónNegocio
    })

# Guardar en JSON
with open('clientes.json', 'w') as archivo_json:
    json.dump(clientes, archivo_json, indent=4)

# Cerrar conexión
conexion.close()
