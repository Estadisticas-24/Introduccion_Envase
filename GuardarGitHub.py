import os
import subprocess

# Cambiar al directorio del proyecto
os.chdir(r'\\ACT_40000008781\ShareEstadisticas\27 Practicantes\Alan Martinez\Prueba A\Introduccion de envase')

# Añadir todos los cambios
subprocess.run(['git', 'add', 'clientes.json', 'index.html', 'logo.png', 'fondo.png'])

# Crear un commit con mensaje
subprocess.run(['git', 'commit', '-m', 'Actualización automática'])

# Hacer push a la rama main
subprocess.run(['git', 'push', 'origin', 'main'])

print("Cambios enviados a GitHub con éxito.")
