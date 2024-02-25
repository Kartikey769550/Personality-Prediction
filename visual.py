import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("train.csv")
sns.boxplot(x="Personality", y="openness",data=df)
plt.show()
