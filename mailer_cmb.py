""" 
Mailer Comb:
Receives data from Integrator: -> Analyzer, -> Database;
Creates email and it's content;
Sends email;
"""

import smtplib
import ssl
import os
from api_retriever_cmb import retrieve_data


PORT = 465
sender_email = os.environ.get("predictorMailerAddress")
sender_pass = os.environ.get("predictorAppPass")
notifyee_email = os.environ.get("notifyeeMailerAddress")
retriever_res = retrieve_data("IBM").content
message = "Hi! \n" #+ str(retriever_res)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
    server.login(sender_email, sender_pass)
    server.sendmail(sender_email, notifyee_email, message)
