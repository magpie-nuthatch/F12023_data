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
   database = "F12023_data",
)
engine = create_engine(
   url_object
)

## FOR RACE RESULTS
# IMPORT CSV FILE AS DATAFRAME
df_race = pd.read_csv(
   "pivot\\output\\df_race.csv",
   sep = ";",
    )

# EXPORT DATAFRAME AS SQL TABLE TO NEW DATABASE
df_race.to_sql(
   name = "f12023_raceresults_race",
   con = engine,
   if_exists = "replace",
   index = False,
   method = None
)

## FOR QUALIFICATION RESULTS
# IMPORT CSV FILE AS DATAFRAME
df_quali = pd.read_csv(
   "pivot\\output\\df_quali.csv",
   sep = ";",
    )

# EXPORT DATAFRAME AS SQL TABLE TO NEW DATABASE
df_quali.to_sql(
   name = "f12023_raceresults_quali",
   con = engine,
   if_exists = "replace",
   index = False,
   method = None
)

## FOR POINTS REWARDED
# IMPORT CSV FILE AS DATAFRAME
df_points = pd.read_csv(
   "pivot\\output\\df_points.csv",
   sep = ";",
    )

# EXPORT DATAFRAME AS SQL TABLE TO NEW DATABASE
df_points.to_sql(
   name = "f12023_raceresults_points",
   con = engine,
   if_exists = "replace",
   index = False,
   method = None
)

## FOR CLASSIFICATION OR NOT
# IMPORT CSV FILE AS DATAFRAME
df_classification = pd.read_csv(
   "pivot\\output\\df_classification.csv",
   sep = ";",
    )

# EXPORT DATAFRAME AS SQL TABLE TO NEW DATABASE
df_classification.to_sql(
   name = "f12023_raceresults_classification",
   con = engine,
   if_exists = "replace",
   index = False,
   method = None
)

## FOR FASTEST LAP OR NOT
# IMPORT CSV FILE AS DATAFRAME
df_fastestlap = pd.read_csv(
   "pivot\\output\\df_fastestlap.csv",
   sep = ";",
    )

# EXPORT DATAFRAME AS SQL TABLE TO NEW DATABASE
df_fastestlap.to_sql(
   name = "f12023_raceresults_fastestlap",
   con = engine,
   if_exists = "replace",
   index = False,
   method = None
)

## FOR FASTEST LAPTIME PER DRIVER
# IMPORT CSV FILE AS DATAFRAME
df_fastestlaptime = pd.read_csv(
   "pivot\\output\\df_fastestlaptime.csv",
   sep = ";",
    )

# EXPORT DATAFRAME AS SQL TABLE TO NEW DATABASE
df_fastestlaptime.to_sql(
   name = "f12023_raceresults_fastestlaptime",
   con = engine,
   if_exists = "replace",
   index = False,
   method = None
)