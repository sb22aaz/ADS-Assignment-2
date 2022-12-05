import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def return_df(fname):
    data = pd.read_csv(fname,header=None,index_col=0).T
    #data=data.drop(["Country Code","Indicator Name","Indicator Code"],axis=1)
    #print(type(data))
    df = pd.DataFrame(data)
    df=df.rename(columns={"Country Name":"Year"})
    return df

filename="C:\\Users\\sb22aaz\\Desktop\\New folder\\population.csv"
df=return_df(filename)
df.plot("Year", ["India","China","Japan","United Kingdom","United States"])
print(df)