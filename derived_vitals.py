import pandas as pd
import numpy as np

df = pd.read_csv('/home/saroj/Documents/xerox_challenge/training_Data/new_outlier_free.csv')

print df.head()

index = np.arange(1,df['ID'].iget(-1)+1)

columns = ['ID', 'min1', 'trend1',
            'max3',
            'max6','trend6']
new = pd.DataFrame(index = index, columns = columns)

#print new.head()

for i in index:
	print i ,
	new.loc[i,'ID']=i
	df1 = df[(df['ID']==i)]
	df1 = df1.reset_index(drop=True) 
	
	if df1['V1'].describe()['count']:
		new.loc[i,'min1'] = df1['V1'].min()
		new.loc[i,'trend1'] = (df1.loc[df1['V1'].last_valid_index(),'V1'] - df1.loc[df1['V1'].first_valid_index(),'V1']) / (df1.loc[df1['V1'].last_valid_index(),'TIME'] - df1.loc[df1['V1'].first_valid_index(),'TIME'])

	'''if df1['V2'].describe()['count']:
		new.loc[i,'avg2'] = df1['V2'].mean()
		new.loc[i,'min2'] = df1['V2'].min()
		new.loc[i,'max2'] = df1['V2'].max()'''

	if df1['V3'].describe()['count']:
		new.loc[i,'max3'] = df1['V3'].max()

	if df1['V6'].describe()['count']:
		new.loc[i,'max6'] = df1['V6'].max()
		new.loc[i,'trend6'] = (df1.loc[df1['V6'].last_valid_index(),'V6'] - df1.loc[df1['V6'].first_valid_index(),'V6']) / (df1.loc[df1['V6'].last_valid_index(),'TIME'] - df1.loc[df1['V6'].first_valid_index(),'TIME'])
	
new.to_csv('der_vitals_param_three.csv')




