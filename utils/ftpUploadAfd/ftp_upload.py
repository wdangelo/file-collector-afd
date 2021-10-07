
import pysftp as sftp
from ftplib import FTP
from utils.emailConfig.email_config import sending


remotepath = '/'
localpath = '/home/administrador/www/file-collector-afd/utils/fileUnifier/files/5042.txt'


def sftpUpload():
    try:
        cnopts = sftp.CnOpts(knownhosts='known_hosts')
        cnopts.hostkeys = None
        s = sftp.Connection(
            host='172.16.0.150',
            username='sicoob\williana5042_00',
            password='@sicoob15',
            port=22,
            private_key='.ppk',
            cnopts=cnopts
            )
        
        s.put(localpath)
        
        s.close()
        print('Upload do arquivo afd efetuado!')
        sending(message='Arquivos enviados com sucesso!')
    except Exception as err:
        print('Error: ', err)
        sending(message=f'Erro ao importar arquivo AFD via FTP: {err}')

sftpUpload()





         