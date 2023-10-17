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
last_year=2030
inflow_montecarlo=pkg_copy_paste.plexos_crear_csv.CreateDataframeOfMultiYears(first_year,last_year,48,np.array(df_scenarios['SCENARIO']),0)
df_inflow_montecarlo=inflow_montecarlo.funcmultiyear()
#df_inflow_montecarlo=df_inflow_montecarlo_total[df_inflow_montecarlo_total['YEAR']<=first_year]

column_test=['er_00801_lago_junin']

#asignar escenario en los afluentes historicos
df_historical['scen']=0
df_historical['year_scen']=0
for i in np.arange(np.shape(df_historical)[0]):
    if df_historical.loc[i,'YEAR'] in np.array(df_scenarios['YEAR']):
        df_historical.loc[i,'scen']=np.array(df_scenarios['SCENARIO'][df_scenarios['YEAR']==df_historical.loc[i,'YEAR']])[0]
        df_historical.loc[i,'year_scen']=first_year

df_historical=df_historical[df_historical['scen']>0]

df_historical=pkg_copy_paste.pd.DataFrame(np.array(df_historical),columns=df_historical.columns)


for k in df_scenarios['SCENARIO']:#[df_scenarios['SCENARIO']<=28]

    df_historical_scen=df_historical[df_historical['scen']==k]
    df_historical_scen=pkg_copy_paste.pd.DataFrame(np.array(df_historical_scen),columns=df_historical_scen.columns)

    indice_j=0

    for i in range(np.shape(df_historical_scen)[0]):

        if df_historical_scen['MONTH'][i]==2 and df_historical_scen['DAY'][i]==29:
            day_h=28
        else:
            day_h=int(df_historical_scen['DAY'][i])
        
        date_historical=datetime.datetime(year=int(df_historical_scen['year_scen'][i]),
                                            month=int(df_historical_scen['MONTH'][i]),
                                            day=day_h,
                                            hour=int(np.array(periods_to_hours['HOUR'][periods_to_hours['PERIOD']==df_historical_scen.loc[i,'PERIOD']])[0]),
                                            minute=int(np.array(periods_to_hours['MINUTE'][periods_to_hours['PERIOD']==df_historical_scen.loc[i,'PERIOD']])[0]))


        for j in range(indice_j,np.shape(df_inflow_montecarlo)[0]):

            date_inflows=datetime.datetime(year=int(df_inflow_montecarlo['YEAR'][j]),
                                            month=int(df_inflow_montecarlo['MONTH'][j]),
                                            day=int(df_inflow_montecarlo['DAY'][j]),
                                            hour=int(np.array(periods_to_hours['HOUR'][periods_to_hours['PERIOD']==df_inflow_montecarlo.loc[i,'PERIOD']])[0]),
                                            minute=int(np.array(periods_to_hours['MINUTE'][periods_to_hours['PERIOD']==df_inflow_montecarlo.loc[i,'PERIOD']])[0]))

            if date_historical>=date_inflows:
                df_inflow_montecarlo.loc[j,k]=df_historical_scen.loc[i,column_test[0]]  
            else:
                indice_j=j
                break

            indice_last_j=j
            
            print(f'scen={k} / date_historical= {i}:{date_historical} / date_inflows= {j}:{date_inflows} / indice_j= {indice_j} / indice_last_j= {indice_last_j}')

    date_inflows_last=datetime.datetime(year=int(df_inflow_montecarlo['YEAR'][indice_last_j]),
                                        month=int(df_inflow_montecarlo['MONTH'][indice_last_j]),
                                        day=int(df_inflow_montecarlo['DAY'][indice_last_j]),
                                        hour=int(np.array(periods_to_hours['HOUR'][periods_to_hours['PERIOD']==df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]),
                                        minute=int(np.array(periods_to_hours['MINUTE'][periods_to_hours['PERIOD']==df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]))

    
    while date_inflows_last<=datetime.datetime(first_year,12,31,23,30):

        df_inflow_montecarlo.loc[indice_last_j,k]=df_inflow_montecarlo.loc[indice_last_j-1,k]

        indice_last_j+=1

        print(f'date_inflows_last = {date_inflows_last}')

        date_inflows_last=datetime.datetime(year=int(df_inflow_montecarlo['YEAR'][indice_last_j]),
                                        month=int(df_inflow_montecarlo['MONTH'][indice_last_j]),
                                        day=int(df_inflow_montecarlo['DAY'][indice_last_j]),
                                        hour=int(np.array(periods_to_hours['HOUR'][periods_to_hours['PERIOD']==df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]),
                                        minute=int(np.array(periods_to_hours['MINUTE'][periods_to_hours['PERIOD']==df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]))

    #print(df_inflow_montecarlo[(df_inflow_montecarlo['YEAR']<=2023) & (df_inflow_montecarlo[k]>0)])

df_inflow_montecarlo.to_csv(f'{ruta}data_inflow_{column_test[0]}.csv',index=False) #data_inflows_es_02007_el_frayle
