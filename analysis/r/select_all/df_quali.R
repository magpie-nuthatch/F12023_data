Sys.setenv(timeout = 360)
options(scipen = 999)

setwd("~/T99/F12023_data")
df <- read.csv(
  "pivot\\output\\df_quali.csv", 
  sep = ";"
  )

df