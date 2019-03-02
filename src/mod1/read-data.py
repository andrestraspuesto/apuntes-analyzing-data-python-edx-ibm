import pandas as pd
import numpy as np

#https://pandas.pydata.org/pandas-docs/stable/reference/api/

def view_data_info(df):
    #Devuelve los tipos de datos en el dataframe
    print(df.dtypes)
    #Devuelve informacion estadistica sobre los datos
    print(df.describe(include = 'all'))

def get_clean_cars_df(df):
    #Eliminacion de registros sin precio, modificando directamente el dataset
    df.replace({'price': {'?': np.nan}}, regex=False,inplace=True)
    df.dropna(subset = ['price'], axis = 0, inplace = True)

    #Sustitucion de normalized-losses si no tiene valor por la media del conjunto
    media = df.dropna(subset = ['normalized-losses'], axis = 0).mean()
    df['normalized-losses'].replace(to_replace = np.nan, value = media, inplace = True)

    #normalizacion mediante escalado
    df['city-mpg'] = (df['city-mpg']- df['city-mpg'].min())/(df['city-mpg'].max() - df['city-mpg'].min())
    #puntuacion estandar
    df['compression-ratio'] = (df['compression-ratio']- df['compression-ratio'].mean())/(df['compression-ratio'].std())
    df["price"] = df["price"].astype("int")
    #Clasificacion 
    bins  = np.linspace(min(df["price"]), max(df["price"]), 4)
    group_names = ["low", "medium", "high"]
    df["price-binned"] = pd.cut(df["price"], bins, labels = group_names, include_lowest = True)
    #Añade columnas con transformacion de categoria a dato cuantitativo
    df = pd.concat([df, pd.get_dummies(df['fuel-type'])], axis = 1) 
    return df


resources_folder = "/tmp/resources/" 

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", 
"num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", 
"length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", 
"engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", 
"peak-rpm", "city-mpg", "highway-mpg", "price" ]

df = pd.read_csv(resources_folder + "imports-85.data", header = None)
df.columns = headers

view_data_info(df)

clean_df = get_clean_cars_df(df)

#Escritura en csv del dataframe con cabeceras
clean_df.to_csv(resources_folder + "export.csv")
