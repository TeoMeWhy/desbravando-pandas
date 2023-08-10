# %%

import pandas as pd

# %%

df_produto = pd.read_csv("../data/produto.csv")
df_produto

# %%
## Maneira 1
## Criando nossa própria função com def

def is_massa(x):
    return x.lower().startswith('massa')

df_produto['flMassa'] = df_produto["descItem"].apply(is_massa)
df_produto[df_produto['flMassa']]

# %%
## Maneira 2
## Usando uma função anonima no apply
df_produto["descItem"].apply(lambda x: x.lower().startswith('massa'))

# %%
## Maneira 3
## Usando os métodos de str
df_produto["descItem"].str.lower().str.startswith('massa')