import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import jinja2

import settings


def send_email(
        recipients: list[str],
        /,
        *,
        mail_body: str,
        mail_subject: str,
):


    TOKEN = settings.TOKEN_UKR_NET
    USER = settings.USER
    SMTP_SERVER = settings.SMTP_SERVER

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = f'<Email was sent from {USER}>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'decorator'

    text_to_send = MIMEText(mail_body, 'html')
    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SMTP_SERVER)
    mail.login(USER, TOKEN)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()


def create_welcome_letter(params: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader)
    template_file = 'templates/letter_for_sales.html'
    template = template_env.get_template(template_file)
    output = template.render(params)
    return output
