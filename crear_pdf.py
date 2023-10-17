# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:27:58 2021

@author: XZ5230
"""

import win32com.client

class print_excel_as_pdf():
    def __init__(self,path_excel,array_sheets,path_pdf):
        self.path_excel=path_excel
        self.array_sheets=array_sheets
        self.path_pdf=path_pdf
        
    def excel_to_pdf(self):
        func_1=win32com.client.Dispatch('Excel.Application')
        func_1.Visible = False
        func_1.DisplayAlerts =False
        path_excel_final=self.path_excel
        excel_open=func_1.Workbooks.Open(path_excel_final, 
                                         ReadOnly=True,
                                         UpdateLinks=False)      
        excel_open.Worksheets(self.array_sheets).Select()
        path_pdf_final=self.path_pdf
        excel_open.ActiveSheet.ExportAsFixedFormat(0,path_pdf_final)
        excel_open.Close()
        return 0
    

###############################################################################
        
year=2023
month='10'

###############################################################################



dict_array_sheets={1:'OSINERG',
                   2:'EDLN',
                   3:'ELSE',
                   4:'ENOSA',
                   5:'ELS',
                   6:'HDNA',
                   7:'LDS',
                   8:'ELU',
                   9:'SEAL',
                   10:'ELC',
                   11:'ENSA',
                   12:'ELPU',
                   13:'EDC',
                   14:'Coelvisac'}


path_excel_f='P:/EnerSur/Comercial/Facturacion/06_Precios_Tarifas/'
client='Precios_Enviados_a_Osinergmin'
file_excel='Precios_Contratos_Distribuidoras - 1'
path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'  
path_pdf_f=path_excel_f

for i in dict_array_sheets.keys():
    array_sheets=[i]
    file_pdf=dict_array_sheets[i]
    path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       
    q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
    q.excel_to_pdf()


'''
###############################################################################
##############################################################
##############################################################
####
####    COELVISAC
####
##############################################################
##############################################################
    
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='Coelvisac'
file_excel='Factura_COELVISAC-Lic-LP_Distriluz09'
array_sheets=[3,4,5]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf()
###############################################################################
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='Coelvisac'
file_excel='Factura_COELVISAC-Libre'
array_sheets=[3,4,5]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf()
###############################################################################
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='Coelvisac'
file_excel='Factura_COELVISAC-Libre-2'
array_sheets=[3,4,5]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf()
        
##############################################################
##############################################################
####
####    EDECANHETE
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='EDC'
file_excel='Factura_LDS_cantera-Lic-LP_ED-09'
array_sheets=[2,3,4]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf()   
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='EDC'
file_excel='Factura_LDS_cantera-Lic-LP_LD0111'
array_sheets=[2,3,4]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf()  
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='EDC'
file_excel='Factura_LDS_cantera-Lic-LP_LD0211'
array_sheets=[2,3,4,5]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf()  

##############################################################
##############################################################
####
####    ENEL DISTRIBUCION
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='EDLN'
file_excel='Factura_EDLN-Lic-LP_ED-2009-RESUMEN'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='EDLN'
file_excel='Factura_EDLN-Lic-LP_LDS1-2011-RESUMEN'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='EDLN'
file_excel='Factura_EDLN-Lic-LP-LDS2-2011-RESUMEN'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='EDLN'
file_excel='Factura_EDLN-LIB2018-RESUMEN'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

##############################################################
##############################################################
####
####    ELECTROCENTRO
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ELC'
file_excel='Factura_ELC-Libre-2'
array_sheets=[5,6,8]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ELC'
file_excel='Factura_ELC-Lic-LP_Distriluz-2009'
array_sheets=[2,3,4]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

##############################################################
##############################################################
####
####    ELECTROPUNO
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ELPU'
file_excel='Factura_ElectroPuno-Lic-LP_ED-2009'
array_sheets=[2,3,4]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

##############################################################
##############################################################
####
####    ELECTROSUR
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ELS'
file_excel='Factura_ElectroSur-Bilateral'
array_sheets=[2,3]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ELS'
file_excel='Factura_ElectroSur-Lic-LP_ED-2009'
array_sheets=[2,3,4,5,6]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

##############################################################
##############################################################
####
####    ELECTROSURESTE ELSE
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ELSE'
file_excel='Factura_ELSE-Anabi-RESUMEN'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ELSE'
file_excel='Factura_ELSE-Libre-RESUMEN'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ELSE'
file_excel='Factura_ELSE-Lic-LP_ED-2009-RESUMEN'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

##############################################################
##############################################################
####
####    ELECTRONOROESTE ENOSA
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ENOSA'
file_excel='Factura_ENOSA-Dist'
array_sheets=[3,4]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ENOSA'
file_excel='Factura_ENOSA-Dist-1'
array_sheets=[3,4]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ENOSA'
file_excel='Factura_ENOSA-stevia'
array_sheets=[3,4]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ENOSA'
file_excel='Factura_ENOSA-Lic-LP_Distriluz09'
array_sheets=[3,4,5]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ENOSA'
file_excel='Factura_ENOSA-Lic-LP_ED-2009'
array_sheets=[3,4,5,6,7,8,9]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

##############################################################
##############################################################
####
####    ELECTRONORTE ENSA
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ENSA'
file_excel='Factura_ENSA-Libre'
array_sheets=[3,4]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ENSA'
file_excel='Factura_ENSA-Libre-2'
array_sheets=[6,7]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='ENSA'
file_excel='Factura_ENSA-Lic-LP_Distriluz09'
array_sheets=[3,4,5]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

##############################################################
##############################################################
####
####    ELECTROUCAYALI EUCY
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='EUCY'
file_excel='Factura_ElectroUcayali-Bi2012'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='EUCY'
file_excel='Factura_ElectroUcayali-Bi2018'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf()

##############################################################
##############################################################
####
####    HIDRANDINA HDNA
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='HDNA'
file_excel='Factura_HDNA-Libre'
array_sheets=[3,4]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='HDNA'
file_excel='Factura_HDNA-Libre-2'
array_sheets=[6,7]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='HDNA'
file_excel='Factura_HDNA-Lic-LP_Distriluz09'
array_sheets=[3,4,5]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

##############################################################
##############################################################
####
####    LUZ DEL SUR LDS
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='LDS'
file_excel='Factura_LDS-Lic-LP_ED-2009-RESUMEN'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='LDS'
file_excel='Factura_LDS-Lic-LP_LDS1-2011-RESUMEN'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='LDS'
file_excel='Factura_LDS-Lic-LP_LDS2-2011-RESUMEN'
array_sheets=[1]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

##############################################################
##############################################################
####
####    SOCIEDAD ELECTRICA DEL SUR OESTE (SEAL)
####
##############################################################
##############################################################       
        
############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='SEAL'
file_excel='Factura_SEAL-Libre-RESUMEN'
array_sheets=[1,2]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='SEAL'
file_excel='Factura_SEAL-Lic-LP_ED-2009-RESUMEN'
array_sheets=[1,2]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 

############################################################################### 
path_excel_f='P:/EnerSur/Comercial/Facturacion/03_Factura_Regulados/'
client='SEAL'
file_excel='Factura_SEAL-Lic-LP_ED-2009-RESUMEN'
array_sheets=[1,2]
path_pdf_f=path_excel_f
file_pdf=file_excel

path_excel_final_1= path_excel_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_excel+'.xlsx'       
path_pdf_final_1= path_pdf_f+client+'/'+str(year)+'/'+str(month)+'_'+str(year)+'/'+str(month)+'_'+str(year)+'_'+file_pdf+'.pdf'       

q=print_excel_as_pdf(path_excel_final_1,array_sheets,path_pdf_final_1)
q.excel_to_pdf() 
'''