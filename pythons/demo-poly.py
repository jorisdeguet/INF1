# demo de manipulation de polynomes avec numpy
import numpy

p = numpy.poly1d([1, 0, 1])
print("--------------------------")
print(p)
print("--------------------------")
q = p.deriv()
print("--------------------------")
print(q)
print("--------------------------")
print(q(5))