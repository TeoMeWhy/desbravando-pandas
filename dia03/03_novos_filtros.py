# %%

import pandas as pd

pd.set_option('display.max_rows', 100)

# %%

df_produto = pd.read_csv("../data/produto.csv")

df_produto["primeiroNome"] = df_produto['descItem'].apply(lambda x: x.lower().split(" ")[0])

# %%

df_produto = df_produto.sort_values(
    by=['vlPreco', 'descItem'],
    ascending=[False, True],
)

df_produto.drop_duplicates(subset=['primeiroNome'], keep='first')

# %%
df_produto.drop_duplicates(subset=['primeiroNome', 'vlPreco'], keep='first')

# %%

df_pedido = pd.read_csv("../data/pedido.csv")

df_pedido.dropna(subset=['txtRecado', 'flKetchup'],
                 how='any')