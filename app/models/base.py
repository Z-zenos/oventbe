from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Column, DateTime, Field, Integer, func


class BaseCreateUpdateModel(BaseModel):
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )

    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), onupdate=func.now())
    )

    created_by: Optional[int] = Field(
        sa_type=Integer,
        sa_column_kwargs={
            "nullable": True,
        },
        default=None,
    )
    updated_by: Optional[int] = Field(
        sa_type=Integer,
        sa_column_kwargs={
            "nullable": True,
        },
        default=None,
    )
