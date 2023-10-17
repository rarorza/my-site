import email.message
import os
import smtplib
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent.parent.parent / "dotenv_files" / ".env"
load_dotenv(dotenv_path=dotenv_path)


def send_email(
    name_form="",
    email_form="",
    message_form="",
    recipient="rafael.rsa@yahoo.com",
):
    sender = "portfolio.rarorza@gmail.com"
    body_email = f"""
<p>from: {name_form} - {email_form}</p>
<p>message: {message_form}</p>
"""

    msg = email.message.Message()
    msg["Subject"] = "Contact Form"
    msg["From"] = sender
    msg["To"] = recipient
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(body_email)

    smtp = smtplib.SMTP("smtp.gmail.com: 587")
    smtp.starttls()

    # login
    try:
        password = os.getenv("PWD_SMTP_FORM")
        smtp.login(msg["From"], password)
        smtp.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
        return True
    except AttributeError:
        return False


send_email("Rafael", "rafael.rsa@yahoo.com", "Oi")
