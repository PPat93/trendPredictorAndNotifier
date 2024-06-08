""" 
Mailer Comb:
Receives data from Integrator: -> Analyzer, -> Database;
Creates email and it's content;
Sends email;
"""

import smtplib
import ssl
import os
from email.message import EmailMessage

PORT = 465
sender_email = os.environ.get("predictorMailerAddress")
sender_pass = os.environ.get("predictorAppPass")
notifyee_email = os.environ.get("notifyeeMailerAddress")


def compose_email(ticker, content):
    """Create a message that will be send"""
    compose_message = EmailMessage()

    compose_message["Subject"] = f"Change on {ticker}"
    compose_message["From"] = sender_email
    compose_message["To"] = notifyee_email
    compose_message.set_content(
        f"Hi! \nI found an interesting change on {ticker}.\n{content}"
    )
    return compose_message


def send_email(message):
    """Send notification email with the specified message"""
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
        server.login(sender_email, sender_pass)
        server.send_message(message)
