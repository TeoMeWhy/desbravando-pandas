# %%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df

# %%

condicao = df["IdCustomer"]=="5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user['Points'].sum()

# %%

pontos = {}
for i in df['IdCustomer'].unique():
    condicao = df["IdCustomer"]==i
    pontos[i] = df[condicao]["Points"].sum()

pontos

# %%
df_summary = df.groupby(["IdCustomer"])["Points"].sum()
df_summary.reset_index()

# %%

(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum',
          "UUID": "count",
          "DtTransaction": "max"})
    .rename(columns={
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
   .reset_index())

# %%
import datetime

data1 = df["DtTransaction"][0]
now = datetime.datetime.now()

(now - data1).days

# %%

(datetime.datetime.now() - df["DtTransaction"][0]).days

# %%
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days


(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum',
          "UUID": "count",
          "DtTransaction": ['max', recencia]
          })
    .rename(columns={
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
   .reset_index())