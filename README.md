# FastAPI Project

## Descripción

Este es un proyecto backend desarrollado con FastAPI, un moderno framework web para construir APIs con Python 3.7+ basado en estándares de OpenAPI.

## Características

- Operaciones CRUD completas
- Autenticación y autorización con JWT
- Documentación automática (Swagger UI)
- Validación de datos con Pydantic
- Estructura modular y escalable
- ORM con SQLAlchemy

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn (servidor ASGI)
- SQLAlchemy (ORM)
- Pydantic
- Otras dependencias en `requirements.txt`

## Instalación

1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd fast-api
```

2. Crear un entorno virtual

```bash
python -m venv venv
```

3. Activar el entorno virtual

- En Windows:

```bash
.\venv\Scripts\activate
```

- En macOS/Linux:

```bash
source venv/bin/activate
```

4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración

1. Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```
DATABASE_URL=postgresql://user:password@postgresserver/db
SECRET_KEY=tu_clave_secreta_para_jwt
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Ejecución

1. Iniciar el servidor de desarrollo

```bash
uvicorn app.main:app --reload
```

2. Acceder a la API en [http://localhost:8000](http://localhost:8000)
3. Documentación Swagger UI en [http://localhost:8000/docs](http://localhost:8000/docs)
4. Documentación ReDoc en [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Estructura del Proyecto

```
fast-api/
│
├── app/                    # Código principal de la aplicación
│   ├── api/                # Endpoints de la API
│   │   ├── dependencies/   # Dependencias para endpoints
│   │   ├── routes/         # Rutas de la API organizadas por recursos
│   │   └── api.py          # Router principal de la API
│   ├── core/               # Configuración central (config, security)
│   │   ├── config.py       # Configuración de la aplicación
│   │   └── security.py     # Funciones relacionadas con seguridad
│   ├── db/                 # Definiciones y configuración de la base de datos
│   │   ├── base_class.py   # Clase base para modelos
│   │   └── session.py      # Configuración de la sesión de BD
│   ├── models/             # Modelos SQLAlchemy
│   ├── schemas/            # Esquemas Pydantic
│   ├── crud/               # Operaciones CRUD
│   └── main.py             # Punto de entrada principal
│
├── tests/                  # Pruebas
├── .env                    # Variables de entorno (no commitear)
├── .gitignore              # Archivos a ignorar por Git
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Este archivo
```

## Pruebas

```bash
pytest
```

Para ejecutar pruebas con cobertura:

```bash
pytest --cov=app tests/
```

## Despliegue

### Docker

1. Construir la imagen

```bash
docker build -t fast-api-app .
```

2. Ejecutar el contenedor

```bash
docker run -d -p 8000:8000 --name fastapi-container fast-api-app
```

## Documentación API

La documentación completa de la API está disponible en:

- **Swagger UI**: `/docs`
- **ReDoc**: `/redoc`

## Contribuir

1. Hacer fork del proyecto
2. Crear una rama para tu característica (`git checkout -b feature/amazing-feature`)
3. Confirmar cambios (`git commit -m 'Add some amazing feature'`)
4. Subir la rama (`git push origin feature/amazing-feature`)
5. Abrir un Pull Request

## Licencia

Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.

## Contacto

Tu Nombre - [@tu_twitter](https://twitter.com/tu_twitter) - email@example.com

Enlace del proyecto: [https://github.com/tu-usuario/fast-api](https://github.com/tu-usuario/fast-api)
