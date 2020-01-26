""" 
Scalar types in python 
int : arbitary unlimited precision integer
float : 64 bit 
NoneType : null object
bool : True / False
"""

print 10
"""binary""" 
print 0b10  
"""octa""" 
print 0o10 
"""hexadecimal"""
print 0x10  
print int(3.5)
print int(-3.5)
print (int("465"))
print 3e8
print (float("nan"))
print (float("inf"))
print (float("-inf"))

a = None
print (a)
print (a is None)

"""0 is falsey , empty string is falsy"""

print (bool(0))
print (bool([]))
print (bool(""))
print (bool(0.0000))
"""anything other than 0 is truthy """
print (bool(-1.90))
print (bool(31))
print (bool("sss"))
