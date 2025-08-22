# 🚀 FastAPI Init - API con Autenticación OAuth2 y Sistema de Auditoría

Una aplicación FastAPI completa con autenticación OAuth2, sistema de auditoría, y configuración lista para producción con Docker.

## ✨ Características

- 🔐 **Autenticación OAuth2** con JWT tokens
- 📊 **Sistema de auditoría** completo
- 🏢 **Gestión de marcas** (brands)
- 👥 **Gestión de usuarios**
- 🐳 **Docker** y **Docker Compose** listos
- 🌐 **Nginx** como proxy reverso
- 🔒 **SSL/HTTPS** con Let's Encrypt
- 📝 **Documentación automática** con Swagger/OpenAPI
- 🧪 **Tests** con pytest
- 🔧 **Migraciones** con Alembic

## 🏗️ Arquitectura

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Cliente   │───▶│    Nginx    │───▶│   FastAPI   │
└─────────────┘    └─────────────┘    └─────────────┘
                          │                    │
                          ▼                    ▼
                   ┌─────────────┐    ┌─────────────┐
                   │  Certbot    │    │ PostgreSQL  │
                   │ (SSL/HTTPS) │    │  Database   │
                   └─────────────┘    └─────────────┘
```

## 🚀 Inicio Rápido

### Desarrollo Local

1. **Clonar el repositorio:**
```bash
git clone <tu-repositorio>
cd fast-api-init
```

2. **Configurar variables de entorno:**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

3. **Ejecutar con Docker:**
```bash
docker-compose up -d --build
```

4. **Acceder a la aplicación:**
- API: http://localhost:8000
- Documentación: http://localhost/docs
- Health Check: http://localhost/health

### Despliegue en VPS

Ver [DEPLOYMENT.md](./DEPLOYMENT.md) para instrucciones completas de despliegue en producción.

```bash
# Despliegue rápido
chmod +x deploy.sh
./deploy.sh tu-dominio.com
```

## 📋 Endpoints Disponibles

### 🔐 Autenticación
- `POST /auth/login` - Login con email y contraseña
- `POST /auth/login-oauth` - Login OAuth2
- `POST /auth/register` - Registro de usuarios
- `GET /auth/me` - Información del usuario actual

### 👥 Usuarios
- `GET /users/` - Listar usuarios
- `GET /users/{id}` - Obtener usuario específico
- `PUT /users/{id}` - Actualizar usuario
- `DELETE /users/{id}` - Eliminar usuario

### 🏢 Marcas
- `GET /brands/` - Listar marcas
- `POST /brands/` - Crear marca
- `GET /brands/{id}` - Obtener marca específica
- `PUT /brands/{id}` - Actualizar marca
- `DELETE /brands/{id}` - Eliminar marca

### 📊 Auditoría
- `GET /audit/` - Listar registros de auditoría
- `GET /audit/{id}` - Obtener registro específico

## 🔧 Configuración

### Variables de Entorno

```env
# Base de datos
DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_db

# Seguridad
SECRET_KEY=tu_clave_secreta_muy_larga_y_segura
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Dominio
DOMAIN=tu-dominio.com
```

### Base de Datos

La aplicación usa PostgreSQL con las siguientes tablas principales:
- `users` - Usuarios del sistema
- `brands` - Marcas/empresas
- `audit_logs` - Registros de auditoría

## 🐳 Docker

### Servicios

- **api**: Aplicación FastAPI (puerto 8000)
- **nginx**: Proxy reverso (puertos 80, 443)
- **certbot**: Certificados SSL automáticos

### Comandos Útiles

```bash
# Construir y levantar
docker-compose up -d --build

# Ver logs
docker-compose logs -f api

# Reiniciar servicios
docker-compose restart

# Detener todo
docker-compose down
```

## 🧪 Testing

```bash
# Ejecutar tests
docker-compose exec api pytest

# Tests con cobertura
docker-compose exec api pytest --cov=app

# Tests específicos
docker-compose exec api pytest tests/test_auth.py
```

## 📊 Monitoreo

### Health Check
```bash
curl http://localhost/health
```

### Logs
```bash
# Logs de la API
docker-compose logs -f api

# Logs de Nginx
docker-compose logs -f nginx

# Logs de Certbot
docker-compose logs -f certbot
```

## 🔒 Seguridad

- ✅ Autenticación JWT
- ✅ Contraseñas hasheadas con bcrypt
- ✅ CORS configurado
- ✅ Headers de seguridad
- ✅ Rate limiting (configurable)
- ✅ Auditoría completa de acciones

## 🚀 Despliegue en Producción

### Requisitos
- VPS con Ubuntu 20.04+
- Docker y Docker Compose
- Dominio configurado (opcional)

### Pasos
1. Clonar el repositorio en el servidor
2. Ejecutar `./deploy.sh tu-dominio.com`
3. Configurar variables de entorno
4. Obtener certificados SSL (automático)

Ver [DEPLOYMENT.md](./DEPLOYMENT.md) para detalles completos.

## 📝 Desarrollo

### Estructura del Proyecto

```
fast-api-init/
├── app/
│   ├── core/           # Configuración y utilidades
│   ├── db/            # Base de datos y sesiones
│   ├── dependencies/  # Dependencias de FastAPI
│   ├── models/        # Modelos SQLAlchemy
│   ├── repositories/  # Capa de acceso a datos
│   ├── routers/       # Endpoints de la API
│   ├── schemas/       # Esquemas Pydantic
│   ├── services/      # Lógica de negocio
│   └── main.py        # Aplicación principal
├── docker/            # Configuración de Docker
├── alembic/           # Migraciones de base de datos
├── tests/             # Tests unitarios
├── requirements.txt   # Dependencias Python
├── docker-compose.yml # Orquestación de contenedores
└── deploy.sh         # Script de despliegue
```

### Agregar Nuevos Endpoints

1. Crear router en `app/routers/`
2. Definir esquemas en `app/schemas/`
3. Crear modelo en `app/models/`
4. Agregar repositorio en `app/repositories/`
5. Incluir router en `app/main.py`

## 🤝 Contribuir

1. Fork el proyecto
2. Crear rama para feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 🆘 Soporte

Si encuentras problemas:

1. Revisa los logs: `docker-compose logs`
2. Verifica la configuración: `docker-compose config`
3. Consulta la documentación de la API: http://localhost/docs
4. Abre un issue en el repositorio

## 🎯 Estado Actual

✅ **Completado:**
- Configuración Docker completa
- API FastAPI funcional
- Sistema de autenticación OAuth2
- Sistema de auditoría
- Proxy reverso con Nginx
- Configuración SSL con Certbot
- Script de despliegue automático
- Documentación completa
- Health check endpoint
- Configuración para VPS

🚀 **Listo para producción en VPS**
