import numpy as np
from numpy.random import randn
from easy_plot import easy_plot

class Process():
	"""
	"""
	def __init__(self, eigen_fn, eigen_val, dist):
		self.e_f = eigen_fn
		self.e_v = eigen_val
		self.dist = dist

	def gen_sample_path(self, time, N):
		W = np.zeros((1, len(time)))
		# Assume that distribution
		Z = self.dist(1,N)[0]

		for n in xrange(1,N+1):
			W += [np.sqrt(2)*Z[n-1]*self.e_f(n,tt)*np.sqrt(self.e_v(n)) 
					for tt in time]

		return W[0]

if __name__ == '__main__':
	e_f = lambda k, tt: np.sin((k-0.5)*np.pi*tt)
	e_v = lambda k: 1/((k-0.5)*np.pi)**2
	dist = randn
	proc = Process(e_f, e_v, dist)

	total_time = 100
	time = [float(tt)/total_time for tt in xrange(0,total_time+1)]

	W1 = proc.gen_sample_path(time, 17)
	W2 = proc.gen_sample_path(time, 50)

	W1_op = np.outer(W1.transpose(),W1)
	W2_op = np.outer(W2.transpose(),W2)

	easy_plot(abs(W1_op))
	easy_plot(abs(W2_op))
	