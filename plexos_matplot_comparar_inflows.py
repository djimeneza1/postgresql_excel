import pkg_copy_paste
import pandas as pd
import numpy as np
import datetime
import ast
import matplotlib.pyplot as plt
import math
from matplotlib.gridspec import GridSpec


#ruta='P:/EnerSur/Comercial/Publico/z_escrit_Daniel/server_mercados/desarrollo_BD_peru/simple_peru_dev/Data/constraints/irrigations/'

ruta1='P:/EnerSur/Comercial/Publico/z_escrit_Daniel/server_mercados/desarrollo_BD_peru/simple_peru_dev/Data/'

ruta2='load/'

ruta=ruta1+ruta2

ruta='./'

archivo='Historical_Inflows_DJ_prueba.csv'

archivo_2='data_plantilla_embalses.csv'

ruta_final=ruta+archivo

ruta_final_2=ruta+archivo_2

dataframe_frame_2=pkg_copy_paste.pd.read_csv(ruta_final) 

dataframe_frame_2_2=pkg_copy_paste.pd.read_csv(ruta_final_2) 

ruta_periods='./'

archivo_periods='transform_periods_hour.csv'

ruta_final_periods=ruta_periods+archivo_periods

periods_to_hours=pkg_copy_paste.pd.read_csv(ruta_final_periods)

#calculando fechas


for i in dataframe_frame_2.index:

    dataframe_frame_2.loc[i,'DATE']=datetime.datetime(year=dataframe_frame_2.loc[i,'YEAR'],
                                                      month=dataframe_frame_2.loc[i,'MONTH'],
                                                      day=dataframe_frame_2.loc[i,'DAY'],
                                                      hour=np.array(periods_to_hours['HOUR'][periods_to_hours['PERIOD']==dataframe_frame_2.loc[i,'PERIOD']])[0],
                                                      minute=np.array(periods_to_hours['MINUTE'][periods_to_hours['PERIOD']==dataframe_frame_2.loc[i,'PERIOD']])[0])
    

for i in dataframe_frame_2_2.index:

    dataframe_frame_2_2.loc[i,'DATE']=datetime.datetime(year=dataframe_frame_2_2.loc[i,'YEAR'],
                                                      month=dataframe_frame_2_2.loc[i,'MONTH'],
                                                      day=dataframe_frame_2_2.loc[i,'DAY'],
                                                      hour=np.array(periods_to_hours['HOUR'][periods_to_hours['PERIOD']==dataframe_frame_2_2.loc[i,'PERIOD']])[0],
                                                      minute=np.array(periods_to_hours['MINUTE'][periods_to_hours['PERIOD']==dataframe_frame_2_2.loc[i,'PERIOD']])[0])

#print(dataframe_frame_2)

for column in dataframe_frame_2.columns:

    if column in ['YEAR','MONTH','DAY','PERIOD','DATE']: 
        pass
    else:
        #x=np.array(dataframe_frame_2['DATE'][dataframe_frame_2['DATE']<datetime.datetime(2023,1,1)])
        #y=np.array(dataframe_frame_2[column][dataframe_frame_2['DATE']<datetime.datetime(2023,1,1)])

        for column_2 in dataframe_frame_2_2.columns:

            if column_2==column:

                x=np.array(dataframe_frame_2['DATE'])
                y=np.array(dataframe_frame_2[column])

                x2=np.array(dataframe_frame_2_2['DATE'])
                y2=np.array(dataframe_frame_2_2[column_2])

                fig, ax =plt.subplots()
                ax.plot(x,y,color='blue',label='historical_plexos',linestyle='--')
                ax.plot(x2,y2,color='red',label='historical engie',linestyle='dashdot')
                ax.legend()
                ax.set_title(column)


        
        plt.show()

'''
fig, axs =plt.subplots(nrows=2,ncols=math.ceil(len(dataframe_frame_2.columns)/2),figsize=(10,10))
for column in dataframe_frame_2.columns: 
    if column in ['YEAR','MONTH','DAY','PERIOD']: 
        pass
    else:
        for row in range(1):
            for col in range(math.ceil(len(dataframe_frame_2.columns)/2)):
                x=np.array(dataframe_frame_2.index)
                y=np.array(dataframe_frame_2[column])
                axs[row,col].plot(x,y,color='green')
                axs[row,col].set_title(column)


fig, axs =plt.subplots(nrows=2,ncols=math.ceil(len(dataframe_frame_2.columns)/2),figsize=(10,10))
for row in range(1):
    for col in range(math.ceil(len(dataframe_frame_2.columns)/2)):
        for column in dataframe_frame_2.columns: 
            if column in ['YEAR','MONTH','DAY','PERIOD']: 
                pass
            else:
                x=np.array(dataframe_frame_2.index)
                y=np.array(dataframe_frame_2[column])
                axs[row,col].plot(x,y,color='green')
                axs[row,col].set_title(column)

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.tick_params(labelbottom=False,labelleft=False)

df_index_column=pd.DataFrame(np.array(dataframe_frame_2.columns),columns=['name_columns'])

fig=plt.figure()
#gs=fig.add_gridspec(nrows=2,ncols=math.ceil(len(dataframe_frame_2.columns)/2))
#gs=fig.add_gridspec(nrows=2,ncols=math.ceil(len(dataframe_frame_2.columns)/2))

gs=GridSpec(nrows=2,ncols=math.ceil(len(dataframe_frame_2.columns)/2),figure=fig)

index_p=0
for row in range(2):
    index_p=0
    for col in range(math.ceil(len(dataframe_frame_2.columns)/2)):
        ax=fig.add_subplot(row+1,col+1,index_p+1)
        x_index=index_p+4
        y_index=df_index_column.loc[x_index]
        x=np.array(dataframe_frame_2.index)
        y=np.array(dataframe_frame_2[y_index])
        ax.plot(x,y,color='red')
        #ax.set_title(y_index)
        index_p+=1
format_axes(fig)
plt.show()
      
        
#print(dataframe_frame_2)

#print(periods_to_hours)

'''