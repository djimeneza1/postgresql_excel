# direccion window para volumes docker \\wsl$\docker-desktop-data\data\docker\volumes
from Z_data_base_query import *
from Z_search_for_excelfiles import *


mes = '01'
anho='2023'

search_path_root='/config/workspace/root_inicio'
search_path_client='/'+'ENOSA'

search_path_year='/'+anho
search_path_month= '/'+mes+'_'+anho
search_final_path=search_path_root+search_path_client+search_path_year+search_path_month
search_final_path_data=search_final_path+'/'+'intefase_postgresql.xlsx'

tabla_consulta=pd.read_excel(search_final_path_data,sheet_name="consulta")

for j in range(np.shape(tabla_consulta)[0]):
    
    query_extract =f'''
        SELECT codigo_string
        FROM public.nombre_barra_facturacion
        WHERE id_tipo_cliente={tabla_consulta['id_tipo_cliente'][j]} AND
        id_cliente={tabla_consulta['id_cliente'][j]} AND
        id_contrato={tabla_consulta['id_contrato'][j]} AND
        id_licitacion={tabla_consulta['id_licitacion'][j]} AND
        id_oferta={tabla_consulta['id_oferta'][j]} AND	 
        id_mercado={tabla_consulta['id_mercado'][j]} AND	
        id_barra_referencia={tabla_consulta['id_barra_referencia'][j]} AND
        id_barra_suministro={tabla_consulta['id_barra_suministro'][j]}
        ;
    '''

    fecha_inicio_f=tabla_consulta['fecha_init'][j]
    fecha_final_f=tabla_consulta['fecha_last'][j]

    nombre_archivo_f = tabla_consulta['contrato'][j]+'_'+tabla_consulta['barra_suministro'][j]

    print("############################################")
    print("creando csv de la medicion "+nombre_archivo_f)
    print("############################################")

    mediciones=data_base_conection("admin",
                        "secret",
                        "172.25.0.1",
                        "5432",
                        "mediciones_cliente"
                        ).execute_query(query_extract,1)

    timestamps=create_timestamp_for_dataframe(int(anho),int(mes))

    array_timestamp=timestamps.create_timestamp_array()
    array_id=timestamps.create_range_arrays()
    array_kwh=timestamps.create_zero_arrays()
    array_kvar_i=timestamps.create_zero_arrays()
    array_kvar_c=timestamps.create_zero_arrays()
    array_kw=timestamps.create_zero_arrays()
    array_kwh_i=timestamps.create_zero_arrays()
    array_id_facturacion=timestamps.create_ones_arrays()

    data_dataframe_f = np.concatenate((array_id,
                                        array_kwh,
                                        array_kvar_i,
                                        array_kvar_c,
                                        array_kw,
                                        array_kwh_i,
                                        array_id_facturacion,
                                        array_timestamp),axis=1)

    df_final_med=pd.DataFrame(data_dataframe_f,columns=['id',
                                                        'kwh',
                                                        'kvar_i',
                                                        'kvar_c',
                                                        'kw',
                                                        'kwh_i',
                                                        'id_facturacion',
                                                        'periodo'])

    dict_medicion={}
    for i in range(np.shape(mediciones)[0]):
        print(mediciones[i][0])
        data_dataframe=postgresql_to_dataframe("admin",
                                                "secret",
                                                "172.25.0.1",
                                                "5432",
                                                "mediciones_cliente").postgresql_to_array(mediciones[i][0],
                                                                                        fecha_inicio_f,
                                                                                        fecha_final_f) # '2023-01-01 00:15','2023-02-01 00:00'      
        dict_medicion[mediciones[i][0]]=pd.DataFrame(data_dataframe , columns=['id',
                                                                                'kwh',
                                                                                'kvar_i',
                                                                                'kvar_c',
                                                                                'kw',
                                                                                'kwh_i',
                                                                                'id_facturacion',
                                                                                'periodo'])

        dict_medicion[mediciones[i][0]].to_csv(search_final_path+'/comprobacion_libres/'+mediciones[i][0]+'.csv') 
        
        if dict_medicion[mediciones[i][0]].empty:
            print(dict_medicion[mediciones[i][0]] + " esta vacio")
            print("\n")
            pass
        else:
            df_final_med['kwh']+=dict_medicion[mediciones[i][0]]['kwh'].astype('float')
            print(df_final_med['kwh'].sum())
            df_final_med['kvar_i']+=dict_medicion[mediciones[i][0]]['kvar_i'].astype('float')
            df_final_med['kvar_c']+=dict_medicion[mediciones[i][0]]['kvar_c'].astype('float')
            df_final_med['kw']+=dict_medicion[mediciones[i][0]]['kw'].astype('float')
            df_final_med['kwh_i']+=dict_medicion[mediciones[i][0]]['kwh_i'].astype('float')
            print("\n")
                
    df_final_med.to_csv(search_final_path+'/revision_libres/'+nombre_archivo_f+'.csv')                                                                          

