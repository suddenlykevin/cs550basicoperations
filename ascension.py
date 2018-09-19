# Ascending and Descending Detector
# Kevin Xie CS550 9/18/2018
# Detects whether or not x, y, and z are "consecutive" in terms of ascending or descending value

import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

if (x>y>z) or (x<y<z):
	print(True)
else:
	print(False)