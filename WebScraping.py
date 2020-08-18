# Importing required modules
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2018,1,1)
end = dt.datetime.now()

df = web.DataReader('BABA','yahoo',start,end)
print(df.head())

#df.to_csv('StockBABA.csv')

#import datetime index
#df = pd.read_csv('StockBABA.csv',parse_dates=True, index_col=0)
#print(df.head())

#df.plot()
#plt.show()

