# 🛠️ Revisión de Errores en Repositorios de GitHub

Este proyecto permite revisar posibles errores en un repositorio de GitHub de forma automatizada, utilizando patrones simples como prueba inicial. Ideal para testear y ampliar con nuevas reglas o patrones personalizados.

## ⚙️ Características

- Revisión básica de errores a partir de patrones predefinidos.
- Posibilidad de ampliar los patrones mediante un archivo `.txt`.
- Acceso autenticado mediante token personal de GitHub.
- Escaneo de cualquier repositorio público o privado (con permisos adecuados).

## 🔐 Configuración del archivo `.env`

Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:


> El token debe tener permisos de lectura sobre los repositorios que se quieran analizar.

## 📝 Uso del programa

1. Cloná el repositorio:

```bash
git clone https://github.com/tu-usuario/nombre-del-repo.git
cd nombre-del-repo


python revisar_repo.py --repo usuario/nombre-repo
