
'''
import pandas as pd
import numpy as np
import datetime
import ast
'''

import pkg_copy_paste

class crear_escenarios_from_historicos_diarios():
    
    def __init__(self,ruta_root,df_historical,df_scenarios,periods_to_hours,first_year,last_year,df_inflow_montecarlo):

        self.ruta_root=ruta_root
        self.df_historical=df_historical
        self.df_scenarios=df_scenarios
        self.periods_to_hours=periods_to_hours
        self.first_year=first_year
        self.last_year=last_year
        self.df_inflow_montecarlo=df_inflow_montecarlo

    def crear_escenarios_inflows_improved(self):

        for column_test in self.df_historical.columns:

            if self.df_historical[column_test].sum()!=0:

                if column_test in ['YEAR','MONTH','DAY','PERIOD']:

                    pass

                else:

                    #asignar escenario en los afluentes historicos
                    self.df_historical['scen']=0

                    self.df_historical['year_scen']=0

                    for i in pkg_copy_paste.np.arange(pkg_copy_paste.np.shape(self.df_historical)[0]):

                        if self.df_historical.loc[i,'YEAR'] in pkg_copy_paste.np.array(self.df_scenarios['YEAR']):

                            self.df_historical.loc[i,'scen']=pkg_copy_paste.np.array(self.df_scenarios['SCENARIO'][self.df_scenarios['YEAR']==self.df_historical.loc[i,'YEAR']])[0]

                            self.df_historical.loc[i,'year_scen']=self.first_year

                    self.df_historical=self.df_historical[self.df_historical['scen']>0]

                    self.df_historical=pkg_copy_paste.pd.DataFrame(pkg_copy_paste.np.array(self.df_historical),columns=self.df_historical.columns)


                    for k in self.df_scenarios['SCENARIO']:#[df_scenarios['SCENARIO']<=28]

                        self.df_historical_scen=self.df_historical[self.df_historical['scen']==k]
                        self.df_historical_scen=pkg_copy_paste.pd.DataFrame(pkg_copy_paste.np.array(self.df_historical_scen),columns=self.df_historical_scen.columns)

                        indice_j=0

                        for i in range(pkg_copy_paste.np.shape(self.df_historical_scen)[0]):

                            if self.df_historical_scen['MONTH'][i]==2 and self.df_historical_scen['DAY'][i]==29:
                                day_h=28
                            else:
                                day_h=int(self.df_historical_scen['DAY'][i])
                            
                            date_historical=pkg_copy_paste.datetime.datetime(year=int(self.df_historical_scen['year_scen'][i]),
                                                                month=int(self.df_historical_scen['MONTH'][i]),
                                                                day=day_h,
                                                                hour=int(pkg_copy_paste.np.array(self.periods_to_hours['HOUR'][self.periods_to_hours['PERIOD']==self.df_historical_scen.loc[i,'PERIOD']])[0]),
                                                                minute=int(pkg_copy_paste.np.array(self.periods_to_hours['MINUTE'][self.periods_to_hours['PERIOD']==self.df_historical_scen.loc[i,'PERIOD']])[0]))


                            for j in range(indice_j,pkg_copy_paste.np.shape(self.df_inflow_montecarlo)[0]):

                                date_inflows=pkg_copy_paste.datetime.datetime(year=int(self.df_inflow_montecarlo['YEAR'][j]),
                                                                month=int(self.df_inflow_montecarlo['MONTH'][j]),
                                                                day=int(self.df_inflow_montecarlo['DAY'][j]),
                                                                hour=int(pkg_copy_paste.np.array(self.periods_to_hours['HOUR'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[i,'PERIOD']])[0]),
                                                                minute=int(pkg_copy_paste.np.array(self.periods_to_hours['MINUTE'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[i,'PERIOD']])[0]))

                                if date_historical>=date_inflows:
                                    self.df_inflow_montecarlo.loc[j,k]=self.df_historical_scen.loc[i,column_test]  
                                else:
                                    indice_j=j
                                    break

                                indice_last_j=j
                                
                                #print(f'scen={k} / date_historical= {i}:{date_historical} / date_inflows= {j}:{date_inflows} / indice_j= {indice_j} / indice_last_j= {indice_last_j}')

                        date_inflows_last=pkg_copy_paste.datetime.datetime(year=int(self.df_inflow_montecarlo['YEAR'][indice_last_j]),
                                                            month=int(self.df_inflow_montecarlo['MONTH'][indice_last_j]),
                                                            day=int(self.df_inflow_montecarlo['DAY'][indice_last_j]),
                                                            hour=int(pkg_copy_paste.np.array(self.periods_to_hours['HOUR'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]),
                                                            minute=int(pkg_copy_paste.np.array(self.periods_to_hours['MINUTE'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]))

                        
                        while date_inflows_last<=pkg_copy_paste.datetime.datetime(self.first_year,12,31,23,30):

                            self.df_inflow_montecarlo.loc[indice_last_j,k]=self.df_inflow_montecarlo.loc[indice_last_j-1,k]

                            indice_last_j+=1

                            #print(f'date_inflows_last = {date_inflows_last}')

                            date_inflows_last=pkg_copy_paste.datetime.datetime(year=int(self.df_inflow_montecarlo['YEAR'][indice_last_j]),
                                                            month=int(self.df_inflow_montecarlo['MONTH'][indice_last_j]),
                                                            day=int(self.df_inflow_montecarlo['DAY'][indice_last_j]),
                                                            hour=int(pkg_copy_paste.np.array(self.periods_to_hours['HOUR'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]),
                                                            minute=int(pkg_copy_paste.np.array(self.periods_to_hours['MINUTE'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]))
                            
                    self.df_inflow_montecarlo.to_csv(f'{self.ruta_root}data_inflow_{column_test}.csv',index=False) 
                        
        return print("creacion de archivos finalizado")




























    def crear_escenarios_inflows(self):

        for column_test in self.df_historical.columns:

            if column_test in ['YEAR','MONTH','DAY','PERIOD']:

                pass

            else:

                #asignar escenario en los afluentes historicos
                self.df_historical['scen']=0

                self.df_historical['year_scen']=0

                for i in pkg_copy_paste.np.arange(pkg_copy_paste.np.shape(self.df_historical)[0]):

                    if self.df_historical.loc[i,'YEAR'] in pkg_copy_paste.np.array(self.df_scenarios['YEAR']):

                        self.df_historical.loc[i,'scen']=pkg_copy_paste.np.array(self.df_scenarios['SCENARIO'][self.df_scenarios['YEAR']==self.df_historical.loc[i,'YEAR']])[0]
                        self.df_historical.loc[i,'year_scen']=self.first_year

                self.df_historical=self.df_historical[self.df_historical['scen']>0]

                self.df_historical=pkg_copy_paste.pd.DataFrame(pkg_copy_paste.np.array(self.df_historical),columns=self.df_historical.columns)


                for k in self.df_scenarios['SCENARIO']:#[df_scenarios['SCENARIO']<=28]

                    self.df_historical_scen=self.df_historical[self.df_historical['scen']==k]
                    self.df_historical_scen=pkg_copy_paste.pd.DataFrame(pkg_copy_paste.np.array(self.df_historical_scen),columns=self.df_historical_scen.columns)

                    indice_j=0

                    for i in range(pkg_copy_paste.np.shape(self.df_historical_scen)[0]):

                        if self.df_historical_scen['MONTH'][i]==2 and self.df_historical_scen['DAY'][i]==29:
                            day_h=28
                        else:
                            day_h=int(self.df_historical_scen['DAY'][i])
                        
                        date_historical=pkg_copy_paste.datetime.datetime(year=int(self.df_historical_scen['year_scen'][i]),
                                                            month=int(self.df_historical_scen['MONTH'][i]),
                                                            day=day_h,
                                                            hour=int(pkg_copy_paste.np.array(self.periods_to_hours['HOUR'][self.periods_to_hours['PERIOD']==self.df_historical_scen.loc[i,'PERIOD']])[0]),
                                                            minute=int(pkg_copy_paste.np.array(self.periods_to_hours['MINUTE'][self.periods_to_hours['PERIOD']==self.df_historical_scen.loc[i,'PERIOD']])[0]))


                        for j in range(indice_j,pkg_copy_paste.np.shape(self.df_inflow_montecarlo)[0]):

                            date_inflows=pkg_copy_paste.datetime.datetime(year=int(self.df_inflow_montecarlo['YEAR'][j]),
                                                            month=int(self.df_inflow_montecarlo['MONTH'][j]),
                                                            day=int(self.df_inflow_montecarlo['DAY'][j]),
                                                            hour=int(pkg_copy_paste.np.array(self.periods_to_hours['HOUR'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[i,'PERIOD']])[0]),
                                                            minute=int(pkg_copy_paste.np.array(self.periods_to_hours['MINUTE'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[i,'PERIOD']])[0]))

                            if date_historical>=date_inflows:
                                self.df_inflow_montecarlo.loc[j,k]=self.df_historical_scen.loc[i,column_test]  
                            else:
                                indice_j=j
                                break

                            indice_last_j=j
                            
                            #print(f'scen={k} / date_historical= {i}:{date_historical} / date_inflows= {j}:{date_inflows} / indice_j= {indice_j} / indice_last_j= {indice_last_j}')

                    date_inflows_last=pkg_copy_paste.datetime.datetime(year=int(self.df_inflow_montecarlo['YEAR'][indice_last_j]),
                                                        month=int(self.df_inflow_montecarlo['MONTH'][indice_last_j]),
                                                        day=int(self.df_inflow_montecarlo['DAY'][indice_last_j]),
                                                        hour=int(pkg_copy_paste.np.array(self.periods_to_hours['HOUR'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]),
                                                        minute=int(pkg_copy_paste.np.array(self.periods_to_hours['MINUTE'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]))

                    
                    while date_inflows_last<=pkg_copy_paste.datetime.datetime(self.first_year,12,31,23,30):

                        self.df_inflow_montecarlo.loc[indice_last_j,k]=self.df_inflow_montecarlo.loc[indice_last_j-1,k]

                        indice_last_j+=1

                        #print(f'date_inflows_last = {date_inflows_last}')

                        date_inflows_last=pkg_copy_paste.datetime.datetime(year=int(self.df_inflow_montecarlo['YEAR'][indice_last_j]),
                                                        month=int(self.df_inflow_montecarlo['MONTH'][indice_last_j]),
                                                        day=int(self.df_inflow_montecarlo['DAY'][indice_last_j]),
                                                        hour=int(pkg_copy_paste.np.array(self.periods_to_hours['HOUR'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]),
                                                        minute=int(pkg_copy_paste.np.array(self.periods_to_hours['MINUTE'][self.periods_to_hours['PERIOD']==self.df_inflow_montecarlo.loc[indice_last_j,'PERIOD']])[0]))
                        
                self.df_inflow_montecarlo.to_csv(f'{self.ruta_root}data_inflow_{column_test}.csv',index=False) 
                        
        return print("creacion de archivos finalizado")
