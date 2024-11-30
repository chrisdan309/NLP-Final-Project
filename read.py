import pandas as pd

# Leer el archivo Parquet
df = pd.read_parquet('train-00000-of-00001.parquet')

# Mostrar las primeras filas del DataFrame
print(df.head(10))
