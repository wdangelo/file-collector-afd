import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

def sending(message):
    
    date_hour_now = datetime.now()
    date_hour_now_format = date_hour_now.strftime(f" data: %d/%m/%Y -  Hora: %H:%M")
    text_mail_body = f'''
                        {date_hour_now_format}
                        Robo RH Informa. 
                        Mensagem: {message}
                      '''

    # email remetente, senha, destinatário
    email_from = 'wdangelo1983@gmail.com'
    email_password = '@sicoob05'
    email_to = 'rh.rioclaro@sicoob.com.br'
    #email_to2 = 'informatica.5042@sicoob.com.br'
    
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = email_from
    message['To'] = email_to
    #message['To'] = email_to2
    message['Subject'] = '# Robo RH Importação arquivo do ponto!!'   #Título do e-mail
    
        # Corpo do E-mail com anexos
    message.attach(MIMEText(text_mail_body, 'plain'))
    
    path_file = os.path.join("c:\\", "bots", "file-collector-afd", "utils", "fileUnifier", "files", "5042.txt")
    attchment = open(path_file, 'rb')
    
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition', f'attachment; filename=5042.txt')
    attchment.close()
    
    message.attach(att)
    
        # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
    session.ehlo()
    session.starttls()  # Habilita a segurança
    session.login(email_from, email_password)  # Login e senha de quem envia o e-mail
    text = message.as_string()
    session.sendmail(email_from, email_to, text)
    session.quit()
    
    
if __name__ == '__main__':
    
    sending(message='Teste de envio do e-mail Robo')