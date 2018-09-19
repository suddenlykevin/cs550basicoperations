# Date to Weekday converter
# Kevin Xie CS550 9/18/2018
# Converts a date into a weekday using operations provided. (only accepts integers)

import sys

m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

y0 = y-int((14-m)/12) # a lot of these return floats, so divisions are all int()'d
x = y0+int(y0/4)-int(y0/100)+int(y0/400)
m0 = m+12*int((14-m)/12)-2
print(int((d+x+(31*m0)/12)%7))