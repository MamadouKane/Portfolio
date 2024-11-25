import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

from email.mime.base import MIMEBase
from email import encoders

load_dotenv()


def send_email(sender_email, subject, message_content, attachment=None):
    # Configuration SMTP
    smtp_server = "smtp.gmail.com"  # Gmail
    smtp_port = 587
    my_email = os.getenv("EMAIL")
    my_password = os.getenv("EMAIL_PASSWORD")

    try:
        # create the message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = my_email
        message["Subject"] = subject + " From Portfolio "

        # Add the msg content 
        # message.attach(MIMEText(message_content, "plain"))
        message.attach(MIMEText(f"Message From : {sender_email}\n\n{message_content}", "plain"))


        if attachment is not None:
            attachment.seek(0)
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={attachment.name}",
            )
            message.attach(part)


        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(my_email, my_password)
            server.sendmail(sender_email, my_email, message.as_string())

        return True
    except Exception as e:
        print(f"Erreur : {e}")
        return False




