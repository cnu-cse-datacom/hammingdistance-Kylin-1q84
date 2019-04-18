import random
import numpy as np
import pandas as pd
from hamming_practice import hamming

df = pd.read_csv('sample.csv',names=['word','bin'])


count = 0
xor_lambda = lambda a,b:hamming(a,b)
count_lambda = lambda x: x==1
minimum = 32

for i in range(0,len(df)):
	for j in range(i+1,len(df)):
		hd = xor_lambda(df.iloc[i,1],df.iloc[j,1])
		print(count, "(",df.iloc[i,0],df.iloc[j,0],")","hamming_distance: ", hd)
		if(hd<minimum):
			minimum = hd
		count +=1


print("min hamming distance", minimum)
