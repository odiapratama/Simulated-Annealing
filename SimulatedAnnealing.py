import random
import math

cr=0.9999
t0=1000000
tmin=1
x1=random.uniform(-10,10)
x2=random.uniform(-10,10)
randx=random.uniform(0,1)

def f(x1,x2):
    return (4-(2.1*(x1**2))+(x1**4)/3)*(x1**2)+(x1*x2)+(-4+(4*(x2**2))*x2**2)

"""Current State"""
cs=f(x1,x2)
while (t0>tmin):
    y1 = (random.uniform(-10, 10))
    y2 = (random.uniform(-10, 10))*(0.1*y1)
    y1 = y1*(0.1*y2)
    #print("y1 = " ,y1)
    #print("y2 = " ,y2)
    """New State"""
    ns=f(y1,y2)

    if (ns<cs):
        cs=ns
        x1hasil=y1
        x2hasil=y2
        print("Nilai Minimun    = ", cs)
    else:
        if (math.exp((cs-ns)/t0)> randx):
            cs=ns
            x1hasil = y1
            x2hasil = y2
            print("Nilai Minimun    = ", cs)
    t0=t0*cr

print("=======================================")
print("X1 Minimun       = ",x1hasil)
print("X2 Minimun       = ",x2hasil)
print("Nilai Minimun    = ",cs)