
import pysftp as sftp
from ftplib import FTP


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
    except Exception as err:
        print('Error: ', err)
        

sftpUpload()





         