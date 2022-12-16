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
    

def sendMailFile():
    print("Arquivo enviado com secesso")
    #sending(message=f'Segue anexo arquivo AFD contendo todos os PAs')
    pass


try:  
    schedule.every().day.at("22:00").do(deleteFiles)
    schedule.every().day.at("22:05").do(downloadFilesAFd)
    schedule.every().day.at("23:05").do(moveFilesAfd)
    schedule.every().day.at("23:10").do(fileUnifier)
    schedule.every().day.at("23:15").do(uploadSftpAfd)
    schedule.every().day.at("23:20").do(sendMailFile)
    
    
    
except Exception as err:
    sending(message=f'Erro ao importar arquivo AFD via FTP: {err}')
    errorLogs(err, task=schedule)
    print("Erro", err)


while 1:
    schedule.run_pending()
    time.sleep(10)
    



