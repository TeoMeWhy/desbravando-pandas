# 5. Hoje só estamos em SP,
# quais os próximos 5 estados devemos abrir filiais?

# %%

import pandas as pd

df_pedido = pd.read_csv("../data/pedido.csv")
df_pedido

# %%

df_not_sp = df_pedido[df_pedido['descUF']!='São Paulo']

(df_not_sp.groupby("descUF")['idPedido']
          .nunique()
          .reset_index()
          .sort_values('idPedido', ascending=False)
          .head(5)
          )