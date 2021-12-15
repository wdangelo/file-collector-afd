import os
from dotenv import load_dotenv
load_dotenv()

controll_id = {
    "user": os.getenv('USER_CONTROLL_ID'),
    "password": os.getenv('PASS_CONTROLL_ID')
}

sisbr = {
    "user": os.getenv('USER_SISBR'),
    "password": os.getenv('PASS_SISBR'),
    "domain": os.getenv('DOMAIN_SISBR'),
    "host": os.get('HOST_SISBR')
    
}

