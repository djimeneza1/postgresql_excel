from read_file_dj import * 

import os
import pandas as pd
import numpy as np

 
#'/config/workspace/proyecto_oswalk/root_inicio/ENOSA/2022/04_2022

print('###############')

path_root='/config/workspace/root_inicio'
path_client='/'+'ENOSA'
path_year='/'+'2022'
path_month= '/'+'11_2022'

path_archive_data='/'+'112022_ENG_DC'

path_final=path_root+path_client+path_year+path_month
print(path_final+path_archive_data)
data=[]

os.chdir(path_final+path_archive_data)
for root, dirs, files in os.walk('.', topdown = False):
    for name in files:
        data.append(name)
        print(name)
#print(data)

'''
dict_med_lib_enosa={}
for archive_final in data:
    path_archive_final=path_final+'/'+path_archive_data+'/'+archive_final
    required_df = pd.read_excel(path_archive_final, usecols = [1, 2]).drop([0,2])
    m_array=np.delete(required_df.values,0,0)
    df_array=pd.DataFrame(m_array,columns=['pot','ener'])
    dict_med_lib_enosa[archive_final]=df_array

#print(dict_med_lib_enosa['042022_ENG_DC_STEVIA.xlsx'])
'''
print('###############')

dict_verificar={}
for ii in data:
    for jj in archivos:
        verif=0
        if ii != jj:
            verif=0
        else:
            verif=1
            break
    dict_verificar[ii]=verif
    
#print(dict_verificar)

print('###############')

dict_verificar_1={}
for ii in archivos:
    for jj in data:
        verif=0
        if ii != jj:
            verif=0
        else:
            verif=1
            break
    dict_verificar_1[ii]=verif

#rint(dict_verificar_1)