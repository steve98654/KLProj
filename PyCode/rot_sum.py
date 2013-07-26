import numpy as np
from . import rotate

def rot_sum(A, deg_low, deg_high, theta_deg):
	def_range = deg_high-deg_low
	num_terms = np.floor(deg_range/theta_deg)

	rows, cols = A.shape

	A_rot_sum = np.zeros((rows,cols))

	for m in xrange(num_terms+1):
		theta = (m*theta_deg) + deg_low
		A_rot = rotate(A, theta)
		A_rot_sum += A_rot

	return A_rot_sum