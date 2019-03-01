import pandas as pd

resources_folder = "/tmp/resources/" 
df = pd.read_csv(resources_folder + "imports-85.data", header = None)
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", 
"num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", 
"length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", 
"engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", 
"peak-rpm", "city-mpg", "highway-mpg", "price" ]

df.columns = headers
#Devuelve los tipos de datos en el dataframe
print(df.dtypes)
#Devuelve informacion estadistica sobre los datos
print(df.describe(include = 'all'))
df.to_csv(resources_folder + "export.csv")