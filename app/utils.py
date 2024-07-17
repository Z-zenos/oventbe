from sqlalchemy.orm import Session
from sqlmodel import SQLModel


def add_flush_refresh_object(db: Session, object: SQLModel):
    db.add(object)
    db.flush()
    db.refresh(object)


def add_commit_refresh_object(db: Session, object: SQLModel):
    db.add(object)
    db.commit()
    db.refresh(object)


# def create_url(path, token):
#     return f"{settings.FRONTEND_URL}/{path}/{token}"


# def set_filename(category: MediaCategory, is_temp=False):
#     media_path = f"{settings.MEDIA_PATH}/{category.value}"
#     if is_temp:
#         media_path = settings.MEDIA_PATH_TMP_PREFIX + media_path
#     random_name = str(uuid.uuid4())
#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Format: YYYYMMDDHHMMSS
#     filename = f"{media_path}/{random_name}_{timestamp}"
#     return filename


# def convert_question_name(name: str) -> str:
#     datetime_str = datetime.now().strftime("%y%m%d%H%M%S")
#     name_converted = f"{name}-{datetime_str}"
#     datetime_length = len(datetime_str) + 1
#     # Truncate name to ensure the total length is <= 25 characters
#     if len(name_converted) > 25:
#         max_name_length = 25 - datetime_length
#         name_converted = f"{name[:max_name_length]}-{datetime_str}"
#     return name_converted


# def get_filename_from_cdn_url(url: str):
#     cdn_host = settings.PUBLIC_CDN_URL
#     if not url.startswith(cdn_host):
#         return None
#     return url.removeprefix(cdn_host)
