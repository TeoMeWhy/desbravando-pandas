# %%

import pandas as pd

df = pd.read_csv("../data/bia_consolidado.csv", sep=";")
df

# %%

df = df.set_index(["cod", "nome", "período"])

# %%
df_stack = df.stack().reset_index().rename(columns={"level_3":"Tipo Homicidio",
                                                    0:"Qtde"})


#%%
df_unstack = (df_stack.set_index(['cod','nome','período', 'Tipo Homicidio'])
                      .unstack()
                      .reset_index())

# %%

homicidios = df_unstack['Qtde'].columns.tolist()
indentificadores = df_unstack.columns.droplevel(1).tolist()[:3]

df_unstack.columns = indentificadores + homicidios
df_unstack