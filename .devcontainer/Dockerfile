# Usa una imagen base de Python mantenida por Microsoft para Dev Containers.
# Incluye Python, pip, y muchas herramientas comunes de desarrollo.
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Instala la herramienta de línea de comandos de SQLite para poder inspeccionar
# las bases de datos desde la terminal si es necesario.
RUN sudo apt-get update && sudo apt-get install -y sqlite3
