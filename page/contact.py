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

from email_validator import validate_email, EmailNotValidError
from captcha.image import ImageCaptcha
import random
import time
import datetime
from streamlit_js_eval import streamlit_js_eval
import json

load_dotenv()

# Configuration SMTP
smtp_server = os.getenv("SERVER_ADRESS")  # Adresse du serveur SMTP
smtp_port = int(os.getenv("PORT"))  # S'assurer que c'est bien un entier
my_email = os.getenv("EMAIL")
my_password = os.getenv("EMAIL_PASSWORD")
options = os.getenv("OPTIONS")

# # Configuration SMTP
# smtp_server = os.getenv("SERVER_ADRESS")  # Adresse du serveur SMTP
# smtp_port = int(os.getenv("PORT"))  # S'assurer que c'est bien un entier
# my_email = os.getenv("EMAIL")
# my_password = os.getenv("EMAIL_PASSWORD")
# options = os.getenv("OPTIONS")

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




## Functions
def generate_captcha():
    captcha_text = "".join(random.choices(options, k=6)) # options is a string of characters that can be included in the CAPTCHA. It may be as simple or as complex as you wish. 
    image = ImageCaptcha(width=400, height=100).generate(captcha_text)
    return captcha_text, image


# Chemin vers le fichier de rate limiting
RATE_LIMIT_FILE = "rate_limit.json"

# Charger les adresses bloquées
def load_rate_limit():
    if os.path.exists(RATE_LIMIT_FILE):
        with open(RATE_LIMIT_FILE, "r") as file:
            return json.load(file)
    return {}

# Sauvegarder les adresses bloquées
def save_rate_limit(data):
    with open(RATE_LIMIT_FILE, "w") as file:
        json.dump(data, file)

# Vérifie si l'email est déjà bloqué
def is_blocked(email):
    rate_limits = load_rate_limit()
    return rate_limits.get(email, {}).get("blocked", False)


# Bloquer l'email après envoi de 2 messages en moins de 5 minutes
def block_email(email):
    rate_limits = load_rate_limit()
    current_time = time.time()

    # Si l'email existe déjà, vérifier l'intervalle
    if email in rate_limits:
        last_sent_time = rate_limits[email].get("last_sent_time", 0)
        
        # Si le dernier mail a été envoyé il y a moins de 5 minutes (300 secondes), bloquer
        if current_time - last_sent_time < 300:
            rate_limits[email] = {"blocked": True, "last_sent_time": current_time}
        else:
            # Mettre à jour simplement le dernier envoi si plus de 5 minutes se sont écoulées
            rate_limits[email]["last_sent_time"] = current_time
    else:
        # Premier envoi de l'email, stocker la date
        rate_limits[email] = {"blocked": False, "last_sent_time": current_time}

    save_rate_limit(rate_limits)


def contact():
    ## Generate CAPTCHA
    if 'captcha_text' not in st.session_state:
        st.session_state.captcha_text = generate_captcha()

    captcha_text, captcha_image = st.session_state.captcha_text

    col1, col2, col3, col4 =  st.columns([3, 0.25, 1, 0.25]) # column widths for a balanced distribution of elements in the page

    captcha_input = None # initiate CAPTCHA

    ## CAPTCHA
    with col3: # right side of the layout
        st.markdown('<p style="text-align: justify; font-size: 12px;">CAPTCHAs are active to prevent automated submissions. <br> Thank you for your understanding.</p>', unsafe_allow_html=True) # warning for user.
        captcha_placeholder = st.empty()
        captcha_placeholder.image(captcha_image, use_column_width=True)

        if st.button("Refresh", type="secondary", use_container_width=True): # option to refresh CAPTCHA without refreshing the page
            st.session_state.captcha_text = generate_captcha()
            captcha_text, captcha_image = st.session_state.captcha_text
            captcha_placeholder.image(captcha_image, use_column_width=True)

        captcha_input = st.text_input("Enter the CAPTCHA") # box to insert CAPTCHA

    ## Contact form
    with col1: # left side of the layout
        sender_email = st.text_input("**Your email***", value=st.session_state.get('email', ''), key='email') # input widget for contact email
        message = st.text_area("**Your message***", value=st.session_state.get('message', ''), key='message') # input widget for message

        st.markdown('<p style="font-size: 13px;">*Required fields</p>', unsafe_allow_html=True) # indication to user that both fields must be filled

        if st.button("Send", type="primary"):
            if not sender_email or not message:
                st.error("Please fill out all required fields.") # error for any blank field
            else:
                try:

                    if is_blocked(sender_email):
                        st.error("Failed to send your message. Please try again later.")
                    else:
                
                        # Robust email validation
                        valid = validate_email(sender_email, check_deliverability=True)

                        # Check CAPTCHA
                        if captcha_input.upper() == captcha_text:

                            # Email configuration - **IMPORTANT**: for security these details should be present in the "Secrets" section of Streamlit
                            #### NOTE FOR DEVELOPERS: UNCOMMENT THE LINES BELOW ####
                            

                            # Create an SMTP connection
                            server = smtplib.SMTP(smtp_server, smtp_port)
                            server.starttls()
                            server.login(my_email, my_password)

                            ## Compose the email message
                            subject = "Contact From Porfolio" # subject of the email you will receive upon contact.
                            body = f"Email: {sender_email}\nMessage: {message}"
                            msg = MIMEMultipart()
                            msg['From'] = sender_email
                            msg['To'] = my_email
                            msg['Subject'] = subject
                            msg.attach(MIMEText(body, 'plain'))

                            # Send the email
                            server.sendmail(sender_email, my_email, msg.as_string())

                            ## Send the confirmation email to the message sender # If you do not want to send a confirmation email leave this section commented
                            current_datetime = datetime.datetime.now()
                            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                            confirmation_subject = f"Confirmation of Mamadou KANE Contact Form Submission ({formatted_datetime})"
                            confirmation_body = f"Thank you for contacting me! Your message has been received.\n\nYour message: {message}"
                            confirmation_msg = MIMEMultipart()
                            confirmation_msg['From'] = my_email
                            confirmation_msg['To'] = sender_email  # Use the sender's email address here
                            confirmation_msg['Subject'] = confirmation_subject
                            confirmation_msg.attach(MIMEText(confirmation_body, 'plain'))
                            server.sendmail(my_email, sender_email, confirmation_msg.as_string())
                            
                            # Close the SMTP server connection
                            server.quit()

                            st.success("Sent successfully!") # Success message to the user.
                            
                            # Block the email if it has sent more than 2 messages in less than 5 minutes
                            block_email(sender_email)

                            #### NOTE FOR DEVELOPERS: UPON DEPLOYMENT DELETE THE SECTION BELOW ####
                            # st.info("""This would have been a message sent successfully!  
                            # For more information on activating the contact form, please check the [documentation](https://github.com/jlnetosci/streamlit-contact-form).""") # Please delete this info box if you have the contact form setup correctly.

                            # Generate a new captcha to prevent button spamming.
                            st.session_state.captcha_text = generate_captcha()
                            captcha_text, captcha_image = st.session_state.captcha_text
                            # Update the displayed captcha image
                            captcha_placeholder.image(captcha_image, use_column_width=True)

                            time.sleep(3)
                            streamlit_js_eval(js_expressions="parent.window.location.reload()")

                        else:
                            st.error("Text does not match the CAPTCHA.") # error to the user in case CAPTCHA does not match input

                except EmailNotValidError as e:
                    st.error(f"Invalid email address. {e}") # error in case any of the email validation checks have not passed
