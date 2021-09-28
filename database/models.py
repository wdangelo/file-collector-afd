import peewee

# Criamos o banco de dados
db = peewee.SqliteDatabase('codigo_avulso.db')


class BaseModel(peewee.Model):


    class Meta:

        database = db
        
class Url(BaseModel):


    pa = peewee.CharField(unique=True)
    ip = peewee.CharField(unique=True)
    
    
        
        
if __name__ == '__main__':
    try:
        Url.create_table()
        print("Tabela 'Url' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Url' ja existe!")

