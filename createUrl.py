from models import Url
from tkinter import * 


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
    
    def test():
        pa = name_pa.get()
        ip = ip_address.get()
        url = url_address.get()
        handle(pa, ip, url)
        
    
    window = Tk()
    window.title("Cadastro de novos Relógios")  
    text_body = Label(window, text="Cadastro de novos relógios")
    text_body.grid(column=0, row=0)
    
    nome_pa_label = Label(window, text="Nome do PA: ")
    nome_pa_label.grid(column=0, row=1)
    name_pa = Entry(window, width=20)
    name_pa.grid(column=1, row=1)
    
    ip_address_label = Label(window, text="Endereço de IP: ")
    ip_address_label.grid(column=0, row=2)
    ip_address = Entry(window, width=20)
    ip_address .grid(column=1, row=2)
    
    url_address_label = Label(window, text="Endereço URL: ")
    url_address_label.grid(column=0, row=3)
    url_address = Entry(window, width=20)
    url_address.grid(column=1, row=3)
    
    
    
    btn_confirm = Button(window, text="Confirmar", command=test)
    btn_confirm.grid(column=0, row=6)
    

    window.mainloop()