# %%
import pandas as pd
import numpy as np

# %%

df = pd.read_csv("../data/produto.csv")


# %%
df = df.rename(columns={"vlPreco": "vlPrecoReal"})

# %%
filtro = df["vlPrecoReal"] > 10
df[filtro]

# %%
queijos_premium = ['queijo brie', 'queijo coalho', 'ricota']
filtro_queijos = df['descItem'].isin(queijos_premium)
df[filtro_queijos]

# %%

df['vlPrecoinflacao'] = (df['vlPrecoReal'] * 1.09).round(2)
df

# %%

df['vlPrecoinflacaoLog'] = np.log(df['vlPrecoinflacao'])
df