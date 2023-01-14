import pandas as pd
import sqlite3

class Replacement:
    def __init__(self,sql,csv):
        self.sql = sql 
        self.csv = csv
    def sql_to_csv(self):
        con = sqlite3.connect(self.sql)
        df = pd.read_sql_query('SELECT * from fault_lines',con)
        df.to_csv('all_fault_line.csv')
    def csv_to_sql(self):
        conn = sqlite3.connect("list_volcanos.db")
        df = pd.read_csv(self.csv)
        df.to_sql("table_name",conn,  if_exists='replace')

csv = 'list_volcano.csv'
sql = 'all_fault_line.db'
datasets = Replacement(sql,csv)
datasets.sql_to_csv()
datasets.csv_to_sql()