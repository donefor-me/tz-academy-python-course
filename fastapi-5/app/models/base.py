from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import func, Column, DateTime


class Base(DeclarativeBase):
    pass


class TimeMixin:
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
