import pkg_copy_paste
'''
ruta='P:/EnerSur/Comercial/Publico/z_escrit_Daniel/server_mercados/desarrollo_BD_peru/simple_peru_test/Data/natural_inflows_montecarlo/'
archivo='data_inflow_er_00801_lago_junin_prueba_2.csv'
object_final=pkg_copy_paste.PlexosClassCopyFirstYear.copyfirstyear(2023,2030,ruta,archivo)
dataframe_final=object_final.copy_first_in_other_years()


dataframe_final.to_csv(f'{ruta}{archivo}',index=False) #data_inflows_es_02007_el_frayle   
'''






'''
ruta='P:/EnerSur/Comercial/Publico/z_escrit_Daniel/server_mercados/desarrollo_BD_peru/simple_peru_test/Data/natural_inflows_montecarlo/'

archivo_historical='data_historical_inflows.csv'
df_historical=pkg_copy_paste.pd.read_csv(ruta+archivo_historical)

archivo_scenarios='scenario_list.csv'
df_scenarios=pkg_copy_paste.pd.read_csv(ruta+archivo_scenarios)

archivo_periods='transform_periods_hour.csv'
periods_to_hours=pkg_copy_paste.pd.read_csv(ruta+archivo_periods)

first_year=2023
last_year=2030
inflow_montecarlo=pkg_copy_paste.PlexosClassCrearCsv.CreateDataframeOfMultiYears(first_year,last_year,48,pkg_copy_paste.np.array(df_scenarios['SCENARIO']),0)
df_inflow_montecarlo=inflow_montecarlo.funcmultiyear()

prueba=pkg_copy_paste.PlexosClassCrearEscenarios.crear_escenarios_from_historicos_diarios(ruta,df_historical,df_scenarios,periods_to_hours,first_year,last_year,df_inflow_montecarlo)

df_prueba=prueba.crear_escenarios_inflows_improved()
'''









ruta='P:/EnerSur/Comercial/Publico/z_escrit_Daniel/server_mercados/desarrollo_BD_peru/simple_peru_test/Data/natural_inflows_montecarlo/'

archivo_historical='data_historical_inflows.csv'
df_historical=pkg_copy_paste.pd.read_csv(ruta+archivo_historical)

archivo_cambios='lista_archivos_para_cambio.csv'
df_archivocambios=pkg_copy_paste.pd.read_csv(ruta+archivo_cambios)

first_year=2023
last_year=2030

#for column in df_historical.columns:
csv_df_full='data_historical_inflows.csv'

object_fin=pkg_copy_paste.PlexosClassCopyFirstYear.copyfirstyear(first_year,last_year,ruta,csv_df_full)

            #csv_df_full_modificado=object_fin.copy_first_in_other_years_improve()
csv_df_full_modificado=object_fin.copy_first_in_other_years_improve()

csv_df_full_modificado.to_csv(csv_df_full,index=False)