import pandas as pd
import numpy as np
import urllib
from io import StringIO

def get_cleaned_data():
	link = "https://firebasestorage.googleapis.com/v0/b/warewolves.appspot.com/o/PM_train.csv?alt=media&token=89333a8a-bef3-458d-8269-fe0bfd5572fa"
	f = urllib.request.urlopen(link)
	myfile = f.read()
	s=str(myfile,'utf-8')
	data = StringIO(s)
	dataset_train=pd.read_csv(data,sep=' ',header=None).drop([26,27],axis=1)


	#dataset_train=pd.read_csv("/Users/divalicious/Desktop/PredictiveMaintainence/PM_train.txt",sep=' ',header=None).drop([26,27],axis=1)
	col_names = ['id','cycle','setting1','setting2','setting3','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','s15','s16','s17','s18','s19','s20','s21']
	dataset_train.columns=col_names
	dataset_train['ttf'] = dataset_train.groupby(['id'])['cycle'].transform(max)-dataset_train['cycle']
	dataset_train.head()
	df_train=dataset_train.copy()
	period=30
	df_train['label_bc'] = df_train['ttf'].apply(lambda x: 1 if x <= period else 0)
	result=dataset_train.to_json()


	return(result)



