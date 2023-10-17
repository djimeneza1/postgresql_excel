
'''
import pandas as pd
import numpy as np
import datetime
import ast
'''
import pkg_copy_paste

class ArrayMonthDaysPeriods():

    def __init__(self,year,month,periodsperdays):
        self.year=year
        self.month=month
        self.periodsperdays=periodsperdays

    def funcNumberOfDaysInMonth(self):
        if self.month in pkg_copy_paste.np.array([1,3,5,7,8,10,12]):
            self.number_days_in_month=31
        elif self.month in pkg_copy_paste.np.array([4,6,9,11]):
            self.number_days_in_month=30
        elif self.month in pkg_copy_paste.np.array([2]):
            if self.year%4==0 and (self.year%100 !=0 or self.year%400==0):
                self.number_days_in_month=29
            else:
                self.number_days_in_month=28
        return self.number_days_in_month

    def funcArrayOfPeriodsInDay(self):
        self.array_of_periods_in_day=pkg_copy_paste.np.arange(1,self.periodsperdays+1,dtype=int)
        return self.array_of_periods_in_day
    
    def funcArrayOfPeriodsInMonth(self):
        self.array_of_periods_in_month=pkg_copy_paste.np.tile(self.funcArrayOfPeriodsInDay(),self.funcNumberOfDaysInMonth()).astype(int)
        return self.array_of_periods_in_month
    
    def funArrayOfDaysInMonth(self):
        self.array_of_days_in_month=pkg_copy_paste.np.array([])
        for i in pkg_copy_paste.np.arange(1,self.funcNumberOfDaysInMonth()+1):
            array=pkg_copy_paste.np.tile(pkg_copy_paste.np.array([i]),pkg_copy_paste.np.shape(self.funcArrayOfPeriodsInDay())[0])
            self.array_of_days_in_month=pkg_copy_paste.np.append(self.array_of_days_in_month,array).astype(int)
        return self.array_of_days_in_month

    def funcArraysOfMonthInMonth(self):
        self.array_of_month_in_month=self.month*pkg_copy_paste.np.ones_like(self.funArrayOfDaysInMonth())
        return self.array_of_month_in_month
    
    def funcArrayYearsInMonth(self):
        self.array_of_year_in_month=self.year*pkg_copy_paste.np.ones_like(self.funArrayOfDaysInMonth()).astype(int)
        return self.array_of_year_in_month
    
    def funcArrayMonthDaysPeriods(self):
        self.array_month_day_periods=pkg_copy_paste.np.stack((self.funcArrayYearsInMonth(),
                                                self.funcArraysOfMonthInMonth(),
                                                self.funArrayOfDaysInMonth(),
                                                self.funcArrayOfPeriodsInMonth()),axis=1).astype(int)
        return self.array_month_day_periods
    

class CreateDataframeOfMonth(ArrayMonthDaysPeriods):

    def __init__(self,
                 year,
                 month,
                 periodsperdays,
                 array_columns,
                 data_complete_blanks):
        
        super().__init__(year,month,periodsperdays)
        self.array_columns=array_columns
        self.data_complete_blanks=data_complete_blanks

    def funcDfOfIndexes(self):

        df_indexes=pkg_copy_paste.pd.DataFrame(self.funcArrayMonthDaysPeriods(),columns=['YEAR','MONTH','DAY','PERIOD'])
        data_DF=self.data_complete_blanks*pkg_copy_paste.np.ones((pkg_copy_paste.np.shape(self.funcArrayMonthDaysPeriods())[0],pkg_copy_paste.np.shape(self.array_columns)[0]))      
        df_data=pkg_copy_paste.pd.DataFrame(data_DF,columns=self.array_columns)
        self.DF_final=df_indexes.join(df_data)
        return self.DF_final
    

class CreateDataframeOfMultiMonths(CreateDataframeOfMonth):

    def __init__(self,
                 year,
                 month_init,
                 month_end,
                 periodsperdays,
                 array_columns,
                 data_complete_blanks):

        super().__init__(year,month_init,periodsperdays,array_columns,data_complete_blanks)
        self.month_init=month_init
        self.month_end=month_end

    def funcmultimonth(self):

        self.DF_final_multimonth=CreateDataframeOfMonth(self.year,self.month_init,self.periodsperdays,self.array_columns,self.data_complete_blanks).funcDfOfIndexes()
        for month_loop in pkg_copy_paste.np.arange(self.month_init+1,self.month_end+1):
            prueba=CreateDataframeOfMonth(self.year,month_loop,self.periodsperdays,self.array_columns,self.data_complete_blanks).funcDfOfIndexes()
            self.DF_final_multimonth=pkg_copy_paste.pd.concat([self.DF_final_multimonth,prueba])
        return self.DF_final_multimonth
    
