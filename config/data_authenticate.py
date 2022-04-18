import os
from dotenv import load_dotenv
load_dotenv()

controll_id = {
    "user": os.getenv('USER_CONTROLL_ID'),
    "password": os.getenv('PASS_CONTROLL_ID')
}


