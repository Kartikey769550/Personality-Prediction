import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv', sep=',')

print('Number of participants: ', len(df))
df.head()

print('Is there any missing value? ', df.isnull().values.any())
print('How many missing values? ', df.isnull().values.sum())
df.dropna(inplace=True)
print('Number of participants after eliminating missing values: ', len(df))

print(df)




#Scatter Plot
plt.scatter(df['Age'], df['openness'])
plt.title("Scatter Plot")
plt.xlabel('Age')
plt.ylabel('openness')
plt.show()

#Bar Graph
plt.bar(df['conscientiousness'], df['agreeableness'])
plt.title("Bar Graph")
plt.xlabel('conscientiousness')
plt.ylabel('agreeableness')
plt.show()

#Histogram
plt.hist(df['Personality'])
plt.title("Histogram")
plt.show()

#Box Plot
sns.boxplot(x="Age", y="extraversion",data=df).set(title='Box Plot')
plt.show()

#Line Plot
sns.lineplot(data=df)
plt.title("Line Plot")
plt.show()

#Bar Chart


