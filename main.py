import time
import schedule
from fileCollectorBrowser import execute

from utils.moveFileDownload.moveFileDownloadAfd import moveFileDownloadAfdFromToFileUnifier_files
from utils.deleteFileAfd.delete import deleteFilesForPathFiles
from utils.fileUnifier.fileUnifierAdf import unifier


def deleteFiles():
    deleteFilesForPathFiles()
    
    

def downloadFilesAFd():
    execute()
    
    
def moveFilesAfd():
    moveFileDownloadAfdFromToFileUnifier_files()
    

def fileUnifier():
    unifier()
    
    
schedule.every().day.at("13:00").do(deleteFiles)
schedule.every().day.at("13:01").do(downloadFilesAFd)
schedule.every().day.at("13:06").do(moveFilesAfd)
schedule.every().day.at("13:11").do(fileUnifier)



while 1:
    
    schedule.run_pending()
    time.sleep(5)
    



