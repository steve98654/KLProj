from scipy.ndimage.interpolation import affine_transform
from scipy.ndimage.interpolation import rotate as imrot
import numpy as np

def rotate(A, theta):
	r1 = np.zeros((3,3))
	r1[0] += [np.cos(theta), -np.sin(theta), 0]
	r1[1] += [np.sin(theta), np.cos(theta), 0]
	r1[2] += [0, 0, 1]

	tr1 = imrot(A, theta)
	#print tr1
	return tr1
	
	#theta = theta * np.pi / 180
	
	#r2 = np.zeros((2,2))
	#r2[0] = [np.cos(theta), -np.sin(theta)]
	#r2[1] = [np.sin(theta), np.cos(theta)]
	
	#print r1, r2
	#A_rows, A_cols = A.shape
	
	#tr1 = affine_transform(A, r2, [float(A_rows)/2, float(A_cols)/2], output_shape=(A_rows, A_cols))
	#tr1 = affine_transform(A, r2, [float(A_rows), float(A_cols)], output_shape=(A_rows, A_cols))
	#tr1 = affine_transform(A, r2, 7, output_shape=(A_rows, A_cols))
	
	#tr1 = affine_transform(A, r2)
	#tr1_rows, tr1_cols = tr1.shape

	#print 'tr1', tr1
	
	#row_range = range((tr1_rows/2-A_rows/2)-1,(tr1_rows/2+A_rows/2))
	#col_range = range((tr1_cols/2-A_cols/2)-1,(tr1_cols/2+A_cols/2))

	#print 'rot tr1', tr1[(tr1_rows/2-A_rows/2):(tr1_rows/2+A_rows/2),(tr1_cols/2-A_cols/2):(tr1_cols/2+A_cols/2)]
	
	#return tr1[row_range, col_range]
	#return tr1[(tr1_rows/2-A_rows/2):(tr1_rows/2+A_rows/2),(tr1_cols/2-A_cols/2):(tr1_cols/2+A_cols/2)]
	
if __name__ == '__main__':
	a = np.random.rand(10, 10)
	print a
	print rotate(a, 30)
	