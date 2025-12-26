from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from cores.config import settings_config

settings = settings_config()

engine = create_engine(
    settings.database_url,
    # echo=True,
    echo=False,  # there is already a logger to take care of the echo
    pool_pre_ping=True,
    pool_size=settings.pool_size,
    max_overflow=settings.max_overflow,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
