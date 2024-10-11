import os
from github import Github
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene el token desde la variable de entorno
token = os.getenv('GITHUB_TOKEN')

# Inicializa GitHub con el token
g = Github(token)

# Función recursiva para obtener el contenido de los archivos de un repositorio
def obtener_contenido_repo(repo, path=""):
    contents = repo.get_contents(path)
    for file_content in contents:
        if file_content.type == "dir":
            obtener_contenido_repo(repo, file_content.path)  # Recursión para entrar a subdirectorios
        else:
            try:
                # Imprime el contenido del archivo
                content = file_content.decoded_content.decode('utf-8')
                print(f"Contenido de {file_content.path}:\n")
                print(content)
                print("\n" + "="*50 + "\n")
            except Exception as e:
                print(f"No se pudo leer el archivo {file_content.path}: {e}")

# Nombre del repositorio en el formato 'usuario/repositorio'
repo_name = "Santiago-sz/frontendnutri"

# Obtiene el repositorio por nombre
repo = g.get_repo(repo_name)

# Llama a la función para obtener e imprimir el contenido
obtener_contenido_repo(repo)
