import pkg_copy_paste
import pandas as pd
import numpy as np
import datetime
import ast

inicio = pkg_copy_paste.time.time()

ruta='P:/EnerSur/Comercial/Publico/z_escrit_Daniel/server_mercados/desarrollo_BD_peru/simple_peru_test/Data/natural_inflows_montecarlo/'

archivo_historical='data_historical_inflows.csv'
df_historical=pkg_copy_paste.pd.read_csv(ruta+archivo_historical)

archivo_scenarios='scenario_list.csv'
df_scenarios=pkg_copy_paste.pd.read_csv(ruta+archivo_scenarios)

archivo_periods='transform_periods_hour.csv'
periods_to_hours=pkg_copy_paste.pd.read_csv(ruta+archivo_periods)

first_year=2023
other_year=first_year+1
last_year=2030

'''
inflow_montecarlo=pkg_copy_paste.plexos_crear_csv.CreateDataframeOfMultiYears(first_year,last_year,48,np.array(df_scenarios['SCENARIO']),0)
df_inflow_montecarlo=inflow_montecarlo.funcmultiyear()
'''

column_test=['er_00801_lago_junin']

df_inflow_montecarlo=pkg_copy_paste.pd.read_csv(f'{ruta}data_inflow_{column_test[0]}.csv')

def identificar_bisiesto(year):
    if year%4==0 and (year%100 !=0 or year%400==0):
        a=1
    else:
        a=0
    return a

for other_year in np.arange(first_year+1,last_year+1):

    if identificar_bisiesto(first_year)==0 and identificar_bisiesto(other_year)==1:

        index_first_1=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==1) &
                                                    (df_inflow_montecarlo['DAY']==1) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_first_2=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==28) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        
        index_first_3=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==3) &
                                                    (df_inflow_montecarlo['DAY']==1) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_first_4=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==12) &
                                                    (df_inflow_montecarlo['DAY']==31) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        
        index_first_5=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==28) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_first_6=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==28) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        
        
        index_other_1=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==1) &
                                                    (df_inflow_montecarlo['DAY']==1) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_other_2=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==28) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        
        index_other_3=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==3) &
                                                    (df_inflow_montecarlo['DAY']==1) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_other_4=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==12) &
                                                    (df_inflow_montecarlo['DAY']==31) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        
        index_other_5=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==29) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_other_6=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==29) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]



        indexes_first_12=np.arange(index_first_1,index_first_2+1)
        indexes_other_12=np.arange(index_other_1,index_other_2+1)

        indexes_first_34=np.arange(index_first_3,index_first_4+1)
        indexes_other_34=np.arange(index_other_3,index_other_4+1)

        indexes_first_56=np.arange(index_first_5,index_first_6+1)
        indexes_other_56=np.arange(index_other_5,index_other_6+1)


        for other,first in zip(indexes_other_12,indexes_first_12):

            for column in df_inflow_montecarlo.columns:

                if column in ['YEAR','MONTH','DAY','PERIOD']:

                    pass

                else:

                    df_inflow_montecarlo.loc[other,column]=df_inflow_montecarlo.loc[first,column]
            print(f'indexes_other_12 {other} / indexes_first_12 {first}')


        for other,first in zip(indexes_other_34,indexes_first_34):

            for column in df_inflow_montecarlo.columns:

                if column in ['YEAR','MONTH','DAY','PERIOD']:

                    pass

                else:

                    df_inflow_montecarlo.loc[other,column]=df_inflow_montecarlo.loc[first,column]
            
            print(f'indexes_other_34 {other} / indexes_first_34 {first}')


        for other,first in zip(indexes_other_56,indexes_first_56):

            for column in df_inflow_montecarlo.columns:

                if column in ['YEAR','MONTH','DAY','PERIOD']:

                    pass

                else:

                    df_inflow_montecarlo.loc[other,column]=df_inflow_montecarlo.loc[first,column]

            print(f'indexes_other_56 {other} / indexes_first_56 {first}')

    elif (identificar_bisiesto(first_year)==0 and identificar_bisiesto(other_year)==0) or (identificar_bisiesto(first_year)==1 and identificar_bisiesto(other_year)==1):

        index_first_1=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==1) &
                                                    (df_inflow_montecarlo['DAY']==1) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_first_2=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==12) &
                                                    (df_inflow_montecarlo['DAY']==31) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        
        index_other_1=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==1) &
                                                    (df_inflow_montecarlo['DAY']==1) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_other_2=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==12) &
                                                    (df_inflow_montecarlo['DAY']==31) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        
        indexes_first_12=np.arange(index_first_1,index_first_2+1)
        indexes_other_12=np.arange(index_other_1,index_other_2+1)
        
        for other,first in zip(indexes_other_12,indexes_first_12):

            for column in df_inflow_montecarlo.columns:

                if column in ['YEAR','MONTH','DAY','PERIOD']:

                    pass

                else:

                    df_inflow_montecarlo.loc[other,column]=df_inflow_montecarlo.loc[first,column]
            print(f'indexes_other_12 {other} / indexes_first_12 {first}')

    elif identificar_bisiesto(first_year)==1 and identificar_bisiesto(other_year)==0:


        index_first_1=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==1) &
                                                    (df_inflow_montecarlo['DAY']==1) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_first_2=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==28) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        
        index_first_3=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==3) &
                                                    (df_inflow_montecarlo['DAY']==1) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_first_4=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==12) &
                                                    (df_inflow_montecarlo['DAY']==31) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        '''
        index_first_5=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==29) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_first_6=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==first_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==29) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        '''
        
        index_other_1=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==1) &
                                                    (df_inflow_montecarlo['DAY']==1) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_other_2=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==28) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        
        index_other_3=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==3) &
                                                    (df_inflow_montecarlo['DAY']==1) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_other_4=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==12) &
                                                    (df_inflow_montecarlo['DAY']==31) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
        
        '''
        index_other_5=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==29) &
                                                    (df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
        
        index_other_6=df_inflow_montecarlo.index[(df_inflow_montecarlo['YEAR']==other_year) & 
                                                    (df_inflow_montecarlo['MONTH']==2) &
                                                    (df_inflow_montecarlo['DAY']==29) &
                                                    (df_inflow_montecarlo['PERIOD']==48)].to_list()[0]

        '''

        indexes_first_12=np.arange(index_first_1,index_first_2+1)
        indexes_other_12=np.arange(index_other_1,index_other_2+1)

        indexes_first_34=np.arange(index_first_3,index_first_4+1)
        indexes_other_34=np.arange(index_other_3,index_other_4+1)


        for other,first in zip(indexes_other_12,indexes_first_12):

            for column in df_inflow_montecarlo.columns:

                if column in ['YEAR','MONTH','DAY','PERIOD']:

                    pass

                else:

                    df_inflow_montecarlo.loc[other,column]=df_inflow_montecarlo.loc[first,column]
            print(f'indexes_other_12 {other} / indexes_first_12 {first}')


        for other,first in zip(indexes_other_34,indexes_first_34):

            for column in df_inflow_montecarlo.columns:

                if column in ['YEAR','MONTH','DAY','PERIOD']:

                    pass

                else:

                    df_inflow_montecarlo.loc[other,column]=df_inflow_montecarlo.loc[first,column]
            
            print(f'indexes_other_34 {other} / indexes_first_34 {first}')


df_inflow_montecarlo.to_csv(f'{ruta}data_inflow_{column_test[0]}_prueba.csv',index=False) #data_inflows_es_02007_el_frayle   