import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def easy_plot(A):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	x = np.arange(0,A.shape[0])
	y = np.arange(0,A.shape[1])

	x,y = np.meshgrid(x,y)
	ax.plot_surface(x, y, A)

	plt.show()

if __name__ == '__main__':
	x = np.random.randn(100, 100)
	easy_plot(x)
	