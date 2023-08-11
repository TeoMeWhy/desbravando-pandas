# 3. Vários queijos estão estragando pela validade.
#  Quais queijos juntos atendem 90% dos pedidos?

# %%

import pandas as pd

df_item_pedido = pd.read_csv("../data/item_pedido.csv")
df_item_pedido.head()

# %%

filtro_queijo = df_item_pedido['descTipoItem'].apply(lambda x: 'queijo' in x.lower())
df_queijo = df_item_pedido[filtro_queijo]

df_group = (df_queijo.groupby(['descItem'])['idPedido']
                     .nunique()
                     .reset_index()
                     .sort_values('idPedido', ascending=False)
                     )

df_group

# %%
df_group['pct'] = df_group['idPedido'] / df_group['idPedido'].sum()
df_group

# %%
df_group['pctAcum'] = df_group['pct'].cumsum()
df_group