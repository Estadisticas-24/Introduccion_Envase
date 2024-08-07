import pyodbc
import json
import git
import os

# Configuración de la conexión a SQL Server
servidor = 'ACT_40000029135\\ESTADISTICAS'
base_de_datos = 'Estadistica'
conexion_string = f'DRIVER={{SQL Server}};SERVER={servidor};DATABASE={base_de_datos};Trusted_Connection=yes;'

def fetch_data_from_sql():
    try:
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
        return "Datos descargados de SQL exitosamente."
    except Exception as e:
        return f"Error al descargar los datos de SQL: {e}"

def commit_and_push_to_github(repo_path, commit_message):
    try:
        repo = git.Repo(repo_path)
        repo.git.add('--all')
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
        return "Proyecto subido a GitHub exitosamente."
    except Exception as e:
        return f"Error al subir el proyecto a GitHub: {e}"

if __name__ == '__main__':
    # Descargar datos de SQL y guardarlos en un archivo JSON
    fetch_response = fetch_data_from_sql()
    print(fetch_response)

    # Ruta al repositorio local
    repo_path = r'\\ACT_40000008781\ShareEstadisticas\27 Practicantes\Alan Martinez\Prueba A\Introduccion de envase'  # Reemplaza esto con la ruta a tu repositorio local
    commit_message = 'Datos guardados y proyecto actualizado'

    # Hacer commit y push de los cambios a GitHub
    git_response = commit_and_push_to_github(repo_path, commit_message)
    print(git_response)