class CreateDataframeOfMultiYears(CreateDataframeOfMultiMonths):

    def __init__(self,
                 year_init,
                 year_end,
                 periodsperdays,
                 array_columns,
                 data_complete_blanks):
        
        super().__init__(year_init,
                        1,
                        12,
                        periodsperdays,
                        array_columns,
                        data_complete_blanks)
        
        self.year_init=year_init
        self.year_end=year_end

    def funcmultiyear(self):

        self.DF_final_multiyear=CreateDataframeOfMultiMonths(self.year_init,1,12,self.periodsperdays,self.array_columns,self.data_complete_blanks).funcmultimonth()
        for year_loop in pkg_copy_paste.np.arange(self.year_init+1,self.year_end+1):
            prueba=CreateDataframeOfMultiMonths(year_loop,1,12,self.periodsperdays,self.array_columns,self.data_complete_blanks).funcmultimonth()
            self.DF_final_multiyear=pkg_copy_paste.pd.concat([self.DF_final_multiyear,prueba])
        
        indices=pkg_copy_paste.pd.Series(pkg_copy_paste.np.arange(0,pkg_copy_paste.np.shape(self.DF_final_multiyear)[0]))
        self.DF_final_multiyear=self.DF_final_multiyear.set_index(indices)

        return self.DF_final_multiyear

class ModifyDataFrameMultiYears(CreateDataframeOfMultiYears):

    def __init__(self,
                 year_init,
                 year_end,
                 periodsperdays,
                 array_columns,
                 data_complete_blanks,
                 dataframe_modif):
        
        super().__init__(year_init,
                         year_end,
                         periodsperdays,
                         array_columns,
                         data_complete_blanks)

        self.dataframe_modif=dataframe_modif

    def parse_tuple(self,string):
            try:
                s = pkg_copy_paste.ast.literal_eval(str(string))
                if type(s) == tuple:
                    return s
                return
            except:
                return
            
    def funCalcDifDates(self):

        iterate=pkg_copy_paste.np.shape(self.dataframe_modif)[0]
        range_iterate=pkg_copy_paste.np.arange(0,iterate)
        data_diff_dates=pkg_copy_paste.np.array([])
        data_periods_init=pkg_copy_paste.np.array([])
        data_periods_end=pkg_copy_paste.np.array([])

        for i in range_iterate:
            date_from=self.parse_tuple(self.dataframe_modif['date_init'].loc[i])
            date_to=self.parse_tuple(self.dataframe_modif['date_end'].loc[i])
            date_from_i=pkg_copy_paste.datetime.datetime(date_from[0],date_from[1],date_from[2],date_from[3],date_from[4])
            date_to_i=pkg_copy_paste.datetime.datetime(date_to[0],date_to[1],date_to[2],date_to[3],date_to[4])
            diff_date_to_from=date_to_i-date_from_i
            periods_changed=divmod(diff_date_to_from.days*24*60*60+diff_date_to_from.seconds,3600/(self.periodsperdays/24)) 
            data_diff_dates=pkg_copy_paste.np.append(data_diff_dates,int(periods_changed[0]))
            
            period_from_p=date_from[3]*self.periodsperdays/24+date_from[4]/(60/(self.periodsperdays/24))+1
            tuple_string_from= "("+str(date_from[0])+","+str(date_from[1])+","+str(date_from[2])+","+str(int(period_from_p))+")"
            data_periods_init=pkg_copy_paste.np.append(data_periods_init,tuple_string_from)
           
            period_to_p=date_to[3]*self.periodsperdays/24+date_to[4]/(60/(self.periodsperdays/24))+1
            tuple_string_to= "("+str(date_to[0])+","+str(date_to[1])+","+str(date_to[2])+","+str(int(period_to_p))+")"
            data_periods_end=pkg_copy_paste.np.append(data_periods_end,tuple_string_to)

        self.dataframe_modif['periods_change']=data_diff_dates
        self.dataframe_modif['date_init_p']=data_periods_init
        self.dataframe_modif['date_end_p']=data_periods_end

        return self.dataframe_modif
    
    def funChangeDataInDataframeColumn(self):

        iterate=pkg_copy_paste.np.shape(self.funCalcDifDates())[0] #2850
        range_iterate=pkg_copy_paste.np.arange(0,iterate) #0-2849

        dataframe_fin=CreateDataframeOfMultiYears(self.year_init,
                                                    self.year_end,
                                                    self.periodsperdays,
                                                    self.array_columns,
                                                    self.data_complete_blanks).funcmultiyear()

        for i in range_iterate:

            print('mantenimiento '+str(i)+' para la central '+str(self.funCalcDifDates()['unit'].loc[i])+' a la hora inicial '+str(self.funCalcDifDates()['date_init'].loc[i]))

            date_from=self.parse_tuple(self.funCalcDifDates()['date_init_p'].loc[i])

            index_inicio=dataframe_fin.index[(dataframe_fin['YEAR']==date_from[0]) &
                                                (dataframe_fin['MONTH']==date_from[1]) &
                                                (dataframe_fin['DAY']==date_from[2]) &
                                                (dataframe_fin['PERIOD']==date_from[3])].to_list()
            
            dataframe_fin.loc[index_inicio[0]:index_inicio[0]+self.funCalcDifDates()['periods_change'].loc[i],self.funCalcDifDates()['unit'].loc[i]]+=self.funCalcDifDates()['value_replace'].loc[i]
                    
            self.data_frame_fin_mod=dataframe_fin

        return self.data_frame_fin_mod
        

##################################################################################################################################################################

