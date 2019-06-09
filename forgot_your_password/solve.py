from z3 import *
solver = Solver()
s = [BitVec('s%i' % i, 128) for i in range(2)]
flag = 'hsctfissocoolwow'
flag1 = int(flag[:-8][::-1].encode('hex'),16)
flag2 = int(flag[8:][::-1].encode('hex'),16)

def o(x,k):
	return x<<k
def m(a):
	return a&0xffffffffffffffff
def next():
	b = m(s[0]+s[1])
	h()
	return m(b)
def p(k, x):
	return x>>(64-k)
def x(b, a):
	return a^b
def oro(a, b):
	return a|b
def h():
	s1 = m(x(s[0],s[1]))
	s[0] = m(x(oro(o(s[0],55),p(55,s[0])),x(s1,(o(s1,14)))))
	s[1] = m(oro(o(s1,36),p(36,s1)))

next()
next()
next()
next()
next()
next()
solver.add(next() == flag1)
solver.add(next() == flag2)
print solver.check()
print solver.model()