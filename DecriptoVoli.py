import os
from cryptography.fernet import Fernet
from colorama import Fore, Style, init
init()
print(f"""{Fore.RED}
     ██████████                                              █████   █████            █████           
░░███░░░░░█                                             ░░███   ░░███            ░░███            
 ░███  █ ░  █████ █████  ██████  ████████  █████ ████    ░███    ░███   ██████   ███████    █████ 
 ░██████   ░░███ ░░███  ███░░███░░███░░███░░███ ░███     ░███████████  ░░░░░███ ░░░███░    ███░░  
 ░███░░█    ░███  ░███ ░███████  ░███ ░░░  ░███ ░███     ░███░░░░░███   ███████   ░███    ░░█████ 
 ░███ ░   █ ░░███ ███  ░███░░░   ░███      ░███ ░███     ░███    ░███  ███░░███   ░███ ███ ░░░░███
 ██████████  ░░█████   ░░██████  █████     ░░███████     █████   █████░░████████  ░░█████  ██████ 
░░░░░░░░░░    ░░░░░     ░░░░░░  ░░░░░       ░░░░░███    ░░░░░   ░░░░░  ░░░░░░░░    ░░░░░  ░░░░░░  
                                            ███ ░███                                              
                                           ░░██████                                               
                                            ░░░░░░                  
                                            𝖌𝖎𝖙𝖍𝖚𝖇 Networkkiller
    {Style.RESET_ALL}""")
carpeta_a_desencriptar = input(" Ingrese la ruta a desencriptar: ")
clave = input("Ingrese la clave para desencriptar la carpeta: ")

# Creamos un objeto Fernet con la clave ingresada por el usuario
fernet = Fernet(clave.encode())

# Ruta de la carpeta que queremos desencriptar


# Recorremos todos los archivos y subdirectorios de la carpeta
for ruta, directorios, archivos in os.walk(carpeta_a_desencriptar):
    for archivo in archivos:
        # Leemos el archivo encriptado
        ruta_archivo = os.path.join(ruta, archivo)
        with open(ruta_archivo, "rb") as archivo_encriptado:
            datos_encriptados = archivo_encriptado.read()

        # Desencriptamos los datos del archivo
        datos_desencriptados = fernet.decrypt(datos_encriptados)

        # Escribimos los datos desencriptados en el mismo archivo
        with open(ruta_archivo, "wb") as archivo_desencriptado:
            archivo_desencriptado.write(datos_desencriptados)

# Imprimimos un mensaje indicando que la desencriptación fue exitosa
print("Carpeta desencriptada exitosamente.")
