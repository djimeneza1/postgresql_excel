#
'''
import pandas as pd
import numpy as np
import datetime
import ast
import matplotlib.pyplot as plt
import math
from matplotlib.gridspec import GridSpec
'''

import pkg_copy_paste



#ruta='P:/EnerSur/Comercial/Publico/z_escrit_Daniel/server_mercados/desarrollo_BD_peru/simple_peru_test/Data/constraints/irrigations/'

ruta1='P:/EnerSur/Comercial/Publico/z_escrit_Daniel/server_mercados/desarrollo_BD_peru/simple_peru_test/Data/'

ruta2='constraints/irrigations/'

ruta=ruta1+ruta2

archivo='data_constraint_irrigations.csv'

ruta_final=ruta+archivo

'''
dataframe_frame_2=pkg_copy_paste.pd.read_csv(ruta_final) 

ruta_periods='./'

archivo_periods='transform_periods_hour.csv'

ruta_final_periods=ruta_periods+archivo_periods

periods_to_hours=pkg_copy_paste.pd.read_csv(ruta_final_periods)

#calculando fechas


for i in dataframe_frame_2.index:

    dataframe_frame_2.loc[i,'DATE']=pkg_copy_paste.datetime.datetime(year=dataframe_frame_2.loc[i,'YEAR'],
                                                      month=dataframe_frame_2.loc[i,'MONTH'],
                                                      day=dataframe_frame_2.loc[i,'DAY'],
                                                      hour=pkg_copy_paste.np.array(periods_to_hours['HOUR'][periods_to_hours['PERIOD']==dataframe_frame_2.loc[i,'PERIOD']])[0],
                                                      minute=pkg_copy_paste.np.array(periods_to_hours['MINUTE'][periods_to_hours['PERIOD']==dataframe_frame_2.loc[i,'PERIOD']])[0])

#print(dataframe_frame_2)

for column in dataframe_frame_2.columns:

    if column in ['YEAR','MONTH','DAY','PERIOD','DATE']: 
        pass
    else:
        #x=np.array(dataframe_frame_2['DATE'][dataframe_frame_2['DATE']<datetime.datetime(2023,1,1)])
        #y=np.array(dataframe_frame_2[column][dataframe_frame_2['DATE']<datetime.datetime(2023,1,1)])
        x=pkg_copy_paste.np.array(dataframe_frame_2['DATE'])
        y=pkg_copy_paste.np.array(dataframe_frame_2[column])
        fig, ax =pkg_copy_paste.plt.subplots()
        ax.plot(x,y,color='blue')
        ax.set_title(column)
        
        pkg_copy_paste.plt.show()
'''









first_year=2023
last_year=2030

#for column in df_historical.columns:
csv_df_full=archivo

object_fin=pkg_copy_paste.PlexosClassCopyFirstYear.copyfirstyear(first_year,last_year,ruta,csv_df_full)
            #csv_df_full_modificado=object_fin.copy_first_in_other_years_improve()
csv_df_full_modificado=object_fin.copy_first_in_other_years_improve()

csv_df_full_modificado.to_csv(archivo,index=False)