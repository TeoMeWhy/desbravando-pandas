# %%
import pandas as pd

# %%

data = {
    "nome":["Téo", "Nah", "Maria", "José", "Marina", "Jessica", "InfoSlack"],
    "idade":[30, 33, 2, 45, 65, 43, 40],
    "cor": ["Preto", "Verde", "Azul", "Vermelho", "Amarelo", "Verde", "Azul"],
    "renda": [3566, 1345, 0, 6576, 4325, 5326, 10244]
}

data["idade"]

# %%
df = pd.DataFrame(data)
df["idade"]

# %%

type(df["idade"])

# %%

df[['idade', 'renda']].describe()

# %%

df.mean()