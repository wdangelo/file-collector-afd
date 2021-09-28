from createUrl import handle

exitCreateUrl = True

while exitCreateUrl == True:
    
    pa = input("Nome do PA: ")
    ip = input("Endereço 'url' do relógio: ")
    handle(pa, ip)
    exitCreate = input("Continuar cadastrando s/n? : ")
    
    if exitCreate != 's' and exitCreate != 'S' and exitCreate != 'sim' and exitCreate != 'SIM' :
        exitCreateUrl = False



