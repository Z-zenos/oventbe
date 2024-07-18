from typing import Any, Optional

from pydantic import PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, env_file_encoding="utf-8"
    )

    PROJECT: str = "Roominar"

    DB_CONNECTION: Optional[str]
    DB_HOST: Optional[str]
    DB_PORT: Optional[str]
    DB_DATABASE: Optional[str]
    DB_USERNAME: Optional[str]
    DB_PASSWORD: Optional[str]
    ALGORITHM: Optional[str]
    SECRET_KEY: Optional[str]
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int]
    REFRESH_TOKEN_EXPIRE_MINUTES: Optional[int]
    REFRESH_TOKEN_REMEMBERED_EXPIRE_MINUTES: Optional[int]
    EMAIL_HOST: Optional[str]
    EMAIL_USERNAME: Optional[str]
    EMAIL_PASSWORD: Optional[str]
    EMAIL_PORT: Optional[str]
    EMAIL_SENDER: Optional[str]
    EMAIL_CONFIRMATION_TOKEN_LENGTH: Optional[int]
    EMAIL_CONFIRMATION_TOKEN_EXPIRE_MINUTES: Optional[int]
    RESET_PASSWORD_TOKEN_LENGTH: Optional[int]
    RESET_PASSWORD_TOKEN_EXPIRE_MINUTES: Optional[int]
    FRONTEND_URL: Optional[str]
    EMAIL_ADMIN: Optional[str]
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn | str] = None
    # TEMPLATE_FOLDER: DirectoryPath = (
    #     Path(__file__).parent / "../mail/templates"
    # )
    # BUCKET_NAME: Optional[str]
    # MEDIA_PATH: Optional[str]
    # MEDIA_PATH_TMP_PREFIX: str = "tmp/"
    # PUBLIC_CDN_URL: Optional[str]
    FORWARD_DB_PORT: Optional[str]
    APP_PORT: Optional[str]
    APP_URL: Optional[str]

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    def assemble_db_connection(cls, v: Optional[str], values: ValidationInfo) -> Any:
        if isinstance(v, str) and v:
            print("Loading SQLALCHEMY_DATABASE_URI from .docker.env file ...")
            return v

        print("Creating SQLALCHEMY_DATABASE_URI from .env file ...")

        return PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get("DB_USERNAME"),
            password=values.data.get("DB_PASSWORD"),
            host=values.data.get("DB_HOST"),
            port=int(values.data.get("DB_PORT")),
            path=f"{values.data.get('DB_DATABASE') or ''}",
        ).unicode_string()


settings = Settings()
