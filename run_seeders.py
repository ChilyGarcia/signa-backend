#!/usr/bin/env python3
"""
Script para ejecutar seeders de la aplicación
"""

import sys
import os

# Agregar el directorio raíz al path para importar módulos de la app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from app.seeders.main_seeder import run_all_seeders
    from app.seeders.user_seeder import run_user_seeder
except ImportError as e:
    print(f"Error importando módulos: {e}")
    print("Asegúrate de estar ejecutando el script desde el directorio raíz")
    sys.exit(1)


def main():
    """
    Función principal que maneja los argumentos de línea de comandos
    """
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "users" or command == "user":
            print("Ejecutando seeder de usuarios...")
            run_user_seeder()
        elif command == "all":
            print("Ejecutando todos los seeders...")
            run_all_seeders()
        elif command == "help" or command == "--help" or command == "-h":
            print_help()
        else:
            print(f"Comando '{command}' no reconocido.")
            print_help()
    else:
        print("Ejecutando todos los seeders por defecto...")
        run_all_seeders()


def print_help():
    """
    Muestra la ayuda del script
    """
    print("""
Uso: python run_seeders.py [comando]

Comandos disponibles:
  users, user    - Ejecuta solo el seeder de usuarios
  all            - Ejecuta todos los seeders disponibles
  help, --help   - Muestra esta ayuda

Ejemplos:
  python run_seeders.py users
  python run_seeders.py all
  python run_seeders.py help
    """)


if __name__ == "__main__":
    main()
