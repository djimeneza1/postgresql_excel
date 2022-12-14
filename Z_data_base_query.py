import pandas as pd
import numpy as np
import psycopg2
import datetime
from sqlalchemy import create_engine

class data_base_conection():


    def __init__(self,user,password,host,port,database):

        self.user=user

        self.password=password

        self.host=host

        self.port=port

        self.database=database


    def activate_connection(self):

        self.connection = psycopg2.connect( user=self.user ,

                                            password=self.password ,

                                            host=self.host ,

                                            port=self.port ,

                                            database=self.database )
        
        return self.connection
        

    def execute_query(self,query):

        try:

            connection = self.activate_connection()

            cursor = connection.cursor()

            query_f = query

            cursor.execute(query_f) 

            connection.commit()

        except (Exception, psycopg2.Error) as error :

            print ("Error while connecting to PostgreSQL", error)

        finally:

                if(connection):

                    cursor.close()

                    connection.close()

                    print("PostgreSQL connection is closed")

        return 0


    def dataframe_to_postgresql(self,dataframe_df,table_df):

        engine=create_engine(url="postgresql://{0}:{1}@{2}:{3}/{4}".format(

                self.user, self.password, self.host, self.port, self.database

                ))

        dataframe_df.to_sql(table_df, con=engine, if_exists='replace', index=False)

        return 0


    def execute_query_insert_many(self,table_name,records):

        try:

            connection = self.activate_connection()

            cursor = connection.cursor()
            
            sql_insert_query =  """ INSERT INTO public.{table} (kwh, kvar_i, kvar_c, kw, kwh_i, id_facturacion, periodo) 
                                    VALUES (%s,%s,%s,%s,%s,%s,%s) 
                                    ON CONFLICT (periodo) 
                                    DO NOTHING
                                    ;            
                                """

            result = cursor.executemany(sql_insert_query.format(table=table_name), records)

            connection.commit()

            print(cursor.rowcount, "Record inserted successfully")

        except (Exception, psycopg2.Error) as error :

            print ("Error while connecting to PostgreSQL", error)

        finally:

                if(connection):
                    
                    cursor.close()

                    connection.close()

                    print("PostgreSQL connection is closed")

        return 0




class delete_all_data_in_table(data_base_conection):


    def __init__(self,user,password,host,port,database):

        super().__init__(user,password,host,port,database)


    def delete_data_in_tables(self,table_name):

        try:

            connection = self.activate_connection()

            cursor = connection.cursor()

            query_f=f"DELETE FROM public.{table_name} WHERE id>=1;"

            cursor.execute(query_f) 

            connection.commit()

        except (Exception, psycopg2.Error) as error :

            print ("Error while connecting to PostgreSQL", error)

        finally:

                if(connection):

                    cursor.close()

                    connection.close()

                    print("PostgreSQL connection is closed")
        
        return 0

class show_all_tables_in_db(data_base_conection):


    def __init__(self,user,password,host,port,database):

        super().__init__(user,password,host,port,database)


    def tables_in_db(self):

        try:

            connection = self.activate_connection()

            cursor = connection.cursor()

            query_f=''' SELECT table_name 
                        FROM information_schema.tables 
                        WHERE table_schema='public' '''

            cursor.execute(query_f) 

            self.table_name = []
            for row in cursor:
                self.table_name.append(row)

            connection.commit()

        except (Exception, psycopg2.Error) as error :

            print ("Error while connecting to PostgreSQL", error)

        finally:

                if(connection):

                    cursor.close()

                    connection.close()

                    print("PostgreSQL connection is closed")
        
        return self.table_name