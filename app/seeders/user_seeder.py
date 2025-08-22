from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password
from app.db.session import SessionLocal


def create_base_user(db: Session) -> User:
    """
    Crea un usuario base/administrador por defecto
    """
    # Verificar si ya existe un usuario con el email o username
    existing_user = db.query(User).filter(
        (User.email == "admin@example.com") | (User.username == "admin")
    ).first()
    
    if existing_user:
        print("El usuario base ya existe")
        return existing_user
    
    # Crear el usuario base
    base_user = User(
        first_name="Administrador",
        last_name="Sistema",
        username="admin",
        email="admin@example.com",
        password=hash_password("admin123"),  # Contraseña por defecto
        is_active=True
    )
    
    db.add(base_user)
    db.commit()
    db.refresh(base_user)
    
    print(f"Usuario base creado exitosamente: {base_user}")
    return base_user


def create_custom_user(
    db: Session,
    first_name: str,
    last_name: str,
    username: str,
    email: str,
    password: str,
    is_active: bool = True
) -> User:
    """
    Crea un usuario personalizado
    """
    # Verificar si ya existe un usuario con el email o username
    existing_user = db.query(User).filter(
        (User.email == email) | (User.username == username)
    ).first()
    
    if existing_user:
        print(f"El usuario con email {email} o username {username} ya existe")
        return existing_user
    
    # Crear el usuario
    user = User(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=hash_password(password),
        is_active=is_active
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    print(f"Usuario creado exitosamente: {user}")
    return user


def run_user_seeder():
    """
    Ejecuta el seeder de usuarios
    """
    db = SessionLocal()
    try:
        # Crear usuario base
        create_base_user(db)
        
        # Opcional: crear usuarios adicionales de ejemplo
        # create_custom_user(
        #     db=db,
        #     first_name="Juan",
        #     last_name="Pérez",
        #     username="juanperez",
        #     email="juan.perez@example.com",
        #     password="password123"
        # )
        
        print("Seeder de usuarios ejecutado exitosamente")
        
    except Exception as e:
        print(f"Error ejecutando el seeder: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    run_user_seeder()
