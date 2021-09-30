import os


def moveFileDownloadAfdFromToFileUnifier_files():
    
    try:
    
        os.chdir('/home/administrador/Downloads/')
        #lista os arquivos da pasta Downloads
        for file in os.listdir():
            os.rename(file, "/home/administrador/www/file-collector-afd/utils/fileUnifier/files/" + file)
        
        print(f'Arquivos os arquvios foram movidos com sucesso')
        
    except (NameError):
        print(f"Erro interno ao mover arquivos: {NameError}")
    

if __name__ == '__main__':
    moveFileDownloadAfdFromToFileUnifier_files()