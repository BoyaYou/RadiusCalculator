import pandas as pd
import numpy as np

def RollingAlgorithm(path):
	data = pd.read_csv(path)
	d = pd.DataFrame()

	for i in range(len(data)-2):
		A=[data['Longitude'][i],data['Latitude'][i]]
		B=[data['Longitude'][i+1],data['Latitude'][i+1]]
		C=[data['Longitude'][i+2],data['Latitude'][i+2]]

		if A==B or A==C or B==C:
			d.set_value(i+1, 'centerLongitude', 'NA')
			d.set_value(i+1, 'centerLatitude', 'NA')
			d.set_value(i+1, 'Radius', 'Inf')
			print 'Skip %d point:' %(i) + ' Same location'
		elif A[1]!=B[1] and B[1]!=C[1] and (B[0]-A[0])/(B[1]-A[1])!=(C[0]-B[0])/(C[1]-B[1]):
			a=np.array([[(B[0]-A[0])/(B[1]-A[1]),1],[(C[0]-B[0])/(C[1]-B[1]),1]])
			b=np.array([(A[1]+B[1])/2+(B[0]-A[0])*(A[0]+B[0])/(2*B[1]-2*A[1]),(B[1]+C[1])/2 + (C[0]-B[0])*(B[0]+C[0])/(2*C[1]-2*B[1])])
			CP = np.linalg.solve(a,b)
			dx = ((CP[0]-A[0])**2+(CP[1]-A[1])**2)**0.5
			d.set_value(i+1, 'centerLongitude', CP[0])
			d.set_value(i+1, 'centerLatitude', CP[1])
			d.set_value(i+1, 'Radius', dx)
		elif (B[0]-A[0])/(B[1]-A[1])==(C[0]-B[0])/(C[1]-B[1]):
			d.set_value(i+1, 'centerLongitude',None)
			d.set_value(i+1, 'centerLatitude',None)
			d.set_value(i+1, 'Radius',None)
			print 'Skip %d point:' %(i)+' 3 points are on the same line'
		
		else: 
			print 'Skip %d point:' %(i)+' please double check this point'
	return d

if __name__ == '__main__':
	d = RollingAlgorithm('C:\Users\user\Desktop\GPS.csv')
	print d.head()
	d.to_csv('radius.csv')