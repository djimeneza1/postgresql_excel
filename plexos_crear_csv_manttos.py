import pkg_copy_paste
import pandas as pd
import numpy as np
import datetime
import ast

inicio = pkg_copy_paste.time.time()
#data_columnas=['unit1','unit2','unit3']


#read_data_columnas=pd.read_excel('./manttos_final.xlsx',sheet_name='bd_hidros')

#read_data_columnas=read_data_columnas.drop_duplicates(subset=['central_plexos'],keep='last')

#read_data_columnas=read_data_columnas.dropna(subset=['central_plexos'])

#data_columnas=np.array(read_data_columnas['central_plexos'].to_list())
'''
data_columnas= ['00057_ch_01018_pariac'
,'00260_ch_00055_cahua'
,'00261_ch_00018_callahuanca'
,'00264_ch_00061_carhuaquero'
,'00267_ch_00073_canhon_del_pato'
,'00269_ch_00100_gallito_ciego'
,'00270_ch_00026_huampani'
,'00272_ch_00022_huinco'
,'00276_ch_00039_malpaso'
,'00277_ch_00001_mantaro'
,'00280_ch_00028_matucana'
,'00282_ch_00030_moyopampa'
,'00283_ch_00043_oroya'
,'00285_ch_00046_pachachaca'
,'00286_ch_00008_restitucion'
,'00291_ch_00050_yaupi'
,'00978_ch_00108_yanango'
,'01191_ch_00109_chimay'
,'01195_ch_00111_charcani_1'
,'01196_ch_00113_charcani_2'
,'01197_ch_00116_charcani_3'
,'01198_ch_00118_charcani_4'
,'01199_ch_00121_charcani_5'
,'01200_ch_00188_charcani_6'
,'01201_ch_00124_aricota_1'
,'01203_ch_00126_machupicchu'
,'01206_ch_00190_san_gaban_2'
,'10609_ch_00193_huanchor'
,'11116_ch_00199_yuncan'
,'11842_ch_00205_canha_brava'
,'11877_ch_11878_santacruz_1'
,'12193_ch_12194_poechos_2'
,'12201_ch_12202_la_joya'
,'12600_ch_12601_el_platanal'
,'12652_ch_12650_santacruz_2'
,'12722_ch_12760_roncador'
,'13368_ch_13411_imperial'
,'13513_ch_13514_yanapampa'
,'13574_ch_13575_las_pizarras'
,'14005_ch_14006_huanza'
,'14844_ch_14845_santa_teresa'
,'14909_ch_00204_carhuaquero_4'
,'14964_ch_14965_cheves'
,'14970_ch_14971_chaglla'
,'15210_ch_15211_cerro_del_aguila'
,'17492_ch_17493_maranhon'
,'17551_ch_00055_yarucaya'
,'18186_ch_18187_la_virgen'
,'18949_ch_18952_angel_1'
,'18950_ch_18955_angel_2'
,'18951_ch_18956_angel_3'
]


'''


