import os
import re
from github import Github
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene el token desde la variable de entorno
token = os.getenv('GITHUB_TOKEN')

# Inicializa GitHub con el token
g = Github(token)

# Función para cargar patrones desde un archivo de texto
def cargar_patrones(archivo):
    with open(archivo, 'r') as f:
        return [linea.strip() for linea in f if linea.strip()]

# Función para buscar posibles datos sensibles en el texto
def buscar_datos_sensibles(texto, patrones):
    resultados = []
    for patron in patrones:
        if re.search(patron, texto):
            resultados.append(patron)  # Guarda el patrón que coincide
    return resultados

# Función recursiva para buscar datos sensibles en los archivos de un repositorio
def obtener_datos_sensibles_repo(repo, patrones, path=""):
    contents = repo.get_contents(path)
    for file_content in contents:
        if file_content.type == "dir":
            obtener_datos_sensibles_repo(repo, patrones, file_content.path)  # Recursión para entrar a subdirectorios
        else:
            try:
                # Obtiene el contenido del archivo
                content = file_content.decoded_content.decode('utf-8')
                
                # Busca datos sensibles en el contenido del archivo
                resultados = buscar_datos_sensibles(content, patrones)
                if resultados:
                    # Imprime los datos sensibles encontrados junto con la ubicación del archivo
                    for patron in resultados:
                        coincidencias = re.findall(patron, content)
                        for coincidencia in coincidencias:
                            print(f"Dato sensible encontrado: '{coincidencia}' en {file_content.path}\n")
            except Exception as e:
                print(f"No se pudo leer el archivo {file_content.path}: {e}")

# Nombre del repositorio en el formato 'usuario/repositorio'
repo_name = "Santiago-sz/frontendnutri"

# Obtiene el repositorio por nombre
repo = g.get_repo(repo_name)

# Cargar patrones desde el archivo patrones.txt
patrones = cargar_patrones('patrones.txt')

# Llama a la función para buscar datos sensibles
obtener_datos_sensibles_repo(repo, patrones)

