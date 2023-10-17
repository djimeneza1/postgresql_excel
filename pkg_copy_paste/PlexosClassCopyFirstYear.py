
'''
import pandas as pd
import numpy as np
import datetime
import ast
'''
#import pkg_copy_paste

class copyfirstyear():

    def __init__(self,first_year,last_year,csv_ruta,csv_df_full):

        self.first_year=first_year

        self.last_year=last_year

        self.csv_ruta=csv_ruta

        self.csv_df_full=csv_df_full

    def identificar_bisiesto(self,year):

        if year%4==0 and (year%100 !=0 or year%400==0):
            a=1
        else:
            a=0
        return a

    def copy_first_in_other_years_improve(self):

        self.df_inflow_montecarlo=pkg_copy_paste.pd.read_csv(f'{self.csv_ruta}{self.csv_df_full}')

        for other_year in pkg_copy_paste.np.arange(self.first_year+1,self.last_year+1):

            if self.identificar_bisiesto(self.first_year)==0 and self.identificar_bisiesto(other_year)==1:

                index_first_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_first_3=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==3) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_4=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_first_5=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_6=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                
                index_other_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_other_3=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==3) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_4=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_other_5=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_6=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]

                indexes_first_12=pkg_copy_paste.np.arange(index_first_1,index_first_2+1)
                indexes_other_12=pkg_copy_paste.np.arange(index_other_1,index_other_2+1)

                indexes_first_34=pkg_copy_paste.np.arange(index_first_3,index_first_4+1)
                indexes_other_34=pkg_copy_paste.np.arange(index_other_3,index_other_4+1)

                indexes_first_56=pkg_copy_paste.np.arange(index_first_5,index_first_6+1)
                indexes_other_56=pkg_copy_paste.np.arange(index_other_5,index_other_6+1)

                columns_p=[]
                for i in self.df_inflow_montecarlo.columns:
                    if i in ['YEAR','MONTH','DAY','PERIOD']:
                        pass
                    else:
                        columns_p.append(i)

                df_other_12=pkg_copy_paste.pd.DataFrame(pkg_copy_paste.np.array(self.df_inflow_montecarlo.loc[indexes_first_12,columns_p]),
                                                        index=indexes_other_12,
                                                        columns=columns_p)
                
                df_other_34=pkg_copy_paste.pd.DataFrame(pkg_copy_paste.np.array(self.df_inflow_montecarlo.loc[indexes_first_34,columns_p]),
                                                        index=indexes_other_34,
                                                        columns=columns_p)

                
                df_other_56=pkg_copy_paste.pd.DataFrame(pkg_copy_paste.np.array(self.df_inflow_montecarlo.loc[indexes_first_56,columns_p]),
                                                        index=indexes_other_56,
                                                        columns=columns_p)
                
                #df_other_paste=pkg_copy_paste.pd.concat([df_other_12,df_other_34,df_other_56])
                
                self.df_inflow_montecarlo=self.df_inflow_montecarlo.update(df_other_12)
                print(f'indexes_other_12 / indexes_first_12 ')

                self.df_inflow_montecarlo=self.df_inflow_montecarlo.update(df_other_34)
                print(f'indexes_other_34  / indexes_first_34 ')

                self.df_inflow_montecarlo=self.df_inflow_montecarlo.update(df_other_56)
                print(f'indexes_other_56  / indexes_first_56 ')

            elif (self.identificar_bisiesto(self.first_year)==0 and self.identificar_bisiesto(other_year)==0) or (self.identificar_bisiesto(self.first_year)==1 and self.identificar_bisiesto(other_year)==1):

                index_first_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_other_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                indexes_first_12=pkg_copy_paste.np.arange(index_first_1,index_first_2+1)
                indexes_other_12=pkg_copy_paste.np.arange(index_other_1,index_other_2+1)
                
                #columns_p=pkg_copy_paste.np.arange(1,31).astype(str)
                columns_p=[]
                for i in self.df_inflow_montecarlo.columns:
                    if i in ['YEAR','MONTH','DAY','PERIOD']:
                        pass
                    else:
                        columns_p.append(i)

                df_other_12=pkg_copy_paste.pd.DataFrame(pkg_copy_paste.np.array(self.df_inflow_montecarlo.loc[indexes_first_12,columns_p]),
                                                        index=indexes_other_12,
                                                        columns=columns_p)
                
                #df_other_paste=pkg_copy_paste.pd.concat([df_other_12,df_other_34,df_other_56])
                
                self.df_inflow_montecarlo=self.df_inflow_montecarlo.update(df_other_12)
                print(f'indexes_other_12 / indexes_first_12 ')
                

            elif self.identificar_bisiesto(self.first_year)==1 and self.identificar_bisiesto(other_year)==0:


                index_first_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_first_3=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==3) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_4=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                '''
                index_first_5=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_6=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                '''
                
                index_other_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_other_3=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==3) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_4=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                '''
                index_other_5=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_6=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]

                '''

                indexes_first_12=pkg_copy_paste.np.arange(index_first_1,index_first_2+1)
                indexes_other_12=pkg_copy_paste.np.arange(index_other_1,index_other_2+1)

                indexes_first_34=pkg_copy_paste.np.arange(index_first_3,index_first_4+1)
                indexes_other_34=pkg_copy_paste.np.arange(index_other_3,index_other_4+1)

                #columns_p=pkg_copy_paste.np.arange(1,31).astype(str)
                columns_p=[]
                for i in self.df_inflow_montecarlo.columns:
                    if i in ['YEAR','MONTH','DAY','PERIOD']:
                        pass
                    else:
                        columns_p.append(i)

                df_other_12=pkg_copy_paste.pd.DataFrame(pkg_copy_paste.np.array(self.df_inflow_montecarlo.loc[indexes_first_12,columns_p]),
                                                        index=indexes_other_12,
                                                        columns=columns_p)
                
                df_other_34=pkg_copy_paste.pd.DataFrame(pkg_copy_paste.np.array(self.df_inflow_montecarlo.loc[indexes_first_34,columns_p]),
                                                        index=indexes_other_34,
                                                        columns=columns_p)
                
                #df_other_paste=pkg_copy_paste.pd.concat([df_other_12,df_other_34,df_other_56])
                
                self.df_inflow_montecarlo=self.df_inflow_montecarlo.update(df_other_12)
                print(f'indexes_other_12 / indexes_first_12 ')

                self.df_inflow_montecarlo=self.df_inflow_montecarlo.update(df_other_34)
                print(f'indexes_other_34  / indexes_first_34 ')

        return self.df_inflow_montecarlo   
    
































































    def copy_first_in_other_years(self):

        self.df_inflow_montecarlo=pkg_copy_paste.pd.read_csv(f'{self.csv_ruta}{self.csv_df_full}')

        for other_year in pkg_copy_paste.np.arange(self.first_year+1,self.last_year+1):

            if self.identificar_bisiesto(self.first_year)==0 and self.identificar_bisiesto(other_year)==1:

                index_first_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_first_3=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==3) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_4=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_first_5=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_6=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                
                index_other_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_other_3=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==3) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_4=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_other_5=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_6=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]



                indexes_first_12=pkg_copy_paste.np.arange(index_first_1,index_first_2+1)
                indexes_other_12=pkg_copy_paste.np.arange(index_other_1,index_other_2+1)

                indexes_first_34=pkg_copy_paste.np.arange(index_first_3,index_first_4+1)
                indexes_other_34=pkg_copy_paste.np.arange(index_other_3,index_other_4+1)

                indexes_first_56=pkg_copy_paste.np.arange(index_first_5,index_first_6+1)
                indexes_other_56=pkg_copy_paste.np.arange(index_other_5,index_other_6+1)


                for other,first in zip(indexes_other_12,indexes_first_12):

                    for column in self.df_inflow_montecarlo.columns:

                        if column in ['YEAR','MONTH','DAY','PERIOD']:

                            pass

                        else:

                            self.df_inflow_montecarlo.loc[other,column]=self.df_inflow_montecarlo.loc[first,column]
                    print(f'indexes_other_12 {other} / indexes_first_12 {first}')


                for other,first in zip(indexes_other_34,indexes_first_34):

                    for column in self.df_inflow_montecarlo.columns:

                        if column in ['YEAR','MONTH','DAY','PERIOD']:

                            pass

                        else:

                            self.df_inflow_montecarlo.loc[other,column]=self.df_inflow_montecarlo.loc[first,column]
                    
                    print(f'indexes_other_34 {other} / indexes_first_34 {first}')


                for other,first in zip(indexes_other_56,indexes_first_56):

                    for column in self.df_inflow_montecarlo.columns:

                        if column in ['YEAR','MONTH','DAY','PERIOD']:

                            pass

                        else:

                            self.df_inflow_montecarlo.loc[other,column]=self.df_inflow_montecarlo.loc[first,column]

                    print(f'indexes_other_56 {other} / indexes_first_56 {first}')

            elif (self.identificar_bisiesto(self.first_year)==0 and self.identificar_bisiesto(other_year)==0) or (self.identificar_bisiesto(self.first_year)==1 and self.identificar_bisiesto(other_year)==1):

                index_first_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_other_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                indexes_first_12=pkg_copy_paste.np.arange(index_first_1,index_first_2+1)
                indexes_other_12=pkg_copy_paste.np.arange(index_other_1,index_other_2+1)
                
                for other,first in zip(indexes_other_12,indexes_first_12):

                    for column in self.df_inflow_montecarlo.columns:

                        if column in ['YEAR','MONTH','DAY','PERIOD']:

                            pass

                        else:

                            self.df_inflow_montecarlo.loc[other,column]=self.df_inflow_montecarlo.loc[first,column]
                    print(f'indexes_other_12 {other} / indexes_first_12 {first}')

            elif self.identificar_bisiesto(self.first_year)==1 and self.identificar_bisiesto(other_year)==0:


                index_first_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_first_3=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==3) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_4=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                '''
                index_first_5=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_first_6=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==self.first_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                '''
                
                index_other_1=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==1) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_2=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==28) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                index_other_3=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==3) &
                                                            (self.df_inflow_montecarlo['DAY']==1) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_4=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==12) &
                                                            (self.df_inflow_montecarlo['DAY']==31) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]
                
                '''
                index_other_5=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==1)].to_list()[0]
                
                index_other_6=self.df_inflow_montecarlo.index[(self.df_inflow_montecarlo['YEAR']==other_year) & 
                                                            (self.df_inflow_montecarlo['MONTH']==2) &
                                                            (self.df_inflow_montecarlo['DAY']==29) &
                                                            (self.df_inflow_montecarlo['PERIOD']==48)].to_list()[0]

                '''

                indexes_first_12=pkg_copy_paste.np.arange(index_first_1,index_first_2+1)
                indexes_other_12=pkg_copy_paste.np.arange(index_other_1,index_other_2+1)

                indexes_first_34=pkg_copy_paste.np.arange(index_first_3,index_first_4+1)
                indexes_other_34=pkg_copy_paste.np.arange(index_other_3,index_other_4+1)


                for other,first in zip(indexes_other_12,indexes_first_12):

                    for column in self.df_inflow_montecarlo.columns:

                        if column in ['YEAR','MONTH','DAY','PERIOD']:

                            pass

                        else:

                            self.df_inflow_montecarlo.loc[other,column]=self.df_inflow_montecarlo.loc[first,column]
                    print(f'indexes_other_12 {other} / indexes_first_12 {first}')


                for other,first in zip(indexes_other_34,indexes_first_34):

                    for column in self.df_inflow_montecarlo.columns:

                        if column in ['YEAR','MONTH','DAY','PERIOD']:

                            pass

                        else:

                            self.df_inflow_montecarlo.loc[other,column]=self.df_inflow_montecarlo.loc[first,column]
                    
                    print(f'indexes_other_34 {other} / indexes_first_34 {first}')

        return self.df_inflow_montecarlo 