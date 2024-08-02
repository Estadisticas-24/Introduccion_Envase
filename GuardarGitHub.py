import os
import subprocess

# Cambiar al directorio del proyecto
os.chdir(r'\\ACT_40000008781\ShareEstadisticas\27 Practicantes\Alan Martinez\Prueba A\Introduccion de envase')

# Configurar el directorio seguro si es necesario
subprocess.run(['git', 'config', '--global', '--add', 'safe.directory', os.getcwd()])

# Crear o cambiar a la rama main
subprocess.run(['git', 'checkout', '-b', 'main'], stderr=subprocess.DEVNULL)

# Hacer pull para actualizar el repositorio local con la opción --allow-unrelated-histories
subprocess.run(['git', 'pull', 'origin', 'main', '--allow-unrelated-histories'])

# Añadir los archivos específicos si existen
archivos_a_subir = ['clientes.json', 'index.html', 'logo.png', 'fondo.png']
archivos_existentes = [archivo for archivo in archivos_a_subir if os.path.exists(archivo)]

if archivos_existentes:
    subprocess.run(['git', 'add'] + archivos_existentes)
    # Crear un commit con mensaje
    subprocess.run(['git', 'commit', '-m', 'Actualización automática de archivos específicos'])
    # Hacer push forzado a la rama main
    subprocess.run(['git', 'push', '--force', 'origin', 'main'])
    print("Cambios enviados a GitHub con éxito.")
else:
    print("No hay archivos para añadir.")
