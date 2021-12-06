# File Collector AFD
### Script para coleta de arquivos AFD, de relógios ponto da marca Controll ID

- Acessa o sistema de cada relógio cadastrado.

- Unifica todos os arquivos em um unico com node de 'name'.

- Acessa servidor FTP e envia o arquivo 'name'

##

# Issues 

[ x ] Criar espaço de 10 dias na data de coleta dos arquivos

[ x ] Direcionar os arquivos para uma pasta especifica

[ x ] Juntar os arquivos

[ x ] Deletar arquivos ja baixados antes de iniciar o doenload de novos arquivos

[ x ] Acessar FTP e enviar arquivo criado 

[ x ] Enviar e-mail com logs "Success" ou "Error" dos passos do bot

[ x  ] Criar arquivo de logs dos erros e succes

        [ x ] Criar log ao tentar acessar o ip do relógio ponto
        [ ] Criar log ao tentar executar uma tarefa no arquivo main.py
        [ ] Criar log ao tentar deletar os arquivos da pasta files
        [ ] Criar log ao tentar enviar e-mail
        [ ] Criar log ao tenar unificar os Arquivos
        [ ] Criar log ao tentar enviar o arquivo AFD para o SFTP 


[ x ] Automatizar no sistema operacional

[ x ] Criar interface para cadastro de Relógios

[ x ] Fazer teste de ip disponivel caso nao esteja passar para o proximo endereço

[  ] Criar ambiente docker para rodar em produção no serviror