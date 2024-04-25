# Enviando email

import smtplib as emails #biblioteca para enviar email
import getpass as gt   #biblioteca para ocultar senha


email = "marcel_86_7@hotmail.com"
senha=gt.getpass("Digite sua senha para continuar: ")

#Lista Destinatários: 
listaDestinatario=["marcel_86_7@hotmail.com"] #,'marcel.rosa@itau-unibanco.com.br']

for destinatario in listaDestinatario:
    smtp=emails.SMTP("smtp-mail.outlook.com",587)
    smtp.ehlo() #verificação conexão email
    smtp.starttls() #verificar criptografia do email
    smtp.ehlo() #fecha a conexão email
    smtp.login(email,senha)
    
# Criar mensagem

assunto="Curso de Python"
conteudo="Email enviado com codigo Python"
mensagem=f"Subject: {assunto}\n\n\n {conteudo}"

#envia email

smtp.sendmail(email,destinatario,mensagem)
smtp.close()
    
    