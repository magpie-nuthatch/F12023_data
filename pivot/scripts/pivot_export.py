import pandas as pd
from initial_pivot import df_race, df_quali, df_points, df_classification, df_fastestlap, df_fastestlaptime

# EXPORTING PIVOTED DATAFRAMES AS INDIVIDUAL CSV FILES 

df_race.to_csv("pivot\\output\\df_race.csv",
               sep = ";")

df_quali.to_csv("pivot\\output\\df_quali.csv",
                sep = ";")

df_points.to_csv("pivot\\output\\df_points.csv",
                 sep = ";")

df_classification.to_csv("pivot\\output\\df_classification.csv",
                         sep = ";")

df_fastestlap.to_csv("pivot\\output\\df_fastestlap.csv",
                     sep = ";")

df_fastestlaptime.to_csv("pivot\\output\\df_fastestlaptime.csv",
                         sep = ";")