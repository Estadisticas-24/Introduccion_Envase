from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Configuración de la conexión a la base de datos
server = 'ACT_40000029135\\ESTADISTICAS'
database = 'Estadistica'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

# Ruta para recibir los datos del formulario y guardarlos en la base de datos
@app.route('/guardar_datos', methods=['POST'])
def guardar_datos():
    datos = request.json

    cod_cliente = datos.get('CODCliente')
    nombre_cliente = datos.get('NombreClienteLegal')
    identidad = datos.get('NumeroIdentidadCliente')
    nombre_negocio = datos.get('NombreComercial')
    direccion = datos.get('DireccionNegocio')
    motivo = datos.get('Motivo')
    beneficio = datos.get('Beneficio')
    fecha = datos.get('Fecha')
    introduccion = datos.get('Introduccion')
    ruta = datos.get('Ruta')

    Pepsi6_5oz_cant = datos.get('Pepsi6_5oz_cant')
    Pepsi6_5oz_precio = datos.get('Pepsi6_5oz_precio')
    Pepsi12oz_cant = datos.get('Pepsi12oz_cant')
    Pepsi12oz_precio = datos.get('Pepsi12oz_precio')
    Pepsi500ml_cant = datos.get('Pepsi500ml_cant')
    Pepsi500ml_precio = datos.get('Pepsi500ml_precio')
    Pepsi1_25lts_cant = datos.get('Pepsi1_25lts_cant')
    Pepsi1_25lts_precio = datos.get('Pepsi1_25lts_precio')
    MirindaN12oz_cant = datos.get('MirindaN12oz_cant')
    MirindaN12oz_precio = datos.get('MirindaN12oz_precio')
    MirindaB12oz_cant = datos.get('MirindaB12oz_cant')
    MirindaB12oz_precio = datos.get('MirindaB12oz_precio')
    MirindaU12oz_cant = datos.get('MirindaU12oz_cant')
    MirindaU12oz_precio = datos.get('MirindaU12oz_precio')
    MirindaN1_25lts_cant = datos.get('MirindaN1_25lts_cant')
    MirindaN1_25lts_precio = datos.get('MirindaN1_25lts_precio')
    sevenup12oz_cant = datos.get('sevenup12oz_cant')
    sevenup12oz_precio = datos.get('sevenup12oz_precio')
    teem12oz_cant = datos.get('teem12oz_cant')
    teem12oz_precio = datos.get('teem12oz_precio')
    LinkM6_5oz_cant = datos.get('LinkM6_5oz_cant')
    LinkM6_5oz_precio = datos.get('LinkM6_5oz_precio')
    LinkB6_5oz_cant = datos.get('LinkB6_5oz_cant')
    LinkB6_5oz_precio = datos.get('LinkB6_5oz_precio')
    LinkC6_5oz_cant = datos.get('LinkC6_5oz_cant')
    LinkC6_5oz_precio = datos.get('LinkC6_5oz_precio')

    try:
        # Conectar a la base de datos
        conexion = pyodbc.connect(connection_string)
        cursor = conexion.cursor()
        
        # Insertar datos en la base de datos
        consulta = """
        INSERT INTO tu_tabla (
            CODCliente, NombreClienteLegal, NumeroIdentidadCliente, NombreComercial, DireccionNegocio, Motivo, Beneficio, Fecha, Introduccion, Ruta,
            Pepsi6_5oz_cant, Pepsi6_5oz_precio,
            Pepsi12oz_cant, Pepsi12oz_precio,
            Pepsi500ml_cant, Pepsi500ml_precio,
            Pepsi1_25lts_cant, Pepsi1_25lts_precio,
            MirindaN12oz_cant, MirindaN12oz_precio,
            MirindaB12oz_cant, MirindaB12oz_precio,
            MirindaU12oz_cant, MirindaU12oz_precio,
            MirindaN1_25lts_cant, MirindaN1_25lts_precio,
            sevenup12oz_cant, sevenup12oz_precio,
            teem12oz_cant, teem12oz_precio,
            LinkM6_5oz_cant, LinkM6_5oz_precio,
            LinkB6_5oz_cant, LinkB6_5oz_precio,
            LinkC6_5oz_cant, LinkC6_5oz_precio
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(consulta, cod_cliente, nombre_cliente, identidad, nombre_negocio, direccion, motivo, beneficio, fecha, introduccion, ruta,
                       Pepsi6_5oz_cant, Pepsi6_5oz_precio,
                       Pepsi12oz_cant, Pepsi12oz_precio,
                       Pepsi500ml_cant, Pepsi500ml_precio,
                       Pepsi1_25lts_cant, Pepsi1_25lts_precio,
                       MirindaN12oz_cant, MirindaN12oz_precio,
                       MirindaB12oz_cant, MirindaB12oz_precio,
                       MirindaU12oz_cant, MirindaU12oz_precio,
                       MirindaN1_25lts_cant, MirindaN1_25lts_precio,
                       sevenup12oz_cant, sevenup12oz_precio,
                       teem12oz_cant, teem12oz_precio,
                       LinkM6_5oz_cant, LinkM6_5oz_precio,
                       LinkB6_5oz_cant, LinkB6_5oz_precio,
                       LinkC6_5oz_cant, LinkC6_5oz_precio)
        
        # Confirmar los cambios
        conexion.commit()
        
        # Cerrar la conexión
        cursor.close()
        conexion.close()

        return jsonify({"mensaje": "Datos guardados exitosamente."}), 200

    except Exception as e:
        return jsonify({"mensaje": f"Error al guardar los datos: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
