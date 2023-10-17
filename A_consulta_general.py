from Z_data_base_query import *
from Z_search_for_excelfiles import *

import matplotlib.pyplot as plt

query = ''' INSERT INTO public.nombre_barra_facturacion(id,nombre, codigo_int, codigo_string, id_tipo_cliente, id_cliente, id_contrato, id_licitacion, id_oferta, id_mercado, id_barra_referencia, id_barra_suministro) 
VALUES (60,'Unimar_Sum12317105_Sum12317105',159,'ENG_DC_Unimar_Sum12317105_Sum12317105',1,1,1,15,8,3,1,1); '''

'''
55,'DOMINUS_Sum16079146_CL',154,'ENG_DC_DOMINUS_Sum16079146_CL',1,1,1,19,8,3,1,1
56,'PACHAMAMA_Sum5883322_CL',155,'ENG_DC_PACHAMAMA_Sum5883322_CL',1,1,1,19,8,3,1,1
57,'PLAZA_CENTER_TALARA',156,'ENG_DC_PLAZA_CENTER_TALARA',1,1,1,15,41,3,1,1
58,'PROAGRO_Sum17165258',157,'ENG_DC_PROAGRO_Sum1716525',1,1,1,15,41,3,1,1
59,'STEVIA',158,'ENG_DC_STEVIA',1,1,1,1,39,3,1,1
60,'Unimar_Sum12317105_Sum12317105',159,'ENG_DC_Unimar_Sum12317105_Sum12317105',1,1,1,15,8,3,1,1
'''

'''
data_base_conection("admin",
                    "secret",
                    "172.25.0.1",
                    "5432",
                    "mediciones_cliente"
                    ).execute_query(query)
'''

query_extract ='''
    SELECT id, kwh, kvar_i, kvar_c, kw, kwh_i, id_facturacion, periodo
	FROM public.medicion_eng_dc_eps_grau_sum10491118_pt
    WHERE periodo >= '2022-07-01 00:15'
    AND periodo <= '2022-07-01 00:15';' 
'''

m=postgresql_to_dataframe("admin",
                    "secret",
                    "172.25.0.1",
                    "5432",
                    "mediciones_cliente"
                    ).postgresql_to_array('medicion_eng_dc_eps_grau_sum10491118_pt','2022-08-01 00:16','2022-08-01 05:43')

columns = ['id', 'kwh', 'kvar_i',' kvar_c', 'kw', 'kwh_i', 'id_facturacion', 'periodo']
dataframe=pd.DataFrame(m,columns=columns)
print(dataframe)

x=np.array(dataframe['periodo'])
y=np.array(dataframe['kw'])

plt.plot(x,y)
plt.savefig("medicion_eng_dc_eps_grau_sum10491118_pt.png")