import pandas as pd
import numpy as np

# IMPORT ORIGINAL DATAFRAME FROM CSV
df = pd.read_csv(
    "initial\\csv\\Formula1_2023season_raceResults.csv",
    encoding='latin1',
    sep = ",",
    )

# PIVOT RACE RESULTS
df_race = df.pivot(
  index = "Track", 
  columns = "Driver", 
  values = "Position"
  )
df_race = df_race.replace(
  "NC", 
  np.nan
  )

# PIVOT QUALIFICATION RESULTS
df_quali = df.pivot(
  index = "Track", 
  columns = "Driver", 
  values = "Starting Grid"
  )
df_quali = df_quali.apply(
  pd.to_numeric, 
  downcast = "signed", 
  errors = "coerce"
  )
df_quali = df_quali.replace(
  "NC", 
  np.nan
  )

# PIVOT POINTS REWARDED
df_points = df.pivot(
  index = "Track", 
  columns = "Driver", 
  values = "Points"
  )
df_points = df_points.apply(
  pd.to_numeric, 
  downcast = "signed", 
  errors = "coerce"
  )
df_points = df_points.replace(
  "NC", 
  np.nan
  )

# PIVOT CLASSIFICATION OR NOT
df_classification = df.pivot(
  index = "Track", 
  columns = "Driver", 
  values = "Time/Retired"
  )
def convert_to_boolean(value):
    if isinstance(value, str) and (value == "DNF" or value == "DNS" or value == "DNQ"):
        return False
    elif isinstance(value, bool):
        return value
    elif pd.isna(value):
        return np.nan
    else:
        return True
df_classification = df_classification.applymap(convert_to_boolean)

# PIVOT FASTEST LAP OR NOT
df_fastestlap = df.pivot(
  index = "Track", 
  columns = "Driver", 
  values = "Set Fastest Lap"
  )
def convert_to_boolean(value):
    if isinstance(value, str) and (value == "No"):
       return False
    elif pd.isna(value):
       return np.nan
    else:
       return True
df_fastestlap = df_fastestlap.applymap(convert_to_boolean)

# PIVOT FASTEST LAP TIME PER DRIVER
df_fastestlaptime = df.pivot(
    index = "Track", 
    columns = "Driver", 
    values = "Fastest Lap Time"
    )

# TEST PIVOT RESULTS AS DATAFRAMES
print(df_race)
print(df_quali)
print(df_points)
print(df_classification)
print(df_fastestlap)
print(df_fastestlaptime)