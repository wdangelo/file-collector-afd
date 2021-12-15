
import pysftp as sftp
from ftplib import FTP
import os
from dotenv import load_dotenv
#from utils.emailConfig.email_config import sending
load_dotenv()

sisbr = {
    "user": os.getenv('USER_SISBR'),
    "password": os.getenv('PASS_SISBR'),
    "domain": os.getenv('DOMAIN_SISBR'),
    "host": os.getenv('HOST_SISBR')
    
}

domain=sisbr["domain"]
user=sisbr["user"]
password=sisbr["password"]
host=sisbr["host"]


remotepath = '/'
localpath = '/home/administrador/www/file-collector-afd/utils/fileUnifier/files/5042.txt'


def sftpUpload():
    try:
        cnopts = sftp.CnOpts(knownhosts='known_hosts')
        cnopts.hostkeys = None
        s = sftp.Connection(
            host=host,
            username=f"{domain}\{user}",
            password=password,
            port=22,
            private_key='.ppk',
            cnopts=cnopts
            )
        
        s.put(localpath)
        
        s.close()
        print('Upload do arquivo afd efetuado!')
        #sending(message='Arquivos enviados com sucesso!')
    except Exception as err:
        print('Erro ao enviar para destino FTP Error: ', err)
        #sending(message=f'Erro ao importar arquivo AFD via FTP: {err}')
        
        
if __name__ == '__main__':

    sftpUpload()





         