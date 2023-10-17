from Z_search_for_excelfiles import *

#######################################################

inicio_ejecucion=datetime.datetime.now()

mes = '12'
anho='2022'

search_path_root='/config/workspace/root_inicio'
search_path_client='/'+'ENOSA'
search_path_year='/'+anho
search_path_month= '/'+mes+'_'+anho
search_final_path=search_path_root+search_path_client+search_path_year+search_path_month
search_final_path_data=search_final_path+'/'+'intefase_postgresql.xlsx'
all_client_mesures=check_archives_in_path(search_final_path+'/'+mes+anho+'_ENG_DC').read_archives_in_path()
print(f'se encontraron {len(all_client_mesures)} archivos')
for i in all_client_mesures:
    print(i)