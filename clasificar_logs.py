import os
import shutil

carpeta = r"C:\Users\kathe\OneDrive\Escritorio\Segundo año\Ciclo 8\PROCESOS INFORMÁTICOS\Semana 3\Tarea3\Logs"

for archivo in os.listdir(carpeta):

    ruta_archivo = os.path.join(carpeta, archivo)

    if archivo.endswith(".log_app_1"):
        destino = os.path.join(carpeta, "log_app_1")

    elif archivo.endswith(".log_app_2"):
        destino = os.path.join(carpeta, "log_app_2")

    elif archivo.endswith(".log_app_3"):
        destino = os.path.join(carpeta, "log_app_3")

    else:
        continue

    os.makedirs(destino, exist_ok=True)

    shutil.move(
        ruta_archivo,
        os.path.join(destino, archivo)
    )

print("Clasificación completada")