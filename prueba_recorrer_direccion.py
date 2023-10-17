import os
import pandas as pd
import numpy as np
from datetime import datetime

print('###############')
'''
path_root='/config/workspace/proyecto_oswalk/root_inicio'
path_client='/'+'ENOSA'
path_year='/'+'2022'
path_month= '/'+'04_2022'

path_archive_data='/'+'042022_ENG_DC'

path_final=path_root+path_client+path_year+path_month
print(path_final+path_archive_data)
data=[]

os.chdir(path_final+path_archive_data)
for root, dirs, files in os.walk('.', topdown = False):
    for name in files:
        data.append(name)
print(data)
'''

ruta='P:/EnerSur/Comercial/Publico/z_escrit_Daniel/server_mercados/desarrollo_BD_peru/simple_peru_test/Data/natural_inflows_montecarlo/'
pd_nombres=pd.read_csv(f'{ruta}/cambio_nombres.csv')
print(pd_nombres)
print(np.array(pd_nombres['correcto'][pd_nombres['incorrecto']=='data_inflow_eh_00000_angel2.csv'])[0])
data=[]
os.chdir(ruta)
for root, dirs, files in os.walk('.', topdown = False):
    for name in files:
        #data.append(name)
        estado=datetime.fromtimestamp(os.stat(name).st_mtime)
        tamanho=os.stat(name).st_size
        data_files=[name,estado,tamanho]
        data.append(data_files)
        if name in pd_nombres['incorrecto'].to_list():
            os.rename(name,np.array(pd_nombres['correcto'][pd_nombres['incorrecto']==name])[0])
dataframe_resultado=pd.DataFrame(data,columns=['nombre','modificacion','tamanho'])
dataframe_resultado.to_csv(f'{ruta}prueba_dataframe.csv')        
print(data)



