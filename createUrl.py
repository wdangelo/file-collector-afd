from models import Url


def handle(pa, ip):
    try:
        urls = {
            'pa': pa,
            'ip': ip
        }
        
        data = [urls]
        
        Url.insert_many(data).execute()
        
        print(f"Cadastro criado com sucesso! {pa} - {ip}")
    except:
        print("Falha ao cadastrar url")
        

if __name__ == '__main__':
    exitCreateUrl = True

    while exitCreateUrl == True:
        
        pa = input("Nome do PA: ")
        ip = input("Endereço 'url' do relógio: ")
        handle(pa, ip)
        exitCreate = input("Continuar cadastrando s/n? : ")
        
        if exitCreate != 's' and exitCreate != 'S' and exitCreate != 'sim' and exitCreate != 'SIM' :
            exitCreateUrl = False