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

tabla_nombre_barra_facturacion=pd.read_excel(search_final_path_data,sheet_name="nombre_barra_facturacion")

records_to_insert=[]

for ro in tabla_nombre_barra_facturacion.index: 

    tuple_prueba=()

    for col in tabla_nombre_barra_facturacion.columns: 
        
        if isinstance(tabla_nombre_barra_facturacion.loc[ro,col],str):
            tuple_prueba+=(str(tabla_nombre_barra_facturacion.loc[ro,col]),)
        else:
            tuple_prueba+=(int(tabla_nombre_barra_facturacion.loc[ro,col].item()),)
            
    records_to_insert.append(tuple_prueba)

data_base_conection("admin",
                    "secret",
                    "172.25.0.1",
                    "5432",
                    "mediciones_cliente"
                    ).execute_query_insert_many('nombre_barra_facturacion',
                                                'id',
                                                records_to_insert,
                                                'id',
                                                'nombre',
                                                'codigo_int',
                                                'codigo_string',
                                                'id_tipo_cliente',
                                                'id_cliente',
                                                'id_contrato',
                                                'id_licitacion',
                                                'id_oferta', 
                                                'id_mercado', 
                                                'id_barra_referencia', 
                                                'id_barra_suministro')