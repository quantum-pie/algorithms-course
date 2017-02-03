import urllib
from urllib import request
import numpy as np

fname = input()  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

Y = data[:, 0]
X = np.concatenate((np.ones(shape=(data.shape[0], 1)), data[:, 1:]), axis=1)

theta = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose()).dot(Y)
print(*theta)
