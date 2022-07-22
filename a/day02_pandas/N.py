import pandas as pd    
import matplotlib.pyplot as plt


#읽기 

df= pd.read_csv('자료실/data.csv')
#df.plot()
# Index(['Duration', 'Date', 'Pulse', 'Maxpulse', 'Calories'], dtype='object') 


# df.plot(kind='scatter',x='Duration',y='Calories')
# df.plot(kind='scatter',x='Duration',y='Pulse')
# df.plot(kind='scatter',x='Duration',y='Maxpulse')
# df.plot(kind='scatter',x='Duration',y='Date')

df['Duration'].plot(kind='hist')



plt.show()