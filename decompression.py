
import os
from compression import writeFile
from compression import codes

# Eliminar los bits extra e info del texto codificado obtenido del archivo
def removeExtraBits(encodedTextPlus):
    extraBitsInfo = encodedTextPlus.lstrip('b')
    extraBitsInfo = encodedTextPlus[:8]
    extraBits = int(extraBitsInfo, 2)

    encodedTextPlus = encodedTextPlus[8:] 
    encodedText = encodedTextPlus[:-1*extraBits]

    return encodedText

# Decodificar texto del archivo comprimido
def decodeText(encodedText, codes):
    decodedText = ""
    code = ""
    for digit in encodedText:
        code += digit
        for codedLetter in codes.items():
            if code == codedLetter[1]:
                decodedText += codedLetter[0]
                code = ""
    return decodedText

# Para leer especificamente archivos binarios
def readFile(path):
    with open(path, "rb") as f:
        byte = f.read(1)
        bitString = ""
        while(len(byte) > 0):
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            bitString += bits
            byte = f.read(1)
    return bitString


def decompress():
    # Ruta archivo comprimido
    path = "archivos/archivoComprimido.bin"

    # Verificacion de que se haya comprimido antes el archivo
    try:
        message = "Se necesita comprimir el archivo primero 📚❗️"
        fileSize = os.path.getsize(path)
        if  fileSize == 0:
            print(message)
            return
    except FileNotFoundError as e:
        print(message)
        return
    
    # Leer texto de archivo comprimido
    encodedTextPlus = readFile(path)
    # Quitar bits extras del texto codificado
    encodedText = removeExtraBits(encodedTextPlus)
    # Obtener texto decodificado
    decodedtext = decodeText(encodedText, codes)

    path = "archivos/archivoDescomprimido.txt"
    # Escribir texto decodificado en archivo
    writeFile(path, decodedtext, "w")
    print(f"La ruta del archivo descomprimido es: HUFFMAN/{path}")

    # Tama;o archivo descomprimido
    size = os.stat(path).st_size
    print(f"El tamaño del archivo descomprimido es: {size} bytes")


