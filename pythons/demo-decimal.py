from decimal import Decimal


point1 = Decimal(0.1)
point3 = Decimal(0.3)
print(point1)
print(point3)
print(point1+point1+point1 == point3)
# quoi?


point1 = Decimal("0.1")
point3 = Decimal("0.3")
print(point1)
print(point3)
print(point1+point1+point1 == point3)
# as-tu une explication?


point1 = Decimal(1) / 10
point3 = Decimal(3) / 10
print(point1)
print(point3)
print(point1+point1+point1 == point3)