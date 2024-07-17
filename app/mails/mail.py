from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from jinja2 import Environment, FileSystemLoader

from app.core.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME=settings.EMAIL_USERNAME,
    MAIL_PASSWORD=settings.EMAIL_PASSWORD,
    MAIL_FROM=settings.EMAIL_SENDER,
    MAIL_PORT=settings.EMAIL_PORT,
    MAIL_SERVER=settings.EMAIL_HOST,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=settings.TEMPLATE_FOLDER,
)


def read_template(file_name, data):
    # Link to directory of templates
    template_folder = settings.TEMPLATE_FOLDER

    # Load template from file
    env = Environment(loader=FileSystemLoader(template_folder))
    j2template = env.get_template(file_name)

    # Replace real data into placeholder
    html = j2template.render(data)
    return html


# Send mail
async def send_email(receivers: str | list, html: str, subject: str, **kwargs):
    html_data = read_template(html, kwargs)

    # create mail context
    message = MessageSchema(
        subject=subject,
        recipients=list(receivers),
        template_body=html_data,
        subtype=MessageType.html,
    )
    fm = FastMail(conf)
    await fm.send_message(message)
