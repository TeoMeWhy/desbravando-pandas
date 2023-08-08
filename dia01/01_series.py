# %%
import pandas as pd

# %%

# Isso é uma lista!!!!
idade = [31, 33, 2, 29, 60, 58, 31, 45, 24]

# %%
s_idade = pd.Series(idade)
s_idade

# %%

# Métodos das Séries
media = s_idade.mean()
variancia = s_idade.var()
des_pad = s_idade.std()
describe = s_idade.describe()
describe

# %%

nova_idade=[]
for i in idade:
    if i >= 30:
        nova_idade.append(i)

nova_idade

# %%

filtro = s_idade >= 30
s_idade[~filtro]

# %%

filtro = [True, False, True, True, False, False, False, False, True]
s_idade[filtro]