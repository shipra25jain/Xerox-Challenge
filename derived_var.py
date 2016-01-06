import pandas as pd
import numpy as np

df = pd.read_csv('lab_no_outlier.csv')
dfage = pd.read_csv('id_age_train.csv')
df = df.reset_index(drop=True)
#print df.head()

index = np.arange(0,dfage.shape[0])

columns = ['age','min1', 
		   'min3', 'trend3',
		   'min5','max6', 'max7','max8',
		   'max9',
		   'min11',
		   'max12',
		  # 'init13', 'avg13', 'min13', 'max13', 'time13', 'diff13', 'last13',
		  # 'avg15', 'min15', 'max15',
		   #'avg16', 'min16', 'max16', 
		  # 'init17', 'avg17', 'min17', 'max17', 'time17', 'diff17', 'last17',
		   #'avg18', 'min18', 'max18', 
		  # 'init19', 'avg19', 'min19', 'max19', 'time19', 'diff19', 'last19',
		  # 'avg20', 'min20', 'max20',
		  # 'avg21', 'min21', 'max21',
		   #'avg22', 'min22', 'max22', 
		  # 'avg23', 'min23', 'max23', 
		   #'init24', 'avg24', 'min24', 'max24', 'time24', 'diff24', 'last24',
		   #'avg25', 'min25', 'max25', 
		  ]
new = pd.DataFrame(index = index, columns = columns)

#print new.head()

for i in index:
	print i ,
	new.loc[i,'ID']=i
	j = i + int(df.loc[0,'ID'])
	df1 = df[(df['ID']==j)]
	df1 = df1.reset_index(drop=True)
	if df1['L1'].describe()['count']:
		new.loc[i,'min1'] = df1['L1'].min()
		

	#if df1['L2'].describe()['count']:
		#new.loc[i,'avg2'] = df1['L2'].mean()
		#new.loc[i,'min2'] = df1['L2'].min()
		#new.loc[i,'max2'] = df1['L2'].max()

	
	if df1['L3'].describe()['count']:
		new.loc[i,'min3'] = df1['L3'].min()
		new.loc[i,'trend3'] = (df1.loc[df1['L3'].last_valid_index(),'L3'] - df1.loc[df1['L3'].first_valid_index(),'L3']) / (df1.loc[df1['L3'].last_valid_index(),'TIME'] - df1.loc[df1['L3'].first_valid_index(),'TIME'])
	
	#if df1['L4'].describe()['count']:
	#	new.loc[i,'avg4'] = df1['L4'].mean()
	#	new.loc[i,'min4'] = df1['L4'].min()
	#	new.loc[i,'max4'] = df1['L4'].max()
	
	if df1['L5'].describe()['count']:
		new.loc[i,'min5'] = df1['L5'].min()
	
	if df1['L6'].describe()['count']:
		new.loc[i,'max6'] = df1['L6'].max()

	if df1['L7'].describe()['count']:
		new.loc[i,'max7'] = df1['L7'].max()

	if df1['L8'].describe()['count']:
		new.loc[i,'max8'] = df1['L8'].max()

	if df1['L9'].describe()['count']:	
		new.loc[i,'max9'] = df1['L9'].max()

	#if df1['L10'].describe()['count']:
	#	new.loc[i,'min10'] = df1['L10'].min()
	#	new.loc[i,'max10'] = df1['L10'].max()
	#
	if df1['L11'].describe()['count']:
		new.loc[i,'min11'] = df1['L11'].min()


	if df1['L12'].describe()['count']:
		new.loc[i,'max12'] = df1['L12'].max()

	'''if df1['L14'].describe()['count']:
		new.loc[i,'avg14'] = df1['L14'].mean()
		new.loc[i,'min14'] = df1['L14'].min()
		new.loc[i,'max14'] = df1['L14'].max()'''

	'''if df1['L15'].describe()['count']:
		new.loc[i,'avg15'] = df1['L15'].mean()
		new.loc[i,'min15'] = df1['L15'].min()
		new.loc[i,'max15'] = df1['L15'].max()'''

	'''if df1['L16'].describe()['count']:
		new.loc[i,'avg16'] = df1['L16'].mean()
		new.loc[i,'min16'] = df1['L16'].min()
		new.loc[i,'max16'] = df1['L16'].max()'''

	'''if df1['L18'].describe()['count']:
		new.loc[i,'avg18'] = df1['L18'].mean()
		new.loc[i,'min18'] = df1['L18'].min()
		new.loc[i,'max18'] = df1['L18'].max()'''
	'''if df1['L19'].describe()['count']:
		new.loc[i,'avg19'] = df1['L19'].mean()
		new.loc[i,'min19'] = df1['L19'].min()
		new.loc[i,'max19'] = df1['L19'].max()
	'''
	'''if df1['L20'].describe()['count']:
		new.loc[i,'avg20'] = df1['L20'].mean()
		new.loc[i,'min20'] = df1['L20'].min()
		new.loc[i,'max20'] = df1['L20'].max()

	if df1['L21'].describe()['count']:
		new.loc[i,'avg21'] = df1['L21'].mean()
		new.loc[i,'min21'] = df1['L21'].min()
		new.loc[i,'max21'] = df1['L21'].max()

	if df1['L22'].describe()['count']:
		new.loc[i,'avg22'] = df1['L22'].mean()
		new.loc[i,'min22'] = df1['L22'].min()
		new.loc[i,'max22'] = df1['L22'].max()

	if df1['L23'].describe()['count']:
		new.loc[i,'avg23'] = df1['L23'].mean()
		new.loc[i,'min23'] = df1['L23'].min()
		new.loc[i,'max23'] = df1['L23'].max()


	if df1['L25'].describe()['count']:
		new.loc[i,'avg25'] = df1['L25'].mean()
		new.loc[i,'min25'] = df1['L25'].min()
		new.loc[i,'max25'] = df1['L25'].max()'''

new.to_csv('der_lab_param_three.csv')




