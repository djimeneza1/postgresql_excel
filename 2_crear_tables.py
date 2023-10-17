from Z_data_base_query import *

#######################################################

tabla=[

'medicion_eng_dc_american_quality_sum10910500',
'medicion_eng_dc_cbc_peruana1_sum10491010',
'medicion_eng_dc_cbc_peruana2_sum10491280',
'medicion_eng_dc_limagro_sum10889686',
'medicion_eng_dc_sunshineexport1_sum11845200',
'medicion_eng_dc_sunshineexport2_sum10889004',
'medicion_eng_dc_grupo_camposur_cl',
'medicion_eng_dc_negocios_del_sur_del_peru_cl',
'medicion_eng_dc_musterion_sum15602345_cl',
'medicion_eng_dc_musterion_sum15783189_cl',
'medicion_eng_dc_koricancha_sum16079100_cl',
'medicion_eng_dc_agricola_el_arenal_sum12547590_cl',
'medicion_eng_dc_agroindustrias_del_chira_srl_sum10878332_cl',
'medicion_eng_dc_greenway_sum16210081_cl',
'medicion_eng_dc_depositos_sum12546000_cl',
'medicion_eng_dc_medlog_paita_sum17165991_cl',
'medicion_eng_dc_macromar_sum17217668_cl',
'medicion_eng_dc_medlog_paita_sum16959447_cl',
'medicion_eng_dc_hielos_y_servicios_sum15526673_piura_cl',
'medicion_eng_dc_agricola_del_chira_la_huaca_sum12557756',
'medicion_eng_dc_complejo_agroindustrial_beta_sum16289448',
'medicion_eng_dc_sunshineexport3_sum17230679',
'medicion_eng_dc_altamar_sum12597027',
'medicion_eng_dc_asj_sum11105870',
'medicion_eng_dc_asj_sum15362436',
'medicion_eng_dc_consorcio_fegurri_sta_regina',
'medicion_eng_dc_donpacking_sum10843050',
'medicion_eng_dc_empafruit',
'medicion_eng_dc_eps_grau_sum10491118_pt',
'medicion_eng_dc_eps_grau_sum12517643_eb1',
'medicion_eng_dc_eps_grau_sum12517652_eb2',
'medicion_eng_dc_eps_grau_sum12517661_pcap',
'medicion_eng_dc_hielo_polar',
'medicion_eng_dc_perupez',
'medicion_eng_dc_plaza_center_paita_sum15540396',
'medicion_eng_dc_plaza_center_piura_sum16907674',
'medicion_eng_dc_plaza_center_sullana_sum15252775',
'medicion_eng_dc_plaza_center_talara3_sum8704597',
'medicion_eng_dc_plaza_center_tumbes_sum17214405',
'medicion_eng_dc_proagro_sum16303064',
'medicion_eng_dc_santa_monica',
'medicion_eng_dc_turismo_costa_del_sol_sum5037077',
'medicion_eng_dc_udep',
'medicion_eng_dc_eps_grau_sum5808079_curumuy',
'medicion_eng_dc_seafrost',
'medicion_eng_dc_seafrost_sum12316977',
'medicion_promotora_inmobiliaria_industrial_de_piura_sac_cl',
'medicion_eng_dc_eps_grau_sum5089681_sanmartin',
'medicion_eng_dc_hielos_y_servicios_sum6716374_tumbes_cl',
'medicion_eng_dc_latimar_sum6629386',
'medicion_eng_dc_rapel',
'medicion_eng_dc_sucroalcolera',
'medicion_eng_dc_hielnorv_sum10876015',
'medicion_eng_dc_dominus_sum11210267_cl',
'medicion_eng_dc_dominus_sum16079146_cl',
'medicion_eng_dc_pachamama_sum5883322_cl',
'medicion_eng_dc_plaza_center_talara',
'medicion_eng_dc_proagro_sum17165258',
'medicion_eng_dc_stevia',
'medicion_eng_dc_unimar_sum12317105_sum12317105',
'medicion_eng_dc_fabrica_hielofish_sum15289354',
'medicion_eng_dc_agropesca_del_peru_sum17815058',
'medicion_eng_dc_limonespiuranos_sum10888885',
'medicion_eng_dc_agropesca_del_peru_sum10490980',
'medicion_eng_dc_bahia_norte_sum6671521_cl',
'medicion_eng_dc_bahia_norte_sum8248360_cl',
'medicion_eng_dc_isla_bella_sum6711369_cl',
'medicion_eng_dc_consorcio_carsol_sum16653302_piura_cl'


]

show_all_tables_in_db("admin",
                    "secret",
                    "172.25.0.1",
                    "5432",
                    "mediciones_cliente"
                    ).tables_in_db()

for i in tabla:
    query=f'''
    CREATE TABLE IF NOT EXISTS public.{i}
    (
        id SERIAL NOT NULL,
        kwh numeric,
        kvar_i numeric,
        kvar_c numeric,
        kw numeric,
        kwh_i numeric,
        id_facturacion integer,
        periodo timestamp without time zone,
        CONSTRAINT {i}_pkey PRIMARY KEY (id),
        CONSTRAINT {i}_uq_per UNIQUE (periodo),
        CONSTRAINT facturacion_medicion_fkey FOREIGN KEY (id_facturacion)
            REFERENCES public.nombre_barra_facturacion (id) MATCH SIMPLE
            ON UPDATE CASCADE
            ON DELETE CASCADE
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public.{i}
        OWNER to admin;
    '''

    data_base_conection("admin",
                    "secret",
                    "172.25.0.1",
                    "5432",
                    "mediciones_cliente"
                    ).execute_query(query,0)