import pandas as pd
#df1 = pd.DataFrame({'id':[1,2,3],'col1':['a','b','c']})
#df2 = pd.DataFrame({'id':[4,3],'col2':['d','e']})

#print(df1)

#print(df1.merge(df2,how='inner',on='id'))

#print(df1.merge(df2,how='left',on='id'))

#print(df1.merge(df2,how='right',on='id'))

#print(df1.merge(df2,how='outer',on='id'))

df1 = pd.DataFrame({'id':[1,2,3],'col1':['a','b','c']},index=[1,2,3])

df2 = pd.DataFrame({'id2':[1,2,3],'col2':['aa','bb','cc']},index=[1,3,2])

#print(df2)

#print(pd.concat([df1,df2],axis=1))

df1.join(df2)