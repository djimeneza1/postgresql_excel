import numpy as np
from Z_data_base_query import *
from Z_search_for_excelfiles import *

mes = '01'
anho='2023'

search_path_root='/config/workspace/root_inicio'
search_path_client='/'+'ENOSA'

search_path_year='/'+anho
search_path_month= '/'+mes+'_'+anho
search_final_path=search_path_root+search_path_client+search_path_year+search_path_month
search_final_path_data=search_final_path+'/'


query_extract ='''
    SELECT codigo_string
	FROM public.nombre_barra_facturacion
    WHERE id_tipo_cliente=1 AND
    id_cliente=1 AND
    id_contrato=1 AND
    id_licitacion=15 AND
    id_oferta=41 AND	 
    id_mercado=3 AND	
    id_barra_referencia=1 AND
    id_barra_suministro=1
    ;
'''

'''
id_tipo_cliente:1
id_cliente:1
id_contrato:1
id_licitacion:1,15,19	
id_oferta:8,39,41	
id_mercado:3	
id_barra_referencia:1,3	
id_barra_suministro:1,2,4

id_tipo_cliente	id_cliente	id_contrato	id_licitacion	id_oferta	id_mercado	id_barra_referencia	id_barra_suministro

regulado	    ENOSA	    BILATERAL	BI0119	        DIST	    LIBR	    PIURA220	        PiuraOeste60
1	            1	        1	        15	            41	        3	        1	                1


regulado	    ENOSA	    BILATERAL	BI0119	        DIST	    LIBR	    PIURA220	        PiuraOeste10
1	            1	        1	        15	            41	        3	        1	                2


regulado	    ENOSA	    BILATERAL	BI0119	        DIST	    LIBR	    ZORRITOS220	        NuevaZorritos60
1	            1	        1	        15	            41	        3	        3	                4

'''


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
                                                                                    '2023-01-01 00:15',
                                                                                    '2023-02-01 00:00')
    
    dict_medicion[mediciones[i][0]]=pd.DataFrame(data_dataframe , columns=['id',
                                                                            'kwh',
                                                                            'kvar_i',
                                                                            'kvar_c',
                                                                            'kw',
                                                                            'kwh_i',
                                                                            'id_facturacion',
                                                                            'periodo'])
    
    if dict_medicion[mediciones[i][0]].empty:
        pass
    else:
        df_final_med['kwh']+=dict_medicion[mediciones[i][0]]['kwh'].astype('float')
        df_final_med['kvar_i']+=dict_medicion[mediciones[i][0]]['kvar_i'].astype('float')
        df_final_med['kvar_c']+=dict_medicion[mediciones[i][0]]['kvar_c'].astype('float')
        df_final_med['kw']+=dict_medicion[mediciones[i][0]]['kw'].astype('float')
        df_final_med['kwh_i']+=dict_medicion[mediciones[i][0]]['kwh_i'].astype('float')
            
df_final_med.to_csv(search_final_path+'/revision_libres/'+'Energia_Libres_1_piura60kv'+'.csv')                                                                      