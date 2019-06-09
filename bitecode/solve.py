import re
text = open("bite.java").read()
text = re.findall("v0\[[0-9]+\] \^ [0-9-]+\) \- [0-9-]+",text)
v0 = [0 for i in range(28)]
for i,t in enumerate(text):
	exec("v0[%i] = chr(" % (i) + t.replace(") -",' ^') + ")")
print ''.join(v0)