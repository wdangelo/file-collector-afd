import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

def handle():

    today = date.today()
    rangetendays = relativedelta(days=10)
    anterior = today - rangetendays

    datetendaysago = anterior.strftime('%d/%m/%Y')

    return datetendaysago


if __name__ == '__main__':
    print(handle())