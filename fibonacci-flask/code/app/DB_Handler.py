# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 19:17:29 2020

@author: sa250067
"""
import mysql.connector as mysql

class DB_Handler:
      
   
    def get_db_connection():
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD = 'root'
        MYSQL_DB = 'test'
        
        db = mysql.connect(host = "db",  user = "root", passwd = "root",   database = "fibonacci")
        return db    

    def add_to_db(ts,ip,url,status):
        mysql = DB_Handler.get_db_connection()
        cur = mysql.cursor()
        sql = "INSERT INTO request_log VALUES (%s,%s,%s,%s)"
        values = (ts,ip,url,status)
        try:
            cur.execute(sql,values)
            mysql.commit()
            cur.close()
            return None
        except Exception as e:
            cur.close()
            return str(e)
