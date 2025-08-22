from app.seeders.user_seeder import run_user_seeder


def run_all_seeders():
    """
    Ejecuta todos los seeders disponibles
    """
    print("=== Iniciando ejecución de seeders ===")
    
    # Ejecutar seeder de usuarios
    print("\n--- Ejecutando seeder de usuarios ---")
    run_user_seeder()
    
    # Aquí puedes agregar más seeders cuando los crees
    # print("\n--- Ejecutando seeder de marcas ---")
    # run_brand_seeder()
    
    print("\n=== Todos los seeders han sido ejecutados ===")


if __name__ == "__main__":
    run_all_seeders()
