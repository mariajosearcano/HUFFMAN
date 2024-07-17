
import compression
import decompression
import time

def about():
    print("Compresor con el Algoritmo de Huffman")
    print("Versión: 1.0")
    print("Autor: Maria Jose Arcila Cano")

print()
print("🔑 Bienvenido al Compresor con el Algoritmo de Huffman 🗜️")

selection = ""
while selection != "0":
    print()
    print("                    🌳       🌳       🌳                 ")
    print()
    print("👇 Escoge una opción:")
    print("1. 🔰 Comprimir archivo")
    print("2. 📥 Descomprimir archivo")
    print("3. ❓ Acerca de")
    print("0. 🚪 Salir")
    selection = input("=> ")
    print()

    match selection:
        case "1":
            compression.compress()
        case "2":
            decompression.decompress()
        case "3":
            about()
        case "0":
            print("Hasta la próxima 👋")
            print()
        case _:
            print("Opción no válida ❌")


