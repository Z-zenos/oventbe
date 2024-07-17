import enum


class RoleCode(str, enum.Enum):
    AUDIENCE = "AUDIENCE"
    SPEAKER = "SPEAKER"
    ORGANIZER = "ORGANIZER"
    ADMIN = "ADMIN"
