import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df = pd.read_csv("train.csv")

print(titanic_df.head(5))

titanic_df.drop(["Parch",'PassengerId','Name','SibSp','Ticket','Fare'],inplace = True,axis = 1)

print(titanic_df.head(5))

titanic_df["Embarked"] = titanic_df["Embarked"].fillna("S")
titanic_df["Embarked"] = titanic_df["Embarked"].map({
    'S':'Southhampton',
    'C':'Cherbourg',
    'Q':'Queensland'
})

titanic_df["Survived"] = titanic_df["Survived"].map({
    0:'Died',
    1:'Survived'
})

titanic_df['Pclass'] = titanic_df['Pclass'].map({
    1:'Luxury class',
    2:'economy class',
    3:'lower class'
})

#Data visualisations
#visualistion 1 class - survival
print(pd.crosstab(titanic_df['Pclass'],titanic_df['Survived']))
ax = sns.countplot(x='Pclass',hue='Survived',data = titanic_df)
ax.set(title='survival rate based on passenger class',xlabel='passenger class',ylabel='total')
plt.show()

#visualisation 2 embarked - survival
print(pd.crosstab(titanic_df["Embarked"],titanic_df["Survived"]))
ax = sns.countplot(x='Embarked', hue='Survived',data = titanic_df)
ax.set(title='survival rate based on embarkment port',xlabel='embark port',ylabel='total')
plt.show()

#visualisation 3 sex - survival
print(pd.crosstab(titanic_df["Sex"],titanic_df["Survived"]))
ax = sns.countplot(x = 'Sex',hue='Survived',data=titanic_df)
ax.set(title='survival rate based on sex',xlabel='sex',ylabel='total')
plt.show()

#visualisation 4 age - survival
categories = ['child','teen','adult','grandparent']
interval = (0,12,20,50,120)
ax = sns.countplot()
titanic_df["Age cat"] = pd.cut(titanic_df["Age"],interval,labels = categories)
pd.crosstab()
ax = sns.countplot(x = 'Age cat',hue = "Survived",data = titanic_df)
ax.set(title='survival rate based on age category',xlabel = 'age categories',ylabel='total')
plt.show()
