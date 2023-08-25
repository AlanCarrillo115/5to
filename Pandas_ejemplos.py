import pandas as pd

datos = {"nombres:":["Maria","Jose","Juan"], "edad":[20,21,20], "promedio":[100,60,85]}
df_datos = pd.DataFrame(datos)
print(df_datos)

df = pd.read_csv("https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv", sep = ";", decimal = ",")
print(df)
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())
print(df.sample())
print(df.shape)
print(df.size)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df[["edad","colesterol"]].mean())