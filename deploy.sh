#!/bin/bash

# Script de despliegue para VPS
# Uso: ./deploy.sh [DOMINIO]

set -e

DOMAIN=${1:-"TU_DOMINIO.COM"}

echo "🚀 Iniciando despliegue para dominio: $DOMAIN"

# Verificar que Docker y Docker Compose estén instalados
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado. Por favor instala Docker primero."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose no está instalado. Por favor instala Docker Compose primero."
    exit 1
fi

# Crear archivo .env si no existe
if [ ! -f .env ]; then
    echo "📝 Creando archivo .env..."
    cat > .env << EOF
# Configuración de la base de datos
DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_db

# Configuración de seguridad
SECRET_KEY=$(openssl rand -hex 32)
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Configuración del dominio
DOMAIN=$DOMAIN
EOF
    echo "✅ Archivo .env creado. Por favor edítalo con tus credenciales reales."
fi

# Actualizar la configuración de Nginx con el dominio real
echo "🔧 Actualizando configuración de Nginx..."
sed -i "s/TU_DOMINIO.COM/$DOMAIN/g" docker/nginx.conf

# Construir y levantar los contenedores
echo "🏗️ Construyendo contenedores..."
docker-compose up -d --build

# Verificar que los contenedores estén funcionando
echo "🔍 Verificando estado de los contenedores..."
sleep 10
docker-compose ps

# Verificar que la API esté respondiendo
echo "🔍 Verificando que la API esté funcionando..."
if curl -f http://localhost/health > /dev/null 2>&1; then
    echo "✅ API funcionando correctamente en http://localhost"
else
    echo "⚠️ La API no responde en localhost. Verificando puerto 8000..."
    if curl -f http://localhost:8000/health > /dev/null 2>&1; then
        echo "✅ API funcionando en puerto 8000"
    else
        echo "❌ La API no está respondiendo. Revisa los logs con: docker-compose logs api"
    fi
fi

echo ""
echo "🎉 Despliegue completado!"
echo ""
echo "📋 Próximos pasos:"
echo "1. Edita el archivo .env con tus credenciales reales"
echo "2. Configura tu dominio para apuntar a este servidor"
echo "3. Para obtener certificados SSL, ejecuta:"
echo "   docker-compose run --rm certbot certonly --webroot -w /var/www/certbot -d $DOMAIN"
echo ""
echo "🌐 URLs disponibles:"
echo "   - API: http://localhost:8000"
echo "   - Nginx: http://localhost"
echo "   - Documentación: http://localhost/docs"
echo ""
