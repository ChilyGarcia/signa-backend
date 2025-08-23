# 🚀 FastAPI - Sistema de Gestión con Autenticación y Auditoría

[![FastAPI](https://img.shields.io/badge/FastAPI-0.103.0+-green.svg)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue.svg)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)](https://docs.docker.com/compose/)
[![Alembic](https://img.shields.io/badge/Alembic-1.12.0+-orange.svg)](https://alembic.sqlalchemy.org/)

Una API REST moderna construida con FastAPI que incluye autenticación OAuth2, sistema de auditoría, gestión de usuarios y marcas, con soporte completo para Docker y migraciones de base de datos.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Prerrequisitos](#-prerrequisitos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Migraciones](#-migraciones)
- [Seeders](#-seeders)
- [Docker](#-docker)
- [Desarrollo](#-desarrollo)
- [API Documentation](#-api-documentation)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

## ✨ Características

- 🔐 **Autenticación OAuth2** con JWT tokens
- 👥 **Gestión de Usuarios** con roles y permisos
- 🏷️ **Gestión de Marcas** con estados y auditoría
- 📊 **Sistema de Auditoría** completo
- 🗄️ **Migraciones de Base de Datos** con Alembic
- 🌱 **Seeders** para datos iniciales
- 🐳 **Docker** y Docker Compose
- 📚 **Documentación Automática** con Swagger/OpenAPI
- 🔒 **Seguridad** con CORS y validación de datos
- 🏥 **Health Checks** para monitoreo
- 🚀 **Producción Ready** con Gunicorn y Nginx

## 🛠️ Tecnologías

### Backend
- **FastAPI** 0.103.0+ - Framework web moderno y rápido
- **SQLAlchemy** 2.0+ - ORM para Python
- **Alembic** 1.12.0+ - Migraciones de base de datos
- **Pydantic** 2.4+ - Validación de datos
- **Passlib** - Hashing de contraseñas
- **Python-Jose** - JWT tokens

### Base de Datos
- **PostgreSQL** 14 - Base de datos principal
- **psycopg2** - Driver de PostgreSQL

### Infraestructura
- **Docker** - Contenedores
- **Docker Compose** - Orquestación
- **Nginx** - Proxy reverso
- **Gunicorn** - Servidor WSGI
- **Certbot** - Certificados SSL

### Desarrollo
- **Pytest** - Testing
- **Black** - Formateo de código
- **Flake8** - Linting
- **isort** - Ordenamiento de imports

## 📋 Prerrequisitos

- Python 3.12+
- Docker y Docker Compose
- Git

## 🚀 Instalación

### Opción 1: Desarrollo Local

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd fast-api-init
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus configuraciones
   ```

5. **Configurar base de datos PostgreSQL**
   - Instalar PostgreSQL 14
   - Crear base de datos `signa`
   - Configurar credenciales en `.env`

### Opción 2: Docker (Recomendado)

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd fast-api-init
   ```

2. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus configuraciones
   ```

## ⚙️ Configuración

### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
# Configuración de la aplicación
APP_NAME=FastAPI
ENVIRONMENT=development

# Base de datos
DATABASE_URL=postgresql://postgres:123@localhost:5432/signa

# Seguridad
SECRET_KEY=tu_clave_secreta_muy_segura_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=20

# Para Docker
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123
POSTGRES_DB=signa
```

## 🏃‍♂️ Uso

### Desarrollo Local

1. **Ejecutar migraciones**
   ```bash
   alembic upgrade head
   ```

2. **Ejecutar seeders**
   ```bash
   python run_seeders.py all
   ```

3. **Iniciar servidor de desarrollo**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Acceder a la documentación**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc
   - Health Check: http://localhost:8000/health

### Docker

1. **Construir e iniciar servicios**
   ```bash
   docker-compose up --build
   ```

2. **Ejecutar migraciones en Docker**
   ```bash
   docker-compose exec api alembic upgrade head
   ```

3. **Ejecutar seeders en Docker**
   ```bash
   docker-compose exec api python run_seeders.py all
   ```

4. **Acceder a la aplicación**
   - API: http://localhost:8000
   - Documentación: http://localhost:8000/docs
   - Nginx: http://localhost:80

## 🗄️ Migraciones

### Comandos Básicos

```bash
# Crear una nueva migración
alembic revision --autogenerate -m "descripción del cambio"

# Aplicar migraciones pendientes
alembic upgrade head

# Revertir última migración
alembic downgrade -1

# Ver historial de migraciones
alembic history

# Ver estado actual
alembic current

# Marcar como aplicada una migración específica
alembic stamp <revision_id>
```

### Migraciones Existentes

El proyecto incluye las siguientes migraciones:

- `081d1eeb5974` - Crear tabla de marcas
- `30a269414553` - Crear tabla de usuarios
- `4c3079a3e835` - Actualizar tabla de marcas con campo created_by
- `61153f7004f4` - Crear tabla de auditoría de marcas
- `b40b6d83542e` - Actualizar marcas con estado pendiente por defecto
- `ba246ea29902` - Crear tabla de marcas (duplicada)
- `bb22d1508fd0` - Actualizar marcas existentes con valores por defecto

### Flujo de Trabajo con Migraciones

1. **Desarrollo**
   ```bash
   # Hacer cambios en los modelos
   # Crear migración automática
   alembic revision --autogenerate -m "nuevo campo en tabla"
   
   # Revisar la migración generada
   # Aplicar migración
   alembic upgrade head
   ```

2. **Producción**
   ```bash
   # Aplicar migraciones pendientes
   alembic upgrade head
   ```

## 🌱 Seeders

### Comandos Disponibles

```bash
# Ejecutar todos los seeders
python run_seeders.py all

# Ejecutar solo seeder de usuarios
python run_seeders.py users

# Ver ayuda
python run_seeders.py help
```

### Seeders Disponibles

- **User Seeder**: Crea usuarios iniciales del sistema
- **Main Seeder**: Coordina la ejecución de todos los seeders

### En Docker

```bash
# Ejecutar seeders en contenedor
docker-compose exec api python run_seeders.py all
```

## 🐳 Docker

### Servicios Incluidos

- **api**: Aplicación FastAPI con Gunicorn
- **db**: Base de datos PostgreSQL
- **nginx**: Proxy reverso y balanceador de carga
- **certbot**: Certificados SSL automáticos

### Comandos Útiles

```bash
# Construir e iniciar todos los servicios
docker-compose up --build

# Ejecutar en segundo plano
docker-compose up -d

# Ver logs
docker-compose logs -f api

# Detener servicios
docker-compose down

# Reconstruir un servicio específico
docker-compose up --build api

# Ejecutar comandos en el contenedor
docker-compose exec api bash
docker-compose exec db psql -U postgres -d signa

# Limpiar volúmenes (¡CUIDADO! Borra datos)
docker-compose down -v
```

### Variables de Entorno para Docker

```env
# Docker Compose usa las mismas variables que el archivo .env
# Asegúrate de que DATABASE_URL apunte al servicio de Docker
DATABASE_URL=postgresql://postgres:123@db:5432/signa
```

## 🛠️ Desarrollo

### Estructura del Proyecto

```
fast-api-init/
├── alembic/                 # Migraciones de base de datos
│   ├── versions/           # Archivos de migración
│   └── env.py             # Configuración de Alembic
├── app/                    # Código de la aplicación
│   ├── core/              # Configuración y utilidades
│   ├── db/                # Configuración de base de datos
│   ├── dependencies/      # Dependencias de FastAPI
│   ├── models/            # Modelos SQLAlchemy
│   ├── repositories/      # Capa de acceso a datos
│   ├── routers/           # Endpoints de la API
│   ├── schemas/           # Esquemas Pydantic
│   ├── seeders/           # Datos iniciales
│   └── services/          # Lógica de negocio
├── docker/                # Configuración de Docker
├── requirements.txt       # Dependencias de Python
├── docker-compose.yml     # Orquestación de servicios
├── Dockerfile            # Imagen de la aplicación
├── alembic.ini           # Configuración de Alembic
└── run_seeders.py        # Script para ejecutar seeders
```

### Endpoints Principales

#### Autenticación
- `POST /auth/login` - Login con email y contraseña
- `POST /auth/login-oauth` - Login OAuth2
- `POST /auth/register` - Registro de usuarios

#### Usuarios
- `GET /users/me` - Obtener perfil del usuario actual
- `GET /users/` - Listar usuarios (admin)
- `POST /users/` - Crear usuario (admin)
- `PUT /users/{id}` - Actualizar usuario
- `DELETE /users/{id}` - Eliminar usuario

#### Marcas
- `GET /brands/` - Listar marcas
- `POST /brands/` - Crear marca
- `GET /brands/{id}` - Obtener marca específica
- `PUT /brands/{id}` - Actualizar marca
- `DELETE /brands/{id}` - Eliminar marca

#### Auditoría
- `GET /audit/brands` - Historial de auditoría de marcas
- `GET /audit/users` - Historial de auditoría de usuarios

### Testing

```bash
# Ejecutar tests
pytest

# Con cobertura
pytest --cov=app

# Tests específicos
pytest tests/test_auth.py
```

### Formateo de Código

```bash
# Formatear con Black
black app/

# Ordenar imports
isort app/

# Linting
flake8 app/
```

## 📚 API Documentation

### Swagger UI
Accede a la documentación interactiva en: http://localhost:8000/docs

### ReDoc
Documentación alternativa en: http://localhost:8000/redoc

### Autenticación
La API utiliza OAuth2 con JWT tokens. Para autenticarte:

1. Ve a `/docs`
2. Haz clic en "Authorize"
3. Usa el endpoint `/auth/login-oauth`
4. Ingresa tus credenciales
5. Usa el token JWT en las siguientes peticiones

### Ejemplo de Uso

```bash
# Login
curl -X POST "http://localhost:8000/auth/login-oauth" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin@example.com&password=password123"

# Usar token
curl -X GET "http://localhost:8000/users/me" \
  -H "Authorization: Bearer <tu_token_jwt>"
```

## 🔧 Troubleshooting

### Problemas Comunes

1. **Error de conexión a base de datos**
   ```bash
   # Verificar que PostgreSQL esté corriendo
   # Verificar variables de entorno
   # Verificar credenciales
   ```

2. **Migraciones fallan**
   ```bash
   # Verificar estado actual
   alembic current
   
   # Revisar migraciones pendientes
   alembic history
   
   # Forzar migración específica
   alembic stamp <revision_id>
   ```

3. **Docker no inicia**
   ```bash
   # Verificar puertos disponibles
   # Limpiar contenedores
   docker-compose down
   docker system prune
   ```

4. **Seeders fallan**
   ```bash
   # Verificar conexión a base de datos
   # Verificar que las tablas existan
   # Ejecutar migraciones primero
   ```

### Logs

```bash
# Ver logs de la aplicación
docker-compose logs -f api

# Ver logs de la base de datos
docker-compose logs -f db

# Ver logs de nginx
docker-compose logs -f nginx
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Guías de Contribución

- Sigue las convenciones de código existentes
- Añade tests para nuevas funcionalidades
- Actualiza la documentación cuando sea necesario
- Usa commits descriptivos

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si tienes preguntas o problemas:

1. Revisa la documentación
2. Busca en los issues existentes
3. Crea un nuevo issue con detalles del problema

---

**¡Gracias por usar FastAPI! 🚀**
