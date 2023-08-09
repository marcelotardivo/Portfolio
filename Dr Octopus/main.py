"""
CODE INFORMATION
DESCRIPTION: THIS PROJECT CONSISTS OF RUNNING A COLLECTION OF SCRIPTS THAT, TOGETHER, HAVE THE CAPABILITY TO ESTABLISH A SOPHISTICATED SYSTEM OF AUTOMATIONS AND MONITORING, ACTING AS AN AGENT RESPONSIBLE FOR DETECTING ERRORS AND OPERATIONAL TASKS.
AUTHOR: MARCELO TARDIVO
DATE: 09/08/2023
"""

# Libraries used to list the scripts
import pandas as pd
import datetime as dt

# List of scripts to be executed
lista_scripts = []

# After attempting to execute the script, it will be added to this list along with its status
lista_relatorio = []

# EXECUTED ON MONDAY
if dt.datetime.today().date().weekday() == 0:
    lista_filtro = []
    lista_filtro = ['script_1.py', 'script_2.py']
    lista_scripts = list(set(lista_scripts + lista_filtro))

# Libraries used for script execution
import subprocess

# Loop to execute each script from the list
results = {}
for script in lista_scripts:
    output = subprocess.run(["python", script])
    if output.returncode == 0:
        results[script] = "Executed successfully"
    elif output.returncode != 0:
        results[script] = "Not Executed"
relatorio = pd.DataFrame.from_dict(results, orient='index', columns=['Status'])


# Sending scripts report via Email (Gmail)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Define the sender's email address and password
remetente_email = 'sender@gmail.com'
remetente_senha = 'passwd'

# Define the recipient's email address
destinatario_email = 'recipient@gmail.com' #'projetos@ehorus.com.br'

# Create the email message
mensagem = MIMEMultipart()
mensagem['From'] = remetente_email
mensagem['To'] = destinatario_email
mensagem['Subject'] = 'Scripts Report: ' + dt.datetime.today().strftime('%d/%m/%Y') 

# Create a MIMEText object with the type "text/html" and attach the DataFrame string to the email body
texto_mensagem = "Hello!<br> Here's the report of the scripts we tried to execute.<br><br>"

mensagem_anexo = MIMEText(texto_mensagem, 'html')
mensagem.attach(mensagem_anexo)

# Create a MIMEText object with the type "text/html" and attach the DataFrame string to the email body
mensagem_anexo = MIMEText(relatorio.to_html(index=True, col_space=300, border=0, justify='left'), 'html')
mensagem.attach(mensagem_anexo)

# Send the email message using the Gmail SMTP server
servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
servidor_smtp.starttls()
servidor_smtp.login(remetente_email, remetente_senha)
servidor_smtp.sendmail(remetente_email, destinatario_email, mensagem.as_string())
servidor_smtp.quit()