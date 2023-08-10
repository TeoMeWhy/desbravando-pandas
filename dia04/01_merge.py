# %%
import pandas as pd

# %%

df_item_pedido = pd.read_csv("../data/item_pedido.csv")
df_produto = pd.read_csv("../data/produto.csv")
df_pedido = pd.read_csv("../data/pedido.csv")

df_item_pedido
# %%

## Maneira 1

df_join = df_item_pedido.merge(right=df_produto,
                               how='left')

df_join.merge(df_pedido, how='left')

# %%
df_join = (df_item_pedido.merge(right=df_produto, how='left')
                         .merge(right=df_pedido[['idPedido', 'descUF']], how='left',))

df_join