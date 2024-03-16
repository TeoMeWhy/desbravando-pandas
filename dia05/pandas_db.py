# %%

import pandas as pd
import sqlalchemy


# %%

engine = sqlalchemy.create_engine("sqlite:///../data/database.db")

# %%

df_transactions_cart = pd.read_sql_table("transactions_cart", engine)
df_transactions_cart

# %%

query = "SELECT * FROM customers LIMIT 10"
df_customers = pd.read_sql_query(query, engine)
df_customers

# %%

query = """
SELECT *
FROM customers AS t1
LEFT JOIN transactions AS t2
ON t1.UUID = t2.IdCustomer
LIMIT 10
"""

df_join = pd.read_sql_query(query, engine)
df_join

# %%


data_01 = {
    "id": [1,2,3,4],
    "nome":["Teo", "Mat", "Nah", "Mah"],
    "idade": [31,31,32,32]
}
df_01 = pd.DataFrame(data_01)

data_02 = {
    "id": [5,6,7,8],
    "nome":["Jose", "Nathan", "Arnaldo", "Mario"],
    "idade": [23,33,19,21]
}

df_02 = pd.DataFrame(data_02)

# %%

df_01.to_sql("tb_fodase", engine, index=False)

# %%

df_02.to_sql("tb_fodase", engine, index=False, if_exists="replace")

# %%

pd.read_sql("tb_fodase", engine)