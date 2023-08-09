# %%
# LINKS
# HOW TO USE: https://www.linkedin.com/pulse/notifica%C3%A7%C3%A3o-whatsapp-via-python-marcelo-tardivo

# %%
# CODE INFORMATION
# DESCRIPTION: SEND A MESSAGE USING PYTHON AND WHATSAPP WHEN SOME EMAIL FROM AN "IMPORT PERSON" ARRIVES IN INBOX 
# INSTRUCTION: CREATE AN ACCOUNT IN WHATSGW AND AN GOOGLE ACCOUNT OR MICROSOFT ACCOUNT
# AUTHOR: MARCELO TARDIVO
# DATE: 09/08/2023

# %%
# ACESSO AO GMAIL
email_acesso = "" # E-MAIL A SER ANALISADO
senha_acesso = "" # SENHA DE APLICATIVO

key_whatsgw =  "" # CHAVE API DISPONIBILIZADA NO WHATSGW
meu_numero_whatsapp = "" # NUMERO QUE VAI ENVIAR A MENSAGEM NO WHATSAPP
numero_destino_whatsapp = "" # NUMERO QUE VAI RECEBER MENSAGEM NO WHATSAPP


# %%
import smtplib
import imaplib
import email
from email.header import decode_header
import datetime

def ultimos_emails():
  # ACESSANDO O GMAIL
  M = imaplib.IMAP4_SSL("imap.gmail.com")
  M.login(email_acesso, senha_acesso) # INFORMAR EMAIL E SENHA DE ACESSO À CONTA DO GMAIL

  # FILTRO DE DATA
  data_recebimento = datetime.datetime.now() - datetime.timedelta(minutes=1)
  data_recebimento_filtro = data_recebimento.strftime("%d-%b-%Y")

  # TRAZENDO OS E-MAILS
  M.select("inbox") # ACESSANDO A CAIXA DE ENTRADA DO GMAIL
  result, data = M.search(None, '(SINCE "{}")'.format(data_recebimento_filtro)) # BUSCANDO PELOS E-MAILS RECEBIDOS A PARTIR DA DATA ESTABELECIDA
  email_ids = data[0].split() # TRAZENDO AS CHAVES DOS E-MAILS

  # IDENTIFICANDO OS REMETENTES
  remetentes_recebidos = [] # LISTA DE E-MAILS
  for email_id in email_ids: # PARA CADA CHAVE DE E-MAIL RECEBIDO
      result, email_data = M.fetch(email_id, "(RFC822)") # BUSCANDO O E-MAIL PERTENCENTE A CADA CHAVE
      for response in email_data:
          if isinstance(response, tuple):
              msg = email.message_from_bytes(response[1])
              for header in ["From", "Sender"]:
                  value = msg[header]
                  name, address = email.utils.parseaddr(value)
                  remetentes_recebidos.append(address)
  return remetentes_recebidos
  M.close()
  M.logout()

# %%
import requests
def send_message_whatsapp(mensagem):
  url = "https://app.whatsgw.com.br/api/WhatsGw/Send"
  data = {
    "apikey" : key_whatsgw,
    "phone_number" : meu_numero_whatsapp,
    "contact_phone_number" : numero_destino_whatsapp,
    "message_type" : "text",
    "message_body" : mensagem,
    "check_status" : "1"
  }
  response = requests.post(url, json=data)
  if response.status_code != 200:
    print("Erro: ",response.status_code)

# %%
# IMPORTANT EMAIL
list_mail = []

# %%
# FUNCTION SEND MESSAGE IN WHATSAPP
def notificao_whatsapp(remetentes_recebidos):
  lista = set(remetentes_recebidos).intersection(list_mail)
  if lista:
    mensagem = "Olá. Acabamos de receber um e-mail de " + str(lista)
    send_message_whatsapp(mensagem)

# %%
notificao_whatsapp(ultimos_emails())


