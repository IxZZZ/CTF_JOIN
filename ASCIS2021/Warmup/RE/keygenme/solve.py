offset = 0x00007FFC62A73B60

name = "Arthur Alexander"

for i in range(len(name)):
    ida_bytes.patch_byte(offset+i,ord(name[i]))

ida_bytes.patch_byte(offset+len(name),0)

