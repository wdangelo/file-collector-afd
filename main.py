import time
import schedule
from fileCollectorBrowser import execute

from utils.moveFileDownload.moveFileDownloadAfd import moveFileDownloadAfdFromToFileUnifier_files
from utils.deleteFileAfd.delete import deleteFilesForPathFiles
from utils.fileUnifier.fileUnifierAdf import unifier
from utils.ftpUploadAfd.ftp_upload import sftpUpload


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


    
schedule.every().day.at("20:30").do(deleteFiles)
schedule.every().day.at("20:32").do(downloadFilesAFd)
schedule.every().day.at("20:40").do(moveFilesAfd)
schedule.every().day.at("20:42").do(fileUnifier)
schedule.every().day.at("20:45").do(uploadSftpAfd)


while 1:
    
    schedule.run_pending()
    time.sleep(5)
    



