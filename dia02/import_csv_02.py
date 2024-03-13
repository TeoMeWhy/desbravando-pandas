# %%
import pandas as pd

df = pd.read_csv("../data/products.csv",
                 sep=";",
                 names=["Id", "Name", "Description"]
                 )

df

# %%

df = df.rename(columns={"Name":"Nome",
                        "Description":"Descricao"})

df
# %%

df.rename(columns={"Name": "Nome",
                   "Description": "Descricao"},
                   inplace=True)

df