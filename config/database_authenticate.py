import os
from dotenv import load_dotenv
load_dotenv()

database_info = {
    "user": os.getenv('USER_CONTROLL_ID'),
    "password": os.getenv('PASS_CONTROLL_ID')
}

