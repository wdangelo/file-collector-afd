import os

#"/home/administrador/www/file-collector-afd/utils/fileUnifier/files/"
#C:\bots\file-collector-afd\utils\fileUnifier\files>
downloads = os.path.join("c:\\", "Users", "williama2009_00", "Downloads")

def moveFileDownloadAfdFromToFileUnifier_files():
    path = os.path.join("c:\\", "bots", "file-collector-afd", "utils", "fileUnifier", "files", "")
    
    try:
        
        os.chdir(downloads)
        #lista os arquivos da pasta Downloads
        for file in os.listdir():
            os.rename(file, path + file)
        
        print(f'Arquivos os arquvios foram movidos com sucesso')
        
    except (NameError):
        print(f"Erro interno ao mover arquivos: {NameError}")
    

if __name__ == '__main__':
    moveFileDownloadAfdFromToFileUnifier_files()