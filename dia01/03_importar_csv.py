# %%

import pandas as pd

# %%

df = pd.read_csv("../data/pedido.csv")
df

# %%
df.columns

# %%
df.shape

# %%
df.index

# %%
df.info(memory_usage='deep')

# %%
tipos_colunas = df.dtypes
tipos_colunas

# %%

df
# %%
# Cabeçalho dos dados
df.head(20)

# %%
df.tail(5)

# %%

df.sample(10)
