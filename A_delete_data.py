from Z_data_base_query import *

#######################################################

inicio_ejecucion=datetime.datetime.now()

mes = '01'
anho='2023'

search_path_root='/config/workspace/root_inicio'
search_path_client='/'+'ENOSA'
search_path_year='/'+anho
search_path_month= '/'+mes+'_'+anho 
search_final_path=search_path_root+search_path_client+search_path_year+search_path_month
search_final_path_data=search_final_path+'/'+'intefase_postgresql.xlsx'
data_postgresql=pd.read_excel(search_final_path_data,sheet_name="nombre_data")

for table_name in data_postgresql['mediciones_tabla_postgres']:
    
    print(table_name)
    
    delete_all_data_in_table("admin",
                            "secret",
                            "172.25.0.1",
                            "5432",
                            "mediciones_cliente"
                            ).delete_data_in_tables(table_name)

print('############### tiempo ejecucion')
print(inicio_ejecucion)
final_ejecucion=datetime.datetime.now()
print(final_ejecucion-inicio_ejecucion)