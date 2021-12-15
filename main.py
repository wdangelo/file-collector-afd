import time
import schedule
from fileCollectorBrowser import execute
from utils.emailConfig.email_config import sending

from utils.moveFileDownload.moveFileDownloadAfd import moveFileDownloadAfdFromToFileUnifier_files
from utils.deleteFileAfd.delete import deleteFilesForPathFiles
from utils.fileUnifier.fileUnifierAdf import unifier
from utils.ftpUploadAfd.ftp_upload import sftpUpload
from utils.logs.app import errorLogs


print("---- Coleta de Arquivos do Sistema de Ponto ATIVO ----")

def deleteFiles():
    deleteFilesForPathFiles()
    
    

def downloadFilesAFd():
    execute()
    
    
def moveFilesAfd():
    moveFileDownloadAfdFromToFileUnifier_files()
    

def fileUnifier():
    unifier()
    

def uploadSftpAfd():
    sftpUpload()


try:  
    schedule.every().day.at("18:04").do(deleteFiles)
    schedule.every().day.at("18:10").do(downloadFilesAFd)
    schedule.every().day.at("18:25").do(moveFilesAfd)
    schedule.every().day.at("18:35").do(fileUnifier)
    schedule.every().day.at("18:45").do(uploadSftpAfd)
    
except Exception as err:
    sending(message=f'Erro ao importar arquivo AFD via FTP: {err}')
    errorLogs(err, task=schedule)
    print("Erro", err)


while 1:
    print('agenda')
    schedule.run_pending()
    time.sleep(10)
    



