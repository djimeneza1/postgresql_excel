
def print_argumentos(*args):
    m=''
    n=''
    for a in args:
        m+=a+','
        n+='%s'+','
    return print(m),print(n)

#print_argumentos('kwh', 'kvar_i', 'kvar_c', 'kw', 'kwh_i', 'id_facturacion', 'periodo')




def execute_query_insert_many_final(table_name,conflict,records,*args):

    argumentos=''
    valores=''
    for a in args:
        argumentos+=a+','
        valores+='%s'+','
    
    argumentos=argumentos[:-1]
    valores=valores[:-1]

    sql_insert_query =  """ INSERT INTO public.{table} ({arguments}) 
                            VALUES ({fix_values}) 
                            ON CONFLICT ({on_conflict}) 
                            DO NOTHING
                                ;            
                        """.format(table=table_name,arguments=argumentos,fix_values=valores,on_conflict=conflict)
    
    return print(sql_insert_query)


execute_query_insert_many_final('daniel_tabla','periodo','records','kwh', 'kvar_i', 'kvar_c', 'kw', 'kwh_i', 'id_facturacion', 'periodo')


