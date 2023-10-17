from Z_data_base_query import *

tabla_2 = [
'medicion_ENG_DC_American_Quality_Sum10910500',
'medicion_ENG_DC_CbC_Peruana1_Sum10491010',
'medicion_ENG_DC_CbC_Peruana2_Sum10491280',
'medicion_ENG_DC_Limagro_Sum10889686',
'medicion_ENG_DC_SunshineExport1_Sum11845200',
'medicion_ENG_DC_SunshineExport2_Sum10889004',
'medicion_ENG_DC_Grupo_Camposur_CL',
'medicion_ENG_DC_Negocios_Del_Sur_Del_Peru_CL',
'medicion_ENG_DC_Musterion_Sum15602345_CL',
'medicion_ENG_DC_Musterion_Sum15783189_CL',
'medicion_ENG_DC_Koricancha_Sum16079100_CL',
'medicion_ENG_DC_Agricola_El_Arenal_Sum12547590_CL',
'medicion_ENG_DC_Agroindustrias_Del_Chira_SRL_Sum10878332_CL',
'medicion_ENG_DC_Greenway_Sum16210081_CL',
'medicion_ENG_DC_Depositos_Sum12546000_CL',
'medicion_ENG_DC_Medlog_Paita_Sum17165991_CL',
'medicion_ENG_DC_Macromar_Sum17217668_CL',
'medicion_ENG_DC_Medlog_Paita_Sum16959447_CL',
'medicion_ENG_DC_Hielos_y_Servicios_Sum15526673_Piura_CL'
'''
'medicion_ENG_DC_Agricola_Del_Chira_La_Huaca_Sum12557756',
'medicion_ENG_DC_Complejo_Agroindustrial_Beta_Sum16289448',
'medicion_ENG_DC_SunshineExport3_Sum17230679',
'medicion_ENG_DC_Altamar_Sum12597027',
'medicion_ENG_DC_ASJ_Sum11105870',
'medicion_ENG_DC_ASJ_Sum15362436',
'medicion_ENG_DC_CONSORCIO_FEGURRI_STA_REGINA',
'medicion_ENG_DC_DonPacking_Sum10843050',
'medicion_ENG_DC_EMPAFRUIT',
'medicion_ENG_DC_EPS_GRAU_Sum10491118_PT',
'medicion_ENG_DC_EPS_GRAU_Sum12517643_EB1',
'medicion_ENG_DC_EPS_GRAU_Sum12517652_EB2',
'medicion_ENG_DC_EPS_GRAU_Sum12517661_PCAP',
'medicion_ENG_DC_HIELO_POLAR',
'medicion_ENG_DC_PERUPEZ',
'medicion_ENG_DC_PLAZA_CENTER_PAITA_Sum15540396',
'medicion_ENG_DC_PLAZA_CENTER_PIURA_Sum16907674',
'medicion_ENG_DC_PLAZA_CENTER_SULLANA_Sum15252775',
'medicion_ENG_DC_PLAZA_CENTER_TALARA3_Sum8704597',
'medicion_ENG_DC_PLAZA_CENTER_TUMBES_Sum17214405',
'medicion_ENG_DC_PROAGRO_Sum16303064',
'medicion_ENG_DC_SANTA_MONICA',
'medicion_ENG_DC_Turismo_Costa_del_Sol_Sum5037077',
'medicion_ENG_DC_UDEP',
'medicion_ENG_DC_EPS_GRAU_Sum5808079_Curumuy',
'medicion_ENG_DC_Seafrost',
'medicion_ENG_DC_Seafrost_Sum12316977',
'medicion_Promotora_Inmobiliaria_Industrial_De_Piura_SAC_CL',
'medicion_ENG_DC_EPS_GRAU_Sum5089681_SanMartin',
'medicion_ENG_DC_Hielos_y_Servicios_Sum6716374_Tumbes_CL',
'medicion_ENG_DC_Latimar_Sum6629386',
'medicion_ENG_DC_RAPEL',
'medicion_ENG_DC_Sucroalcolera',
'medicion_ENG_DC_HIELNORV_Sum10876015',
'medicion_ENG_DC_DOMINUS_Sum11210267_CL',
'medicion_ENG_DC_DOMINUS_Sum16079146_CL',
'medicion_ENG_DC_PACHAMAMA_Sum5883322_CL',
'medicion_ENG_DC_PLAZA_CENTER_TALARA',
'medicion_ENG_DC_PROAGRO_Sum17165258',
'medicion_ENG_DC_STEVIA',
'medicion_ENG_DC_Unimar_Sum12317105_Sum12317105'
'''
]

for i in tabla_2:
    print(f'''
    CREATE TABLE IF NOT EXISTS public.{i}
    (
        id serial NOT NULL,
        kwh numeric,
        kvar_i numeric,
        kvar_c numeric,
        kw numeric,
        kwh_i numeric,
        id_facturacion integer,
        periodo timestamp without time zone,
        CONSTRAINT {i}_pkey PRIMARY KEY (id),
        CONSTRAINT facturacion_medicion_fkey FOREIGN KEY (id_facturacion)
            REFERENCES public.nombre_barra_facturacion (id) MATCH SIMPLE
            ON UPDATE CASCADE
            ON DELETE CASCADE
            NOT VALID
    )

    TABLESPACE pg_default;
    ''')



'''
CREATE TABLE IF NOT EXISTS public.medicion_eng_dc_altamar_sum12597027
(
    id integer NOT NULL DEFAULT nextval('medicion_eng_dc_altamar_sum12597027_id_seq'::regclass),
    kwh numeric,
    kvar_i numeric,
    kvar_c numeric,
    kw numeric,
    kwh_i numeric,
    id_facturacion integer,
    periodo timestamp without time zone,
    CONSTRAINT medicion_eng_dc_altamar_sum12597027_pkey PRIMARY KEY (id),
    CONSTRAINT medicion_eng_dc_altamar_sum12597027_uq_per UNIQUE (periodo),
    CONSTRAINT facturacion_medicion_fkey FOREIGN KEY (id_facturacion)
        REFERENCES public.nombre_barra_facturacion (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.medicion_eng_dc_altamar_sum12597027
    OWNER to admin;

'''

data_base_conection("admin",
                    "secret",
                    "172.25.0.1",
                    "5432",
                    "mediciones_cliente"
                    ).tables_in_db()