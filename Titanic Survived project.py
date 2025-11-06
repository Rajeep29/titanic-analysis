import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# Load dataset (assuming cleaned or from Seaborn)
df = sns.load_dataset('titanic')

# Data Cleaning (same as before)
df['deck'] = df['deck'].astype(object)
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
df['deck'].fillna('Unknown', inplace=True)
df.dropna(subset=['embark_town'], inplace=True)

# Quick check
print(df.head())
print(df.isnull().sum())

print(df['survived'].value_counts(normalize=True)*100)
print(sns.countplot(x="sex",hue="survived",data=df,palette="coolwarm"))
plt.show()
print(sns.countplot(x="pclass",hue="survived",data=df,palette="viridis"))
plt.show()
print(sns.histplot(x="age",data=df,bins=20,kde=True,color="blue"))
plt.show()
print(sns.heatmap(df.corr(numeric_only=True),annot=True))
plt.show()
survival_gender=df.groupby("sex")["survived"].value_counts(normalize=True).unstack()*100
print(survival_gender)
survival_byclass=df.groupby("pclass")["survived"].value_counts(normalize=True).unstack()*100
print(survival_byclass)
survival_gender_class=df.groupby(["sex","pclass"])["survived"].value_counts(normalize=True).unstack()*100
print(survival_gender_class)
survival_gender_class.plot(kind="bar",stacked=True,colormap="coolwarm")
plt.show()
df["family_size"]=df["sibsp"]+df["parch"]+1
family_survival=df.groupby("family_size")["survived"].mean()*100
print(family_survival)
family_survival.plot(kind="bar",color="skyblue")
plt.show()
sns.kdeplot(df.loc[df["survived"]==1,"age"],label='Survived', fill=True)
sns.kdeplot(df.loc[df["survived"]==0,"age"],label='unSurvived', fill=True)
plt.show()

      





