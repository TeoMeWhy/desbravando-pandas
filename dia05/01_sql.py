# %%

import pandas as pd
import sqlalchemy

def import_query(path):
    with open(path, 'r') as open_file:
        query = open_file.read()
    return query

# %%

engine = sqlalchemy.create_engine("sqlite:///../data/database.db")

# %%

query = 'SELECT * FROM produto WHERE vlPreco > 10'

df_prod_10 = pd.read_sql_query(query, engine)
df_prod_10

# %%

query = import_query("pedido_item_preco.sql")
print(query)

# %%

df_item_pedido_preco = pd.read_sql_query(query, engine)
df_item_pedido_preco

# %%
query_uf_pedido = import_query("qtde_pedidos_estado.sql")
df_pedido_estado = pd.read_sql_query(query_uf_pedido, engine)
df_pedido_estado

# %%

import matplotlib.pyplot as plt

df_pedido_estado.boxplot('qtdePedido')

# %%

import datetime

top5_uf = (df_pedido_estado.sort_values("qtdePedido", ascending=False)
                           .head(5))

top5_uf['dt_ingestao'] = datetime.datetime.now()

top5_uf.to_sql('top5_uf_pedido', engine, if_exists='append')
