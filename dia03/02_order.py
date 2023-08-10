# %%
import pandas as pd

pd.set_option('display.max_rows', 500)

# %%
df_produto = pd.read_csv("../data/produto.csv")
df_produto

# %%
df_produto.sort_values(by="vlPreco", ascending=False)

# %%
df_produto.sort_values(by=["vlPreco", 'descItem'], ascending=[False, True])