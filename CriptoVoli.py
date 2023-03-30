import os
from colorama import Fore, Style, init
init()
from cryptography.fernet import Fernet
# Generamos una clave para encriptar los archivos
clave = Fernet.generate_key()

# Creamos un objeto Fernet con la clave generada
fernet = Fernet(clave)
print(f"""{Fore.BLUE}
        CCCCCCCCCCCCC                     iiii                              tttt                        VVVVVVVV           VVVVVVVV              lllllll   iiii  
     CCC::::::::::::C                    i::::i                          ttt:::t                        V::::::V           V::::::V              l:::::l  i::::i 
   CC:::::::::::::::C                     iiii                           t:::::t                        V::::::V           V::::::V              l:::::l   iiii  
  C:::::CCCCCCCC::::C                                                    t:::::t                        V::::::V           V::::::V              l:::::l         
 C:::::C       CCCCCCrrrrr   rrrrrrrrr  iiiiiiippppp   ppppppppp   ttttttt:::::ttttttt       ooooooooooo V:::::V           V:::::V ooooooooooo    l::::l iiiiiii 
C:::::C              r::::rrr:::::::::r i:::::ip::::ppp:::::::::p  t:::::::::::::::::t     oo:::::::::::ooV:::::V         V:::::Voo:::::::::::oo  l::::l i:::::i 
C:::::C              r:::::::::::::::::r i::::ip:::::::::::::::::p t:::::::::::::::::t    o:::::::::::::::oV:::::V       V:::::Vo:::::::::::::::o l::::l  i::::i 
C:::::C              rr::::::rrrrr::::::ri::::ipp::::::ppppp::::::ptttttt:::::::tttttt    o:::::ooooo:::::o V:::::V     V:::::V o:::::ooooo:::::o l::::l  i::::i 
C:::::C               r:::::r     r:::::ri::::i p:::::p     p:::::p      t:::::t          o::::o     o::::o  V:::::V   V:::::V  o::::o     o::::o l::::l  i::::i 
C:::::C               r:::::r     rrrrrrri::::i p:::::p     p:::::p      t:::::t          o::::o     o::::o   V:::::V V:::::V   o::::o     o::::o l::::l  i::::i 
C:::::C               r:::::r            i::::i p:::::p     p:::::p      t:::::t          o::::o     o::::o    V:::::V:::::V    o::::o     o::::o l::::l  i::::i 
 C:::::C       CCCCCC r:::::r            i::::i p:::::p    p::::::p      t:::::t    tttttto::::o     o::::o     V:::::::::V     o::::o     o::::o l::::l  i::::i 
  C:::::CCCCCCCC::::C r:::::r           i::::::ip:::::ppppp:::::::p      t::::::tttt:::::to:::::ooooo:::::o      V:::::::V      o:::::ooooo:::::ol::::::li::::::i
   CC:::::::::::::::C r:::::r           i::::::ip::::::::::::::::p       tt::::::::::::::to:::::::::::::::o       V:::::V       o:::::::::::::::ol::::::li::::::i
     CCC::::::::::::C r:::::r           i::::::ip::::::::::::::pp          tt:::::::::::tt oo:::::::::::oo         V:::V         oo:::::::::::oo l::::::li::::::i
        CCCCCCCCCCCCC rrrrrrr           iiiiiiiip::::::pppppppp              ttttttttttt     ooooooooooo            VVV            ooooooooooo   lllllllliiiiiiii
                                                p:::::p                                                                                                          
                                                p:::::p                                                                                                          
                                               p:::::::p                                                                                                         
                                               p:::::::p                                                                                                         
                                               p:::::::p                                                                                                         
                                               ppppppppp
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
