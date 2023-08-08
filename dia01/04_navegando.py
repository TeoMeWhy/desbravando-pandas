# %%
import pandas as pd

df = pd.read_csv("../data/pedido.csv")
df

# %%

# SELECT idPedido, flKetchup from pedido
df[['idPedido', 'flKetchup']]

# %%

# SELECT idPedido, descUF, flKetchup, txtRecado, dtPedido
# from pedido

colunas = [
    'idPedido',
    'descUF',
    'flKetchup',
    'txtRecado',
    'dtPedido',
]

df = df[colunas]

# %%
# Cria um dataframe novo com 100 dados aleatórios do antigo
df_sample = df.sample(100)

# %%
df_sample.iloc[0]

# %%
df.loc[33:384]

# %%
df_sample.iloc[0:10][['idPedido', 'dtPedido']]
