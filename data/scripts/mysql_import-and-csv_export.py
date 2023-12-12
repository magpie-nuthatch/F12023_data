import pandas as pd
import mysql.connector as sql
from sqlalchemy import create_engine
from sqlalchemy import URL

# CONNECT TO NEW SQL DATABASE THROUGH SQL ALCHEMY
url_object = URL.create(
   "mysql+pymysql",
   host = "localhost",
   username = "default",
   password = "default",
   database = "f12023_data",
   )

engine = create_engine(
   url_object
   )

# RACE
df_race = pd.read_sql("SELECT * FROM f12023_raceresults_race", 
                 con = engine
                 )

df_race.to_csv("data\\csv\\df_race.csv",
               sep = ";"
               )

# QUALI
df_quali = pd.read_sql("SELECT * FROM f12023_raceresults_quali", 
                 con = engine
                 )

df_quali.to_csv("data\\csv\\df_quali.csv",
               sep = ";"
               )

# POINTS
df_points = pd.read_sql("SELECT * FROM f12023_raceresults_points", 
                 con = engine
                 )

df_points.to_csv("data\\csv\\df_points.csv",
               sep = ";"
               )

# CLASSIFICATION
df_classification = pd.read_sql("SELECT * FROM f12023_raceresults_classification", 
                 con = engine
                 )

df_classification.to_csv("data\\csv\\df_classification.csv",
               sep = ";"
               )
# FASTEST LAP
df_fastestlap = pd.read_sql("SELECT * FROM f12023_raceresults_fastestlap", 
                 con = engine
                 )

df_fastestlap.to_csv("data\\csv\\df_fastestlap.csv",
               sep = ";"
               )

# FASTEST LAP TIME
df_fastestlaptime = pd.read_sql("SELECT * FROM f12023_raceresults_fastestlaptime", 
                 con = engine
                 )

df_fastestlaptime.to_csv("data\\csv\\df_fastestlaptime.csv",
               sep = ";"
               )