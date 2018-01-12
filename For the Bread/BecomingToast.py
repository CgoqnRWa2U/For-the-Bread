#Hopefully it Works    -Reese Witherspoon 1924
import pandas_datareader.data as d
from datetime import datetime as c
class b:
    def __init__(self):
        pass
    
    def returnChartData (self, b, a, c = 'yahoo'):
        return d.DataReader(b, c, a)
    
class a:
    stockID = "0001.HK"   
    e = c(2017, 5, 1)
    
    requester = b()
    e = requester.returnChartData(stockID, e) 
    
    print(e)
    