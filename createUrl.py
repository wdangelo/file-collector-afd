from models import Url


def handle(pa, ip, url):
    try:
        urls = {
            'pa': pa,
            'ip': ip,
            'url': url
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
        ip = input("Endereço 'ip' do relógio: ")
        url = input("Endereço 'url' do relógio: ")
        handle(pa, ip, url)
        exitCreate = input("Continuar cadastrando s/n? : ")
        
        if exitCreate != 's' and exitCreate != 'S' and exitCreate != 'sim' and exitCreate != 'SIM' :
            exitCreateUrl = False