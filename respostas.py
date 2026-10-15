#%%
import pandas as pd

df = pd.read_csv("tested.csv", sep = ",")
df
# %%
#Quantos passageiros sobreviveram?
survived = df.groupby('Survived').size()
survived
#sobreviveram 152 pessoas
 # %%
 #Qual era a proporção entre homens e mulheres?
sex = df['Sex'].value_counts()
proporção_m = sex['male'] / len(df['Sex']) * 100
proporção_f = sex['female']/len(df['Sex']) * 100
print(f"proporção de homens{proporção_m}")
print(f"proporção de mulheres{proporção_f}")
#a proporção é de 63,6 porcento de homens e a de mulheres é de 36,4 porcento
# %%
#Qual era a idade média dos passageiros?
idade_media = df['Age'].mean()
print(idade_media)
#a idade media e de 30 anos
# %%
#A taxa de sobrevivência foi maior entre homens ou mulheres?
m = df.query("Sex == 'male' and Survived == 1")[["Sex","Survived"]].sum()
f = df.query("Sex == 'female' and Survived ==1")[["Sex","Survived"]].sum()
print(f"mulheres: {f}, homens: {m}")
#a maior taxa de sobrevivencia foram das mulheres
# %%
#Qual classe apresentou a maior taxa de sobrevivência?
classe_sobrevivente = df.groupby('Pclass')['Survived'].mean()
maior_classe = classe_sobrevivente.idxmax()
print(maior_classe)
#a classe com maior taxa de sobrevivencia foi a 1
# %%
#Existe alguma relação aparente entre idade e sobrevivência?
correlação = df['Age'].corr(df['Survived'])
print(f"correlação entre idade e sobrevivencia: {correlação:.4f}")
#não existe relação de idade com sobrevivencia
# %%
