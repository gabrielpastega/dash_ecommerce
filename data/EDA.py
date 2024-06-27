#%%
import chardet

with open('BASE_DADOS_CNPJ_FISIOTERAPIA_CURITIBA(BASE_DADOS_CNPJ_FISIOTERAPIA_CU).csv', 'rb') as data:
    result = chardet.detect(data.read())
    print(result)

#%%
import pandas as pd

data_raw = pd.read_csv('BASE_DADOS_CNPJ_FISIOTERAPIA_CURITIBA(BASE_DADOS_CNPJ_FISIOTERAPIA_CU).csv', sep=';', encoding='ISO-8859-1')

data_raw.head()


