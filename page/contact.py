import streamlit as st
import smtplib
import re
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from email.mime.base import MIMEBase
from email import encoders
import dns.resolver

load_dotenv()


# def is_valid_email(email):
#     """ Vérifie si l'email a un format valide """
#     pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#     return re.match(pattern, email) is not None

# def email_domain_exists(email):
#     """ Vérifie si le domaine de l'email a un enregistrement MX (serveur de mail) """
#     try:
#         domain = email.split("@")[1]
#         records = dns.resolver.resolve(domain, 'MX')  # Recherche des serveurs mail
#         return bool(records)  # True si un serveur mail existe, False sinon
#     except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.LifetimeTimeout):
#         return False  # Domaine inexistant ou pas de serveur mail


# https://mailboxlayer.com/dashboard
def email_exists(email):
    API_KEY = os.getenv("MAILBOXLAYER_API_KEY")  # Mets ta clé API ici
    url = f"http://apilayer.net/api/check?access_key={API_KEY}&email={email}"

    response = requests.get(url)
    data = response.json()

    return data.get("format_valid") and data.get("smtp_check")


def send_email(sender_email, subject, message_content, attachment=None):
    # Vérifier l'email avant l'envoi
    # if not is_valid_email(sender_email):
    #     print("Erreur : Adresse e-mail invalide.")
    #     return False
    # Vérifier le domaine de l'email
    if not email_exists(sender_email):
        print("Erreur : L'email n'existe pas.")
        return False


    # Configuration SMTP
    smtp_server = os.getenv("SERVER_ADRESS")  # Adresse du serveur SMTP
    smtp_port = int(os.getenv("PORT"))  # S'assurer que c'est bien un entier
    my_email = os.getenv("EMAIL")
    my_password = os.getenv("EMAIL_PASSWORD")

    try:
        # Créer le message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = my_email
        message["Subject"] = subject + " From Portfolio "

        # Ajouter le contenu du message
        message.attach(MIMEText(f"Message From : {sender_email}\n\n{message_content}", "plain"))

        # Ajouter une pièce jointe si présente
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

        # Envoyer l'e-mail
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(my_email, my_password)
            server.sendmail(sender_email, my_email, message.as_string())

        return True
    except Exception as e:
        print(f"Erreur : {e}")
        return False


