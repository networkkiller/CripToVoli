import os
from colorama import Fore, Style, init
init()
from cryptography.fernet import Fernet
# Generamos una clave para encriptar los archivos
clave = Fernet.generate_key()

# Creamos un objeto Fernet con la clave generada
fernet = Fernet(clave)
print(f"""{Fore.BLUE}
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
carpeta_a_encriptar = input("Ruta que decea encriptar: ")

for ruta, directorios, archivos in os.walk(carpeta_a_encriptar):
    for archivo in archivos:
        # Leemos el archivo que queremos encriptar
        ruta_archivo = os.path.join(ruta, archivo)
        with open(ruta_archivo, "rb") as archivo_original:
            datos = archivo_original.read()

        # Encriptamos los datos del archivo
        datos_encriptados = fernet.encrypt(datos)

        # Escribimos los datos encriptados en el mismo archivo
        with open(ruta_archivo, "wb") as archivo_encriptado:
            archivo_encriptado.write(datos_encriptados)

#with open("clave.txt", "wb") as archivo_clave:
    #archivo_clave.write(clave)

print("Carpeta encriptada exitosamente.")

print("la llave de cifrador es la siguiente (dentro de las comillas): ",clave)
print("Porfavor guardar esta clave de manera segura (ojo, esta clave solo funcionara para desencriptar la ruta cifrada una vez.)")
