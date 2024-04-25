# Enviando email

import smtplib as emails #biblioteca para enviar email
import getpass as gt   #biblioteca para ocultar senha
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
servidorSmtp='smtp-mail.outlook.com'
porta=587

email = "marcel_86_7@hotmail.com"
senha=gt.getpass("Digite sua senha para continuar: ")
server=emails.SMTP(servidorSmtp,porta) 
server.starttls()
server.login(email,senha)
mensagem=MIMEMultipart()
mensagem["FROM"]="marcel_86_7@hotmail.com"
mensagem["TO"]="marcel_86_7@hotmail.com"
mensagem["Subject"]="Aula de email Python"
corpo="haaa yeah yeah"
mensagem.attach(MIMEText(corpo,"plain"))
server.sendmail("marcel_86_7@hotmail.com","marcel_86_7@hotmail.com",mensagem.as_string())
server.quit()





    