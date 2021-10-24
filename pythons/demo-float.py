# pour plus d'information https://docs.python.org/3/tutorial/floatingpoint.html

# https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
# https://fr.wikipedia.org/wiki/IEEE_754

import struct
def binary(num):
    raw = ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))
    spaced = raw[0:1] + ' ' + raw[1:9] + ' ' + raw[9:]
    return  spaced + "  :  " + str(num)



print(.1 + .1 + .1)
print(.1 + .1 + .1 == .3)

print("-------------------------------")
print(binary(0))
print(binary(0.5))
print(binary(-1.0))
print(binary(1.0))
print(binary(2))
print(binary(4))
print(binary(8))
print(binary(16))
print(binary(32))
print(binary(64))
print(binary(123456789))
print("--------------------------------")
print(binary(.1))
print(binary(.1 + .1))
print(binary(.1 + .1 + .1))

#TODO video la dessus :
# 1/3 en decimal ca donne 0.3333333333   si on fait *3 ca donne 0.999999999 donc pas 1
# ici c'est la meme chose en base 2
# 1/10 en binaire ca donne 0.