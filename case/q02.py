# 2. Podemos deixar a de Catupiry como borda padrão?

# %%

import pandas as pd

df_item_pedido = pd.read_csv("../data/item_pedido.csv")

filtro_borda = df_item_pedido['descTipoItem'] == "borda"

df_borda = df_item_pedido[filtro_borda]

df_group = (df_borda.groupby(['descItem'])['idPedido']
                    .nunique()
                    .reset_index())

df_group['RepPedidos(%)'] = df_group['idPedido'] / df_group['idPedido'].sum()
df_group