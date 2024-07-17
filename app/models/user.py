from datetime import datetime
from typing import Optional

from geoalchemy2 import Geometry
from sqlmodel import Column, DateTime, Enum, Field, String, Text

from app.core.code import RoleCode
from app.models.base import BaseCreateUpdateModel


class User(BaseCreateUpdateModel, table=True):
    __tablename__: str = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    role_code: Optional[RoleCode] = Field(sa_column=Column(Enum(RoleCode)))
    organization_id: Optional[int] = Field(
        default=None, foreign_key="organizations.id"
    )
    email: Optional[str] = Field(sa_column=Column(String(255)), default=None)

    password: Optional[str] = Field(
        sa_column=Column(String(2048), nullable=True), default=None
    )
    first_name: Optional[str] = Field(
        sa_column=Column(String(255)), default=None
    )
    last_name: Optional[str] = Field(
        sa_column=Column(String(255)), default=None
    )
    company_name: Optional[str] = Field(
        sa_column=Column(String(255)), default=None
    )

    phone: Optional[str] = Field(sa_column=Column(String(20)), default=None)

    location: Optional[list] = Field(
        default_factory=list, sa_column=Column(Geometry("POINT"))
    )

    city: Optional[str] = Field(sa_column=Column(String(50)), default=None)

    address: Optional[str] = Field(sa_column=Column(Text), default=None)
    industry_code: Optional[str] = Field(
        sa_column=Column(String(50), comment="業種"), default=None
    )
    employee_size_code: Optional[str] = Field(
        sa_column=Column(String(20)), default=None
    )
    revenue_code: Optional[str] = Field(
        sa_column=Column(String(20), comment="会社の年商規模"), default=None
    )
    job_type_code: Optional[str] = Field(
        sa_column=Column(String(20), comment="担当領域（職種）"), default=None
    )
    position_code: Optional[str] = Field(
        sa_column=Column(String(20), comment="立場（役職）"), default=None
    )
    avatar_url: Optional[str] = Field(
        sa_column=Column(String(2048), nullable=True), default=None
    )
    email_verify_token: Optional[str] = Field(
        sa_column=Column(String(2048), nullable=True), default=None
    )
    email_verify_token_expire_at: Optional[str] = Field(
        sa_column=Column(DateTime(timezone=True), nullable=True), default=None
    )
    email_verify_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=True,
        ),
        default=None,
    )
    reset_password_token: Optional[str] = Field(
        sa_column=Column(String(2048), nullable=True), default=None
    )
    reset_password_token_expire_at: Optional[str] = Field(
        sa_column=Column(DateTime(timezone=True), nullable=True), default=None
    )

    new_email: Optional[str] = Field(
        sa_column=Column(String(255)), default=None
    )
    new_email_verify_token: Optional[str] = Field(
        sa_column=Column(String(2048), nullable=True), default=None
    )
    new_email_verify_token_expire_at: Optional[str] = Field(
        sa_column=Column(DateTime(timezone=True), nullable=True), default=None
    )
    deleted_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=True,
        ),
        default=None,
    )
