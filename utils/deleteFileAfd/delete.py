import os, shutil

def deleteFilesForPathFiles():
    
    folder = '/home/administrador/www/file-collector-afd/utils/fileUnifier/files'
    
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #Elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    deleteFilesForPathFiles()

