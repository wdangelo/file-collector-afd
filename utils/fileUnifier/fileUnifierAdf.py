import os
import codecs

import pandas as pd
path = '/home/administrador/www/file-collector-afd/utils/fileUnifier/files/'


def unifier():
        
    os.chdir(path)

    def read_text_file(file_path):
        with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            
            df = f.read()
            return df


    def create_text_file(file_path):


        with codecs.open('5042.txt', 'a', encoding='utf-8', errors='ignore') as f:
            f.write(str(read_text_file(file_path)) + "\n")


    for file in os.listdir():

        if file.endswith(".txt"):
            file_path = f"{path}{file}"
            create_text_file(file_path)
            
            

if __name__ == '__main__':
    unifier()