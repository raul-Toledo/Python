import pyAesCrypt
from os import stat, remove
# Tamaña de buffer para encriptar/desencriptar
bufferSize = 64 * 1024
password = "Semana Ulsa 2019" #Semilla para encriptar
with open("data.txt", "rb") as fIn:
    with open("data.txt.aes", "wb") as fOut:
        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

#Obtenemos el tamaño del archivo encriptado
encFileSize = stat("data.txt.aes").st_size

with open("data.txt.aes", "rb") as fIn:
    try:
        with open("dataout.txt", "wb") as fOut:
            #Desencriptamos el archivo
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
    except ValueError:
        #En caso de error removemos el archivo desencriptado
        remove("dataout.txt")