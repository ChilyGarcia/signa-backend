from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.core import exception_handlers
from app.routers.auth import router as auth_router
from app.routers.user import router as user_router
from app.routers.brand import router as brand_router
from app.routers.audit import router as audit_router

app = FastAPI(
    title="FastAPI App",
    description="API con autenticación OAuth2 y sistema de auditoría",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
    swagger_ui_init_oauth={
        "usePkceWithAuthorizationCodeGrant": True,
        "clientId": "fastapi-app",
        "clientSecret": "",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(
    HTTPException, exception_handlers.http_exception_handler
)
app.add_exception_handler(404, exception_handlers.not_found_exception_handler)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(brand_router, prefix="/brands", tags=["brands"])
app.include_router(audit_router, prefix="/audit", tags=["audit"])


@app.get("/health")
async def health_check():
    """Endpoint para verificar el estado de salud de la aplicación"""
    return {"status": "healthy", "message": "API funcionando correctamente"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    
    # Configurar esquema de seguridad OAuth2
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "oauth2",
            "flows": {
                "password": {
                    "tokenUrl": "/auth/login-oauth",
                    "scopes": {}
                }
            },
            "description": (
                "Ingresa tu email y contraseña para obtener un token JWT"
            )
        }
    }
    
    # Aplicar seguridad global a todos los endpoints excepto auth
    for path in openapi_schema["paths"]:
        if not path.startswith("/auth"):
            for method in openapi_schema["paths"][path]:
                if method.lower() in ["get", "post", "put", "delete", "patch"]:
                    if "security" not in openapi_schema["paths"][path][method]:
                        openapi_schema["paths"][path][method]["security"] = [
                            {"OAuth2PasswordBearer": []}
                        ]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
