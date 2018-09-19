# Farenheit and wind speed to Effective Temperature basic operation
# Kevin Xie CS550 9/18/2018
# put temperature in first argument and wind speed in second. (only valid if |t|>50 && v>120 or v<3)

import sys

t = float(sys.argv[1])
v = float(sys.argv[2])

print(35.74+0.6215*t+(0.4275*t-35.75)*v**0.16)