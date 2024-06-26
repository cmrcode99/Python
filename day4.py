import pandas as pd
import numpy as np
from numpy.random import randn
df= pd.DataFrame(randn(5,4),index="A B C D E".split(), columns="W X Y Z".split())
print(df)
print(type(df['W']))
print(df.loc[['A','B'],['W','Y']])
a=df.drop('E',axis=0)
print(a)
print(a>0)
c=df[df['W']>0]
print(c)