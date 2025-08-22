from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.security import decode_access_token
from app.db.session import get_db
from app.models.user import User as DBUser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login-oauth")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> DBUser:
    try:
        payload = decode_access_token(token, verify_exp=False)
        user_id = int(payload.get("sub"))
    except Exception as e:
        raise HTTPException(
            status_code=401, 
            detail=f"Token inválido o expirado: {str(e)}"
        )

    user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=404, 
            detail="Usuario no encontrado en la base de datos"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=401, 
            detail="Usuario inactivo"
        )

    return user
