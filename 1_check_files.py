from Z_data_base_query import *
from Z_search_for_excelfiles import *

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
all_client_mesures=check_archives_in_path(search_final_path+'/'+mes+anho+'_ENG_DC').read_archives_in_path()
print(f'se encontraron {len(all_client_mesures)} archivos')
for i in all_client_mesures:
    print(i)

list_of_files=[]
for i in all_client_mesures:
    string_name = 'medicion_'+i.lower()[7:len(i)-5]
    list_of_files.append(string_name)

tables_in_db = show_all_tables_in_db("admin",
                                    "secret",
                                    "172.25.0.1",
                                    "5432",
                                    "mediciones_cliente"
                                    ).tables_in_db()

list_of_tables_in_db=[]
for i in range(len(tables_in_db)):
    list_of_tables_in_db.append(tables_in_db[i][0])

list_exclude_files=['medicion_eng_dc_agroindustrias_del_chira_s.r.l._sum10878332_cl',
                    'medicion_eng_dc_agropesca_del_perú_sum17815058-cl',
                    'medicion_eng_dc_negocios _del_sur_del_peru_cl',
                    'medicion_eng_dc_promotora_inmobiliaria_industrial_de_piura_s.a.c_sum16464548_cl',
                    'medicion_eng_dc_fabrica_de_hielo_hielofish s.a.c_sum15289354_tumbes_cl']

list_of_files_not_in_tables=[]
for files in list_of_files:
    if files not in list_of_tables_in_db:
        if files not in list_exclude_files:
            list_of_files_not_in_tables.append(files)
print(f'el archivo nuevo que no esta en base de datos es: {list_of_files_not_in_tables}')

list_exclude_tables=[   'nombre_clientes',
                        'nombre_contratos',
                        'tipo_clientes',
                        'nombre_mercado',
                        'nombre_barra_referencia',
                        'nombre_barra_suministro',
                        'nombre_licitacion',
                        'nombre_oferta',
                        'nombre_barra_facturacion',

                        'medicion_eng_dc_grupo_camposur_cl',
                        'medicion_eng_dc_musterion_sum15602345_cl',
                        'medicion_eng_dc_musterion_sum15783189_cl',
                        'medicion_eng_dc_depositos_sum12546000_cl',
                        'medicion_eng_dc_agricola_del_chira_la_huaca_sum12557756',
                        'medicion_eng_dc_consorcio_fegurri_sta_regina',
                        'medicion_eng_dc_donpacking_sum10843050',
                        'medicion_eng_dc_hielo_polar',
                        'medicion_eng_dc_santa_monica',
                        'medicion_eng_dc_seafrost',
                        'medicion_eng_dc_seafrost_sum12316977',
                        'medicion_eng_dc_sucroalcolera',

                        'medicion_eng_dc_agroindustrias_del_chira_srl_sum10878332_cl', 
                        'medicion_promotora_inmobiliaria_industrial_de_piura_sac_cl', 
                        'medicion_eng_dc_negocios_del_sur_del_peru_cl' ]

list_of_table_not_in_files=[]
for files in list_of_tables_in_db:
    if files not in list_of_files:
        if files not in list_exclude_tables:
            list_of_table_not_in_files.append(files)
print(f'el archivo que no se ha enviado este mes es: {list_of_table_not_in_files}')