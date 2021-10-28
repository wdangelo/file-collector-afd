import logging

log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'

logging.basicConfig(filename="logs.log",
                    filemode="a",
                    level=logging.DEBUG,
                    format=log_format
                    )

logger = logging.getLogger('root')

def errorLogs(error: str, task: str) -> str:
    if isinstance(error, str) and isinstance(task, str):
        logger.info(f"{error} - {task}")
        
    else:
        logger.error(
        f"{error} type: {type(error)} - {task} type: {type(task)}"
        )   
         
        
def errorLogsIp(error: str, ip: str) -> str:
    if isinstance(error, str) and isinstance(ip, str):
        logger.info(f"{error} - {ip}")
        
    else:
        logger.error(
        f"{error} type: {type(error)} - {ip} type: {type(ip)}"
        )    

  

def fullname(primeiro_nome: str, segundo_nome: str) -> str:
    
    if isinstance(primeiro_nome, str) and isinstance(segundo_nome, str):
        logger.info(f"{primeiro_nome} {segundo_nome}")
        return primeiro_nome + segundo_nome
    
    else:
        logger.error(
            f"{primeiro_nome} type: {type(primeiro_nome)} - {segundo_nome} type: {type(segundo_nome)}"
        )
        
