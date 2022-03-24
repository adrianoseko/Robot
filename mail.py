

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(msg, destinatario):
    
    # Configuração
    host = 'smtp.gmail.com'
    port = 587
    user = 'adriano.jorge.moraes@gmail.com'
    password = ''

    # Criando objeto
    print('Criando objeto servidor...')
    server = smtplib.SMTP(host, port)

    # Login com servidor
    print('Login...')
    server.ehlo()
    server.starttls()
    server.login(user, password)

    # Criando mensagem
    message = msg
    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = destinatario
    email_msg['Subject'] = 'Teste Robot Framework'
    print('Adicionando texto...')
    email_msg.attach(MIMEText(message, 'plain'))

    # Enviando mensagem
    print('Enviando mensagem...')
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    print('Mensagem enviada!')
    server.quit()
    

    return(msg)

def mail(msg):
    
    # Passando e-mails para a função send
    destinatario = ['adriano.jorge.moraes@gmail.com','apoio.ti@agrofito.com.br']
    for n in destinatario:
        send(msg, n)
    return(msg)
