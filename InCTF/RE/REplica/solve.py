offset = 0x00005602F16CEAF0

for i in range(12):
    ida_bytes.patch_byte(offset+i,ord('A'))

