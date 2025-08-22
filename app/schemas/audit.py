from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from app.models.audit import AuditAction


class BrandAuditBase(BaseModel):
    brand_id: int
    brand_name: str
    action: AuditAction
    user_id: int
    user_email: str
    old_values: Optional[str] = None
    new_values: Optional[str] = None
    changes_summary: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    timestamp: datetime


class BrandAuditCreate(BrandAuditBase):
    pass


class BrandAuditUpdate(BrandAuditBase):
    pass


class BrandAudit(BrandAuditBase):
    id: int

    class Config:
        from_attributes = True


class AuditStatistics(BaseModel):
    total_audits: int
    creations: int
    updates: int
    deletions: int
    status_changes: int


class AuditFilter(BaseModel):
    brand_id: Optional[int] = None
    user_id: Optional[int] = None
    action: Optional[AuditAction] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    brand_name: Optional[str] = None
    skip: int = 0
    limit: int = 100
