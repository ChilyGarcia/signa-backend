from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.models.audit import AuditAction
from app.repositories.audit import audit_repository
from app.schemas.audit import BrandAudit, AuditStatistics

router = APIRouter()


@router.get("/test-auth")
def test_authentication(
    current_user: User = Depends(get_current_user),
):
    """Endpoint de prueba para verificar autenticación"""
    return {
        "message": "Autenticación exitosa",
        "user_id": current_user.id,
        "user_email": current_user.email,
        "user_name": f"{current_user.first_name} {current_user.last_name}"
    }


@router.get("/", response_model=List[BrandAudit])
def get_audit_logs(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Obtener historial de auditoría (requiere autenticación)"""
    return audit_repository.get_recent_audits(db, limit=limit)


@router.get("/brand/{brand_id}", response_model=List[BrandAudit])
def get_brand_audit_history(
    brand_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Obtener historial de auditoría de una marca específica"""
    return audit_repository.get_brand_audit_history(
        db, brand_id=brand_id, skip=skip, limit=limit
    )


@router.get("/user/{user_id}", response_model=List[BrandAudit])
def get_user_audit_history(
    user_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Obtener historial de auditoría de un usuario específico"""
    return audit_repository.get_user_audit_history(
        db, user_id=user_id, skip=skip, limit=limit
    )


@router.get("/action/{action}", response_model=List[BrandAudit])
def get_audits_by_action(
    action: AuditAction,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Obtener auditorías por tipo de acción"""
    return audit_repository.get_audits_by_action(
        db, action=action, skip=skip, limit=limit
    )


@router.get("/date-range", response_model=List[BrandAudit])
def get_audits_by_date_range(
    start_date: datetime = Query(
        ..., description="Fecha de inicio (YYYY-MM-DD HH:MM:SS)"
    ),
    end_date: datetime = Query(..., description="Fecha de fin (YYYY-MM-DD HH:MM:SS)"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Obtener auditorías en un rango de fechas"""
    return audit_repository.get_audits_by_date_range(
        db,
        start_date=start_date.isoformat(),
        end_date=end_date.isoformat(),
        skip=skip,
        limit=limit,
    )


@router.get("/search", response_model=List[BrandAudit])
def search_audits_by_brand_name(
    brand_name: str = Query(
        ..., min_length=1, description="Nombre de la marca a buscar"
    ),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Buscar auditorías por nombre de marca"""
    return audit_repository.search_audits_by_brand_name(
        db, brand_name=brand_name, skip=skip, limit=limit
    )


@router.get("/statistics", response_model=AuditStatistics)
def get_audit_statistics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Obtener estadísticas de auditoría"""
    return audit_repository.get_audit_statistics(db)


@router.get("/my-audits", response_model=List[BrandAudit])
def get_my_audit_history(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Obtener historial de auditoría del usuario autenticado"""
    return audit_repository.get_user_audit_history(
        db, user_id=current_user.id, skip=skip, limit=limit
    )


@router.get("/{audit_id}", response_model=BrandAudit)
def get_audit_detail(
    audit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Obtener detalles de una auditoría específica"""
    audit = audit_repository.get(db, audit_id)
    if not audit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registro de auditoría no encontrado",
        )
    return audit
