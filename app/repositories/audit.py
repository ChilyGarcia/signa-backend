from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.repositories.base import BaseRepository
from app.models.audit import BrandAudit, AuditAction
from app.schemas.audit import BrandAuditCreate, BrandAuditUpdate


class AuditRepository(BaseRepository[BrandAudit, BrandAuditCreate, BrandAuditUpdate]):
    def get_brand_audit_history(
        self, db: Session, brand_id: int, skip: int = 0, limit: int = 100
    ) -> List[BrandAudit]:
        """Obtiene el historial de auditoría de una marca específica"""
        return (
            db.query(BrandAudit)
            .filter(BrandAudit.brand_id == brand_id)
            .order_by(desc(BrandAudit.timestamp))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_user_audit_history(
        self, db: Session, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[BrandAudit]:
        """Obtiene el historial de auditoría de un usuario específico"""
        return (
            db.query(BrandAudit)
            .filter(BrandAudit.user_id == user_id)
            .order_by(desc(BrandAudit.timestamp))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_audits_by_action(
        self, db: Session, action: AuditAction, skip: int = 0, limit: int = 100
    ) -> List[BrandAudit]:
        """Obtiene auditorías por tipo de acción"""
        return (
            db.query(BrandAudit)
            .filter(BrandAudit.action == action)
            .order_by(desc(BrandAudit.timestamp))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_audits_by_date_range(
        self,
        db: Session,
        start_date: str,
        end_date: str,
        skip: int = 0,
        limit: int = 100,
    ) -> List[BrandAudit]:
        """Obtiene auditorías en un rango de fechas"""
        return (
            db.query(BrandAudit)
            .filter(
                BrandAudit.timestamp >= start_date, BrandAudit.timestamp <= end_date
            )
            .order_by(desc(BrandAudit.timestamp))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_recent_audits(self, db: Session, limit: int = 50) -> List[BrandAudit]:
        """Obtiene las auditorías más recientes"""
        return (
            db.query(BrandAudit).order_by(desc(BrandAudit.timestamp)).limit(limit).all()
        )

    def search_audits_by_brand_name(
        self, db: Session, brand_name: str, skip: int = 0, limit: int = 100
    ) -> List[BrandAudit]:
        """Busca auditorías por nombre de marca"""
        return (
            db.query(BrandAudit)
            .filter(BrandAudit.brand_name.ilike(f"%{brand_name}%"))
            .order_by(desc(BrandAudit.timestamp))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_audit_statistics(self, db: Session) -> dict:
        """Obtiene estadísticas de auditoría"""
        total_audits = db.query(BrandAudit).count()

        create_count = (
            db.query(BrandAudit).filter(BrandAudit.action == AuditAction.CREATE).count()
        )

        update_count = (
            db.query(BrandAudit).filter(BrandAudit.action == AuditAction.UPDATE).count()
        )

        delete_count = (
            db.query(BrandAudit).filter(BrandAudit.action == AuditAction.DELETE).count()
        )

        status_change_count = (
            db.query(BrandAudit)
            .filter(BrandAudit.action == AuditAction.STATUS_CHANGE)
            .count()
        )

        return {
            "total_audits": total_audits,
            "creations": create_count,
            "updates": update_count,
            "deletions": delete_count,
            "status_changes": status_change_count,
        }


audit_repository = AuditRepository(BrandAudit)
