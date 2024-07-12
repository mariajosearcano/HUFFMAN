
import os
from collections import Counter

# Leer archivos y almacenar su valor en una cadena
def readFile(path, type):
    with open(path, type) as f:
        text = f.read()
        f.close()
    return text

# Clase nodo
class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency
    
# Construccion del arbol
def buildTree(frequencies):
    queue = []
    # Creacion de lista que contiene los nodos
    for character, frequency in frequencies.items():
        node = Node(character, frequency)
        queue.append(node)
    queue.sort()
    # Creacion de nodos hasta llegar al nodo raiz
    while len(queue) > 1:
        node = queue.pop(0)
        node1 = queue.pop(0)
        newNode = Node(None, node.frequency + node1.frequency)
        newNode.left = node
        newNode.right = node1
        queue.append(newNode)
        queue.sort()
    return queue[0]

# Creacion y guardado de los codigos huffman de cada caracter
def generateCodes(node, currentCode="", codes={}):
    if node.character:
        codes[node.character] = currentCode
    if node.left:
        generateCodes(node.left, currentCode + "0", codes)
    if node.right:
        generateCodes(node.right, currentCode + "1", codes)

# Impresion de cada caracter con el codigo huffman
def impression():
    print("Carácter y su respectivo código: ")
    for character, code in codes.items():
        if character == "\n":
            print(f"salto: {code}")
        elif character == " ":
            print(f"esp: {code}")
        elif character == "\xad":
            print(f"soft: {code}")
        else:
            print(f"{character}: {code}")
    print()

# Proceso de compresion (codificacion) del texto
def encodeText(text):
    frequencies = Counter(text) #para contar las frecuencias de los caracteres en una cadena de texto
    tree = buildTree(frequencies)
    generateCodes(tree, "", codes)
    encodedText = "".join(codes[character] for character in text)
    return encodedText

codes = {}

# Calcular los bits extra necesarios para formatear correctamente y agregar dicha informacion
def addBits(encodedText):
    bits = 8 - len(encodedText) % 8
    for i in range(bits):
        encodedText += "0"

    extraBitsInfo = "{0:08b}".format(bits)
    encodedTextPlus = extraBitsInfo + encodedText
    return encodedTextPlus

# Formatear la cadena a bytes
def formatting(encodedTextPlus):
    b = bytearray()
    for i in range(0, len(encodedTextPlus), 8):
        byte = encodedTextPlus[i:i+8]
        b.append(int(byte, 2))
    return b

# Escribir texto en archivo
def writeFile(path, text, type):
  with open(path, type) as f:
    f.write(text)
    f.close()


def compress():
    # Ruta archivo a descomprimir
    path = "archivos/archivo.txt"

    # Verificacion de que el archivo exista y tenga datos
    try:
        fileSize = os.path.getsize(path)
        if  fileSize == 0:
            print("Se necesita llenar el archivo primero 📄✏️")
            print(f"En la direccion: HUFFMAN/{path}")
            return
    except FileNotFoundError as e:
        print("Se necesita crear el archivo primero 📃❗️")
        print(f"En la direccion: HUFFMAN/{path[:9]}")
        return

    # Obtener texto archivo y almacenar en un string
    text = readFile(path, "r")
    print(f"La ruta del archivo a comprimir es: HUFFMAN/{path}")

    # Tama;o archivo original
    size = os.stat(path).st_size
    print(f"El tamaño del archivo es: {size} bytes")
    print()

    # Codificacion del texto
    encodedText = encodeText(text)
    # Impresion de cada caracter con el codigo huffman
    impression()

    # Texto multiplo de 8 e informacion
    encodedTextPlus = addBits(encodedText)
    # Formateo del texto a binario
    b = formatting(encodedTextPlus)
    bF = bytes(b)

    # Escribir texto codificado en archivo
    path = "archivos/archivoComprimido.bin"
    writeFile(path, bF, "wb") #wb escritura bytes
    print(f"La ruta del archivo comprimido es: HUFFMAN/{path}")
    
    # Tama;o archivo comprimido
    size = os.stat(path).st_size
    print(f"El tamaño del archivo comprimido es: {size} bytes")