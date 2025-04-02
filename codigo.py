

from google.colab import drive  
import os  

# Montar Google Drive  
drive.mount('/content/drive')  

# Definir el directorio (cambia 'tu_directorio' por el nombre de tu carpeta)  
directory = '/content/drive/My Drive/tu_directorio'  

# Listar archivos en el directorio  
def list_files_in_directory(directory):  
    try:  
        files = os.listdir(directory)  
        print("Archivos en el directorio:")  
        for file in files:  
            print(file)  
    except FileNotFoundError:  
        print("Directorio no encontrado.")  

# Llamar a la función  
list_files_in_directory(directory)

