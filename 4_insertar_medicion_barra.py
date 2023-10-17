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

data_postgresql=pd.read_excel(search_final_path_data,sheet_name="nombre_data")
tabla_postgresql=pd.read_excel(search_final_path_data,sheet_name="tablas_postgres")
search_excel_name = data_postgresql['nombre_medicion_enviada'].isin(all_client_mesures)

par_postgresql=[]
for j in data_postgresql.index:
    par=[data_postgresql['nombre_medicion_enviada'][j],data_postgresql['encontrado_numero_postgres'][j],data_postgresql['mediciones_tabla_postgres'][j]]
    par_postgresql.append(par)


timestamps=create_timestamp_for_dataframe(int(anho),int(mes))

array_timestamp=timestamps.create_timestamp_array()
array_kvar_i=timestamps.create_zero_arrays()
array_kvar_c=timestamps.create_zero_arrays()
cantidad_datos=len(array_kvar_i)


for client,numero,tabla in par_postgresql:

    copy_path_root='/config/workspace/root_inicio'
    copy_path_client='/'+'ENOSA'

    copy_path_year='/'+anho
    copy_path_month= '/'+mes+'_'+anho+'/'+mes+anho+'_ENG_DC'

    copy_archive=client
    copy_sheet='Compra'
    copy_final_path=copy_path_root+copy_path_client+ copy_path_year+ copy_path_month+ '/'+copy_archive
    print(copy_final_path)

    kwh=copy_excel_data(copy_final_path,copy_archive,copy_sheet,5,3,cantidad_datos+4,3)
    kwh_copied = kwh.activate_workbook_to_copy()

    kw=copy_excel_data(copy_final_path,copy_archive,copy_sheet,5,2,cantidad_datos+4,2)
    kw_copied = kw.activate_workbook_to_copy()

    array_id_facturacion = np.dot(timestamps.create_ones_arrays(),numero)

    data_dataframe = np.concatenate((kwh_copied,
                                    array_kvar_i,
                                    array_kvar_c,
                                    kw_copied,
                                    kwh_copied,
                                    array_id_facturacion,
                                    array_timestamp),axis=1)

    dataframe_prueba=pd.DataFrame(data_dataframe ,columns=['kwh',
                                                            'kvar_i',
                                                            'kvar_c',
                                                            'kw',
                                                            'kwh_i',
                                                            'id_facturacion',
                                                            'periodo'])
    

    
    records_to_insert=[]

    for ro in dataframe_prueba.index: 

        tuple_prueba=()

        for col in dataframe_prueba.columns: 

            tuple_prueba+=(dataframe_prueba.loc[ro,col],)

        records_to_insert.append(tuple_prueba)


    data_base_conection("admin",
                    "secret",
                    "172.25.0.1",
                    "5432",
                    "mediciones_cliente"
                    ).execute_query_insert_many(tabla,'periodo',records_to_insert,'kwh',
                                                                                    'kvar_i',
                                                                                    'kvar_c',
                                                                                    'kw',
                                                                                    'kwh_i',
                                                                                    'id_facturacion',
                                                                                    'periodo')

    dataframe_prueba.to_csv(copy_path_root+
                        copy_path_client+ 

                        copy_path_year+ '/'+mes+'_'+anho+'/revision_libres/'+str(tabla)+'.csv')


print('############### tiempo ejecucion')
print(inicio_ejecucion)
final_ejecucion=datetime.datetime.now()
print(final_ejecucion-inicio_ejecucion)