data_columnas= ['00258_ct_00209_aguaytia_tg1'
,'00258_ct_00210_aguaytia_tg2'
,'00275_ct_00271_malacas2_tg4'
,'00289_ct_00221_santarosa1_uti5d'
,'00289_ct_00223_santarosa1_td7h'
,'00289_ct_00240_santarosa1_uti6d'
,'00289_ct_00278_santarosa1_tg7h'
,'00289_ct_00279_santarosa1_tg7'
,'00289_ct_00280_santarosa1_uti5g'
,'00289_ct_00281_santarosa1_uti6g'
,'00290_ct_00205_ventanilla_td3'
,'00290_ct_00207_ventanilla_td4'
,'00290_ct_00274_ventanilla_tg3'
,'00290_ct_00275_ventanilla_tg4'
,'00290_ct_00286_ventanilla_tg3tv'
,'00290_ct_00287_ventanilla_tg4tv'
,'00290_ct_00288_ventanilla_tg3tg4tv'
,'00290_ct_00289_ventanilla_tg3tvfd'
,'00290_ct_00290_ventanilla_tg4tvfd'
,'00290_ct_00291_ventanilla_tg3tg4tvfd'
,'00987_ct_00236_san_nicolas_tv1'
,'00987_ct_00237_san_nicolas_tv2'
,'00987_ct_00238_san_nicolas_tv3'
,'00987_ct_00272_san_nicolas_td'
,'01066_ct_00303_santarosa2_tg8'
,'01205_ct_00241_chilina_sulz'
,'01205_ct_00355_chilina_td'
,'01214_ct_00346_mollendo_td'
,'11513_ct_00292_chilca1_tg1'
,'11513_ct_00295_chilca1_tg2'
,'11513_ct_00302_chilca1_tg3'
,'11513_ct_00327_chilca1_tg1tv'
,'11513_ct_00328_chilca1_tg2tv'
,'11513_ct_00329_chilca1_tg3tv'
,'11513_ct_00330_chilca1_tg1tg2tv'
,'11513_ct_00331_chilca1_tg2tg3tv'
,'11513_ct_00332_chilca1_tg1tg3tv'
,'11513_ct_00333_chilca1_tg1tg2tg3tv'
,'11571_ct_00296_kallpa_tg1'
,'11571_ct_00305_kallpa_tg2'
,'11571_ct_00306_kallpa_tg3'
,'11571_ct_00320_kallpa_tg1tv'
,'11571_ct_00321_kallpa_tg2tv'
,'11571_ct_00322_kallpa_tg3tv'
,'11571_ct_00323_kallpa_tg1tg2tv'
,'11571_ct_00324_kallpa_tg2tg3tv'
,'11571_ct_00325_kallpa_tg1tg3tv'
,'11571_ct_00326_kallpa_tg1tgtg3tv'
,'11883_ct_00298_oquendo_tg1'
,'11883_ct_03418_oquendo_tv1'
,'11883_ct_03424_oquendoi_tg1tv'
,'12720_ct_00304_las_flores_tg1'
,'12720_ct_03375_las_flores_tg1tv'
,'12781_ct_00312_independencia_tg'
,'12815_ct_00309_paramonga_tg'
,'13417_ct_00317_maple_tv'
,'13549_ct_00339_rf_ilo_td1'
,'13549_ct_00340_rf_ilo_td2'
,'13549_ct_00341_rf_ilo_td3'
,'13601_ct_00344_fenix_tg12'
,'13601_ct_00345_fenix_tg12tv'
,'13601_ct_00347_fenix_tg11'
,'13601_ct_00348_fenix_tg11tv'
,'13601_ct_00349_fenix_tg11tg12tv'
,'13601_ct_00553_fenix_td11tv'
,'13601_ct_00554_fenix_td11'
,'13601_ct_00555_fenix_td12tv'
,'13601_ct_00556_fenix_td12'
,'13601_ct_00605_fenix_tg11tg12tv'
,'13656_ct_00318_olleros_tg1tv'
,'13656_ct_00343_olleros_tg1'
,'14908_ct_00338_rf_talara_td5'
,'14908_ct_00543_rf_talara_tg5'
,'14927_ct_00353_rf_eten_td1'
,'14927_ct_00354_rf_eten_td2'
,'15107_ct_00843_recka_td1'
,'15214_ct_00358_puerto_bravo_td1'
,'15214_ct_00359_puerto_bravo_td2'
,'15214_ct_00360_puerto_bravo_td3'
,'15214_ct_00361_puerto_bravo_td4'
,'15785_ct_00606_chilca2_tg41'
,'15785_ct_00919_chilca2_tg41tv'
,'16290_ct_00372_rf_puerto_maldonado_td'
,'16291_ct_00373_rf_pucallpa_td'
,'16327_ct_00611_nepi_td41'
,'16327_ct_00612_nepi_td42'
,'16327_ct_00613_nepi_td43'
,'16926_ct_00672_malacas_tg6'
,'20510_ct_00573_canha_brava_tv1'
,'20510_ct_00574_canha_brava_tv2'
,'20510_ct_00575_canha_brava_tv1tv2'
]

#print(data_columnas)

dataframe_manttos=pd.read_csv('./manto_thermal.csv') 

prueba4=pkg_copy_paste.ModifyDataFrameMultiYears(2023,2024,48,data_columnas,0,dataframe_manttos)

#dataframe_final=prueba4.funcmultiyear()

#dataframe_final.to_csv('./plantilla-data-final.csv')

#df_calcdifdates=prueba4.funCalcDifDates()

#df_calcdifdates.to_csv('./plantilla-calcdifdate-final.csv')

dataframe_fin_mod=prueba4.funChangeDataInDataframeColumn()

dataframe_fin_mod.to_csv('./plexos_mantto_hidros.csv')

final=pkg_copy_paste.time.time()
   
print(f'ejecucion finalizada de copy and paste en {final-inicio} segundos')
