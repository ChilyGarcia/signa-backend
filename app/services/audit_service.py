import json
from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import Request

from app.models.audit import BrandAudit, AuditAction
from app.models.brand import Brand
from app.models.user import User


class AuditService:
    @staticmethod
    def _get_client_info(request: Request) -> tuple[str, str]:
        """Obtiene información del cliente desde la request"""
        ip_address = request.client.host if request.client else None
        user_agent = request.headers.get("user-agent", "")
        return ip_address, user_agent

    @staticmethod
    def _serialize_brand_data(brand: Brand) -> str:
        """Serializa los datos de una marca a JSON"""
        brand_data = {
            "id": brand.id,
            "name": brand.name,
            "description": brand.description,
            "owner": brand.owner,
            "registration_number": brand.registration_number,
            "status": brand.status.value if brand.status else None,
            "created_by": brand.created_by,
        }
        return json.dumps(brand_data, ensure_ascii=False)

    @staticmethod
    def _get_changes_summary(
        old_data: Optional[Dict[str, Any]], 
        new_data: Optional[Dict[str, Any]]
    ) -> str:
        """Genera un resumen de los cambios realizados"""
        if not old_data and not new_data:
            return "Sin cambios detectados"
        
        if not old_data:
            return "Registro creado"
        
        if not new_data:
            return "Registro eliminado"
        
        changes = []
        for key in new_data:
            if key in old_data and old_data[key] != new_data[key]:
                changes.append(f"{key}: {old_data[key]} → {new_data[key]}")
        
        return "; ".join(changes) if changes else "Sin cambios detectados"

    @staticmethod
    def log_brand_creation(
        db: Session,
        brand: Brand,
        user: User,
        request: Request
    ) -> BrandAudit:
        """Registra la creación de una marca"""
        ip_address, user_agent = AuditService._get_client_info(request)
        
        audit_entry = BrandAudit(
            brand_id=brand.id,
            brand_name=brand.name,
            action=AuditAction.CREATE,
            user_id=user.id,
            user_email=user.email,
            old_values=None,
            new_values=AuditService._serialize_brand_data(brand),
            changes_summary="Registro creado",
            ip_address=ip_address,
            user_agent=user_agent,
        )
        
        db.add(audit_entry)
        db.commit()
        db.refresh(audit_entry)
        return audit_entry

    @staticmethod
    def log_brand_update(
        db: Session,
        old_brand: Brand,
        new_brand: Brand,
        user: User,
        request: Request
    ) -> BrandAudit:
        """Registra la actualización de una marca"""
        ip_address, user_agent = AuditService._get_client_info(request)
        
        old_data = json.loads(AuditService._serialize_brand_data(old_brand))
        new_data = json.loads(AuditService._serialize_brand_data(new_brand))
        
        audit_entry = BrandAudit(
            brand_id=new_brand.id,
            brand_name=new_brand.name,
            action=AuditAction.UPDATE,
            user_id=user.id,
            user_email=user.email,
            old_values=json.dumps(old_data, ensure_ascii=False),
            new_values=json.dumps(new_data, ensure_ascii=False),
            changes_summary=AuditService._get_changes_summary(old_data, new_data),
            ip_address=ip_address,
            user_agent=user_agent,
        )
        
        db.add(audit_entry)
        db.commit()
        db.refresh(audit_entry)
        return audit_entry

    @staticmethod
    def log_brand_deletion(
        db: Session,
        brand: Brand,
        user: User,
        request: Request
    ) -> BrandAudit:
        """Registra la eliminación de una marca"""
        ip_address, user_agent = AuditService._get_client_info(request)
        
        audit_entry = BrandAudit(
            brand_id=brand.id,
            brand_name=brand.name,
            action=AuditAction.DELETE,
            user_id=user.id,
            user_email=user.email,
            old_values=AuditService._serialize_brand_data(brand),
            new_values=None,
            changes_summary="Registro eliminado",
            ip_address=ip_address,
            user_agent=user_agent,
        )
        
        db.add(audit_entry)
        db.commit()
        db.refresh(audit_entry)
        return audit_entry

    @staticmethod
    def log_status_change(
        db: Session,
        brand: Brand,
        old_status: str,
        new_status: str,
        user: User,
        request: Request
    ) -> BrandAudit:
        """Registra el cambio de estado de una marca"""
        ip_address, user_agent = AuditService._get_client_info(request)
        
        audit_entry = BrandAudit(
            brand_id=brand.id,
            brand_name=brand.name,
            action=AuditAction.STATUS_CHANGE,
            user_id=user.id,
            user_email=user.email,
            old_values=json.dumps({"status": old_status}, ensure_ascii=False),
            new_values=json.dumps({"status": new_status}, ensure_ascii=False),
            changes_summary=f"Estado cambiado: {old_status} → {new_status}",
            ip_address=ip_address,
            user_agent=user_agent,
        )
        
        db.add(audit_entry)
        db.commit()
        db.refresh(audit_entry)
        return audit_entry
