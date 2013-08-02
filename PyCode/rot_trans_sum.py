import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from easy_plot import easy_plot
from process import Process
from rotate import rotate

def rot_trans_sum(n, p1=45, p2=45):
	tt = np.arange(0, 1, .01)
	A = np.zeros((len(tt), len(tt)))

	thetas = np.floor(np.random.rand(n,1)*2*np.pi)

	for i in xrange(n):
		e_f = lambda k, tt: np.sin((k-0.5)*np.pi*tt)
		e_v = lambda k: 1/((k-0.5)*np.pi)**2
		dist = randn
		proc = Process(e_f, e_v, dist)

		w1 = proc.gen_sample_path(tt, p1)
		w2 = proc.gen_sample_path(tt, p2)
		T = np.outer(w1.transpose(), w2)


## Add a smoother to this. 
## Remove the random part, e.g. sample uniformly and 
## see what happens.  
## Make sure I understand and edit all the classes.
## Add in the Brownian Bridge.


		#T = np.dot(w1.transpose(), w2)
#		print T
		
#		print thetas[i][0]
		
		T = rotate(T, thetas[i][0])
		A = A + T[0:len(tt),0:len(tt)]
	return abs(A)

if __name__ == '__main__':
	A = rot_trans_sum(10)
	easy_plot(A)
	
