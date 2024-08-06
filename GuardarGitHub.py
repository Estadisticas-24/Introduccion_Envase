import os
import subprocess

# Ruta al directorio del proyecto
project_dir = r'\\ACT_40000008781\ShareEstadisticas\27 Practicantes\Alan Martinez\Prueba A\Introduccion de envase'

# Cambiar al directorio del proyecto
os.chdir(project_dir)

# Inicializar un nuevo repositorio
subprocess.run(['git', 'init'])

# Añadir el repositorio remoto
subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/Estadisticas-24/Introduccion_Envase.git'])

# Añadir todos los archivos
subprocess.run(['git', 'add', '.'])

# Crear un commit
subprocess.run(['git', 'commit', '-m', 'Inicialización del repositorio y carga de todos los archivos'])

# Verificar la existencia de la rama main
branch_result = subprocess.run(['git', 'branch', '-a'], capture_output=True, text=True)
if 'remotes/origin/main' not in branch_result.stdout:
    subprocess.run(['git', 'branch', '-M', 'main'])

# Hacer push de los cambios al repositorio remoto
push_result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], capture_output=True, text=True)

print(push_result.stdout)
print(push_result.stderr)

if push_result.returncode == 0:
    print("Cambios enviados a GitHub con éxito.")
else:
    print("Error al enviar cambios a GitHub. Verifique las credenciales y permisos.")
