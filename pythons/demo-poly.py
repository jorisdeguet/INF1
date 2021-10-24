# demo de manipulation de polynomes avec numpy
import numpy

# f(x) = 3*x*x*x*x + 7*x*x*x +  1*x*x + 5*x + 1
p = numpy.poly1d([3, 7, 1, 5, 1])
print("--------------------------")
print(p)
print("--------------------------")
# q est la dérivée d'un polynôme
q = p.deriv()
print("--------------------------")
print(q)
print("--------------------------")
print(q(5))

# quand on integre, on peut fournir la valeur pour x = 0
i = p.integ(k=100)
print("--------------------------")
print(i)
print("--------------------------")
print(i(5))

rec = i.deriv()
print("--------------------------")
print(rec)
print("--------------------------")
print(rec(5))