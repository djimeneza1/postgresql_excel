import pkg_copy_paste
import pandas as pd
import numpy as np
import datetime
import ast

inicio = pkg_copy_paste.time.time()

df_embalses=pkg_copy_paste.pd.read_csv('./data_embalses.csv')

data_columnas=np.array(df_embalses['embalses'].to_list())

data_embalses_days=pkg_copy_paste.plexos_crear_csv.CreateDataframeOfMultiYears(1965,2022,1,data_columnas,0)

plantilla_embalses=data_embalses_days.funcmultiyear()

data_historical=pkg_copy_paste.pd.read_csv('./data_historical_inflows.csv')

indice_j=0

for i in range(np.shape(data_historical)[0]):

    date_historical=datetime.datetime(data_historical['YEAR'][i],data_historical['MONTH'][i],data_historical['DAY'][i])

    for j in range(indice_j,np.shape(plantilla_embalses)[0]):

        date_embalses=datetime.datetime(plantilla_embalses['YEAR'][j],plantilla_embalses['MONTH'][j],plantilla_embalses['DAY'][j])

        if date_historical>=date_embalses:

            for k in data_columnas:

                plantilla_embalses.loc[j,k]=data_historical.loc[i,k]
        
        else:

            indice_j=j

            break
        
        print(f'date_historical= {i} / date_embalses= {j}')


plantilla_embalses.to_csv('./data_plantilla_embalses.csv',index=False)






'''
date_from_i=datetime.datetime(date_from[0],date_from[1],date_from[2],date_from[3],date_from[4])
            date_to_i=datetime.datetime(date_to[0],date_to[1],date_to[2],date_to[3],date_to[4])
            diff_date_to_from=date_to_i-date_from_i
            periods_changed=divmod(diff_date_to_from.days*24*60*60+diff_date_to_from.seconds,3600/(self.periodsperdays/24)) 
            data_diff_dates=np.append(data_diff_dates,int(periods_changed[0]))



data_columnas=pkg_copy_paste.np.array(df_embalses['embalses'])   

#print(data_columnas)

dataframe_manttos=pd.read_csv('./manto_thermal.csv') 

prueba4=pkg_copy_paste.ModifyDataFrameMultiYears(2023,2024,48,data_columnas,0,dataframe_manttos)

#dataframe_final=prueba4.funcmultiyear()

#dataframe_final.to_csv('./plantilla-data-final.csv')

#df_calcdifdates=prueba4.funCalcDifDates()

#df_calcdifdates.to_csv('./plantilla-calcdifdate-final.csv')

dataframe_fin_mod=prueba4.funChangeDataInDataframeColumn()

dataframe_fin_mod.to_csv('./plexos_mantto_hidros.csv')

final=pkg_copy_paste.time.time()
   
print(f'ejecucion finalizada de copy and paste en {final-inicio} segundos')
'''