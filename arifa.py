import pandas as pd
df=pd.read_excel(r'C:\Users\Abdul\Downloads\Data_Engineering.xlsx')
df
df.columns

df1=pd.read_excel(r'C:\Users\Abdul\Downloads\Data_Engineering.xlsx',sheet_name=1)
df1
df1.columns

df2=pd.read_excel(r'C:\Users\Abdul\Downloads\Data_Engineering.xlsx',sheet_name=2)
df2
df2.columns

df_cl_f1=df[['Customer_ID', 'Customer_Name']]
df_cl_f1

df_tr_ct=df1.groupby('Customer_ID')['Transaction_Date'].count()
df_tr_ct
df_tr_ct2=pd.DataFrame(df_tr_ct)
df_tr_ct2

df_cl_f2=df2[['Customer_ID','Income']]
df_cl_f2()

df_merge1=df_cl_f1.merge(df_tr_ct2,how='inner',on='Customer_ID')
df_merge1
df_merge2=df_merge1.merge(df_cl_f2,how='inner',on='Customer_ID')
df_merge2

df_cond1=df_merge2[((df_merge2.Income>10000)&(df_merge2.Income<30000))&(df_merge2.Transaction_Date>=2)]
df_cond1

df_cond2=df_merge2[((df_merge2.Income>30000)&(df_merge2.Income<50000))&(df_merge2.Transaction_Date>=1)]
df_cond2

df_cond3=df_merge2[((df_merge2.Income>50000)&(df_merge2.Income<60000))&(df_merge2.Transaction_Date>=1)]
df_cond3

df_cond4=df_merge2[((df_merge2.Income>60000))&(df_merge2.Transaction_Date>=2)]
df_cond4

df_ap=pd.concat([df_cond1,df_cond2,df_cond3,df_cond4],axis=0,ignore_index=True)
df_ap
