# %%
import pandas as pd

# %%
idade = pd.Series([30,33,21,43,53,6,45,41])
idade.describe()

# %%
df = pd.DataFrame({
    "nome":["teo", "maria", "jose"],
    "idade":[30,2,45]
    })

df

# %%
df_pedido = pd.read_csv("../data/pedido.csv")
df_pedido

# %%
df_pedido.head(5)  # 5 primeiras linhas
df_pedido.tail(5)  # 5 últimas linhas
df_pedido.sample(5)    # 5 linhas aleatórias

# %%
df_pedido.info(memory_usage='deep')

# %%
df_pedido.dtypes

# %%
df_pedido[['descUF', 'flKetchup']]

# %%
df_pedido.iloc[892:900]

# %%
df_pedido.loc[892]