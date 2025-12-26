from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    db_username: str = Field(..., validation_alias="DATABASE_USERNAME")
    db_password: str = Field(..., validation_alias="DATABASE_PASSWORD")
    db_hostname: str = Field(..., validation_alias="DATABASE_HOSTNAME")
    db_port: int = Field(default="5432", validation_alias="DATABASE_PORT")
    db_name: str = Field(..., validation_alias="DATABASE_NAME")

    database_url: str = Field(..., validation_alias="DATABASE_URL")
    tz: str = Field(default="UTC", validation_alias="TZ")
    pool_size: int = Field(default=10, validation_alias="DB_POOL_SIZE")
    max_overflow: int = Field(default=20, validation_alias="DB_MAX_OVERFLOW")


@lru_cache
def settings_config() -> Settings:
    # noinspection PyArgumentList
    return Settings()
