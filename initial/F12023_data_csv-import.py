import pandas as pd 
import mysql.connector as sql
from sqlalchemy import create_engine
from sqlalchemy import URL

# CONNECT TO SQL SERVER
sql_connection = sql.connect(
    host = "localhost",
    user = "default",
    password = "default"
)

# CHECK IF DATABASE EXISTS
mycursor = sql_connection.cursor()
mycursor.execute("SHOW DATABASES")

print("-- Check 1 --")
for x in mycursor:
   print(f"{x} exists.")

# DROP POSSIBLE EXISTING DATABASE
mycursor = sql_connection.cursor()
mycursor.execute(
    "DROP DATABASE F12023_data"
    )

# CREATE NEW DATABASE
mycursor = sql_connection.cursor()
mycursor.execute(
    "CREATE DATABASE F12023_data"
    )

# CONNECT TO NEW DATABASE
db_connection = sql.connect(
    host = "localhost",
    user = "default",
    password = "default",
    database = "F12023_data"
)

# CHECK IF DATABASE EXISTS
mycursor = sql_connection.cursor()
mycursor.execute("SHOW DATABASES")

print("-- Check 2 --")
for x in mycursor:
   print(f"{x} exists.")

# IMPORT CSV FILE AS DATAFRAME
df = pd.read_csv(
    "initial\\csv\\Formula1_2023season_raceResults.csv",
    encoding = "latin1",
    sep = ",",
    )

# CHECK HEAD OF DATAFRAME
print(df.head())

# CONNECT TO NEW SQL DATABASE THROUGH SQL ALCHEMY
url_object = URL.create(
   "mysql+pymysql",
   host = "localhost",
   username = "default",
   password = "default",
   database = "F12023_data",
)
engine = create_engine(
   url_object
)

# EXPORT DATAFRAME AS SQL TABLE TO NEW DATABASE
df.to_sql(
   name = "f12023_raceresults",
   con = engine,
   if_exists = "replace",
   index = False,
   method = None
)