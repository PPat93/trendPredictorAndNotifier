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

from api_retriever_cmb import retrieve_data


PORT = 465
TICKER = "CMA"
sender_email = os.environ.get("predictorMailerAddress")
sender_pass = os.environ.get("predictorAppPass")
notifyee_email = os.environ.get("notifyeeMailerAddress")

retriever_res = retrieve_data(TICKER).content

compose_message = EmailMessage()

compose_message["Subject"] = f"Change on {TICKER}"
compose_message["From"] = sender_email
compose_message["To"] = notifyee_email
compose_message.set_content(
    f"Hi! \nI found an interesting change on {TICKER}.\n{retriever_res}"
)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
    server.login(sender_email, sender_pass)
    server.send_message(compose_message)
