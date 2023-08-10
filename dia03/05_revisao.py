# %%

import pandas as pd

df = pd.read_csv("../data/produto.csv")
df

# %%

df["desItemPrimNome"] = df['descItem'].apply(lambda x: x.lower().split(" ")[0])
df

# %%

df.sort_values(by=['vlPreco', 'descItem'],
               ascending=[False, True])

# %%

df.drop_duplicates(subset=['desItemPrimNome'], keep='first')

# %%

(df.groupby(['desItemPrimNome'])
   .agg({'vlPreco':['mean', 'count']}))