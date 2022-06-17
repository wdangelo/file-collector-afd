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
    sending(message=f'Segue anexo arquivo AFD contendo todos os PAs')


try:  
    schedule.every().day.at("08:10").do(deleteFiles)
    schedule.every().day.at("08:15").do(downloadFilesAFd)
    schedule.every().day.at("08:40").do(moveFilesAfd)
    schedule.every().day.at("08:42").do(fileUnifier)
    schedule.every().day.at("08:45").do(uploadSftpAfd)
    schedule.every().day.at("08:50").do(sendMailFile)
    
    
    
except Exception as err:
    sending(message=f'Erro ao importar arquivo AFD via FTP: {err}')
    errorLogs(err, task=schedule)
    print("Erro", err)


while 1:
    schedule.run_pending()
    time.sleep(10)
    



