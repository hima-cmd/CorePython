""
' read eval print loop : REPL ' 

print 2+2
print 6*7
print 9+70+234

""" print "" in py2 """
print "hi there"

""" print() required in py3 """
print ('hello')


""" python std libraries """
import math
math.sqrt(81)
print "Using help on math module"
print help(math)

""" using math built functions by importing all builtin functions."""

print "Factorial of 5 :"
print math.factorial(5)
n = 5
k = 3
print (math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))

""" also , from math import factorial  : importing specific module"""
""" from math import factorial as fac: importing specific module and renaming """
from math import factorial as fac
print (fac(n) / (fac(k) * fac(n-k)))
print ("------")
print (fac(n) // (fac(k) * fac(n-k)))
n = 100
k = 2
print (fac(n) // (fac(k) * fac(n-k)))
print (fac(n))
print (len(str(fac(n))))




