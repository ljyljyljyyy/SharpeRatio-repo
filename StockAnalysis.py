# Importing required modules
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2020,5,1)
end = dt.datetime.now()

df = web.DataReader('BABA','yahoo',start,end)
print(df.head())


