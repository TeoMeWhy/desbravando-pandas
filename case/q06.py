# 6. A preferência do tipo de massa muda entre os estados?

# %%
import pandas as pd

df_item_pedido = pd.read_csv("../data/item_pedido.csv")
df_pedido = pd.read_csv("../data/pedido.csv")

# %%
filtro_massa = df_item_pedido['descTipoItem'] == 'massa'
df_massa = df_item_pedido[filtro_massa].merge(df_pedido[['idPedido', 'descUF']],
                                              how='left')

df_analise = (df_massa.groupby(['descItem','descUF'])['idPedido']
                      .nunique()
                      .reset_index()
                      .sort_values(['descUF', 'descItem'])
                      .pivot_table(values='idPedido', columns='descItem', index='descUF')
                      .reset_index()
                      .fillna(0))

df_analise.to_csv("analise_borda_estado.csv", sep=";", index=False)