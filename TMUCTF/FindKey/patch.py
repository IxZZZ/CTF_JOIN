offset = 0x000055B42E233060

for i in range(16):
    ida_bytes.patch_byte(offset+i,0xff)
