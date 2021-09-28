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