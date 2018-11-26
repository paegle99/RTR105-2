# -*- coding: utf -8 -*-


from math import sin, fabs
from time import sleep
def f(x):
    return sin(x)

a=1.1
b=3.2

funa=f(a)
funb=f(b)

if(funa*funb>0.0):
    print "Dotajaa intervalaa [%s, %s] saknju nav"%(a,b)
    sleep(1); exit()
else:
    print "Dotajaa intervalaa sakne(s) ir!"

deltax=0.01

while ( fabs(b-a) > deltax ):
    x=(a+b)/2; funx=f(x)
    if ( funa*funx<0.):
        b=x
    else:
        a=x
print "Sakne ir: ", x
print "funkcijas vertiba ir: ", sin(x)
