import math

a = 0
b = 0
c = 0

while True:
    c = math.sqrt(a**2 + b**2)
    if a+b+c > 1000:
        a -= 1
    else:
        a+=1

        #??????????????????????