import binascii
f = open('file')
hex = f.read()
f.close()
ans = binascii.a2b_hex(hex)
print ans


_sun = open('_sun.png', 'wb')
_sun.write(ans)
_sun.close()
