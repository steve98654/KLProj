import numpy as np
from numpy.random import randn
from easy_plot import easy_plot
from math import sqrt,sin,cos

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

def twodfun(s,t,theta,r1,r2,ef,ev,n):
    tpvl = 0
    for i in xrange(0,n):
        for j in xrange(0,n):
            tpvl += (r1[i]*r2[j]*sqrt(ev(i)*ev(j))*ef(i,s*cos(theta)-t*sin(theta))
                    *ef(j,s*sin(theta)+t*cos(theta)))
                     
    return tpvl        

if __name__ == '__main__':
    e_f = lambda k, tt: np.sin((k-0.5+1)*np.pi*tt)
    e_v = lambda k: 1/((k-0.5+1)*np.pi)**2
    dist = randn
    
    proc = Process(e_f, e_v, dist)
    nmds = 30
    nms1 = randn(nmds)
    nms2 = randn(nmds)

    time = np.linspace(0, 1, 100)
    W1 = proc.gen_sample_path(time, nmds)
    W2 = proc.gen_sample_path(time, nmds)

    W1_op = np.outer(W1,W2)
#    W2_op = np.outer(W2.transpose(),W2)

    pts = 30
    s1 = np.linspace(0,1,pts)
    t1 = np.linspace(0,1,pts)
    s,t = np.meshgrid(s1,t1)
    z = np.zeros((pts,pts))
    th = np.linspace(0,2*np.pi,10)

    for theta in th:
        for i in xrange(0,pts):
            for j in xrange(0,pts):
                z[i][j] = twodfun(s1[i], t1[j], theta, nms1, nms2, e_f, e_v,30)
    
    easy_plot(z)

    np.savetxt("tstarr1234.csv", z, delimiter=",")

