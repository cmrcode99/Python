import numpy as np
import pandas as pd
df=pd.DataFrame({'A':[1,2,np.nan],'B':[5,np.nan, np.nan,], 'C':[1,2,3]})
print(df)
z=df.dropna()
print(z)
zy=df.dropna(axis=1)
print(zy)
zyy=df.dropna(thresh=2)
print(zyy)
