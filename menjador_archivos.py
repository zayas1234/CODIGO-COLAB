import os

def count_lines_words_chars(file_path):

    lines = 0
    words = 0
    chars = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            lines += 1
            words += len(line.split())
            chars += len(line)
    
    return {
        'lines': lines,
        'words': words,
        'characters': chars
    }

def create_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Archivo '{file_path}' creado exitosamente.")

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"\ncontenido de '{file_path}':\n{'-'*40}\n{content}\n{'-'*40}")
    except FileNotFoundError:
        print(f"error: el archivo '{file_path}' no existe.")

def append_to_file(file_path, content):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content + "\n")
        print(f"contenido añadido a '{file_path}'.")
    except FileNotFoundError:
        print(f"error: el archivo '{file_path}' no existe.")

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"archivo '{file_path}' eliminado.")
    else:
        print(f"error: El archivo '{file_path}' no existe.")

def show_menu():
    print("\n" + "="*40)
    print("GESTOR DE ARCHIVOS DE TEXTO")
    print("="*40)
    print("1. crear archivo")
    print("2. leer archivo")
    print("3. añadir texto a archivo")
    print("4. eliminar archivo")
    print("5. analizar archivo (líneas, palabras, caracteres)")
    print("6. salir")

def main():
    
    while True:
        show_menu()
        option = input("\nSeleccione una opción (1-6): ").strip()
        
        if option == '1':
            file_path = input("ingrese la ruta del archivo a crear: ")
            content = input("ingrese el contenido: ")
            create_file(file_path, content)
        
        elif option == '2':
            file_path = input("ingrese la ruta del archivo a leer: ")
            read_file(file_path)
        
        elif option == '3':
            file_path = input("ingrese la ruta del archivo a modificar: ")
            content = input("ingrese el texto a añadir: ")
            append_to_file(file_path, content)
        
        elif option == '4':
            file_path = input("Ingrese la ruta del archivo a eliminar: ")
            delete_file(file_path)
        
        elif option == '5':
            file_path = input("Ingrese la ruta del archivo a analizar: ")
            if os.path.exists(file_path):
                stats = count_lines_words_chars(file_path)
                print(f"\nestadísticas de '{file_path}':")
                print(f"- líneas: {stats['lines']}")
                print(f"- palabras: {stats['words']}")
                print(f"- caracteres: {stats['characters']}")
            else:
                print(f"error: el archivo '{file_path}' no existe.")
        
        elif option == '6':
            print("gracias por usar el programa")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()