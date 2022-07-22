import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset("tips")

print(df)

sns.distplot(df['total_bill'])
plt.show()