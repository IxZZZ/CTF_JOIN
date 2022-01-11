iXor = [16, 32, 48];
Serial = "5B 13 49 77 13 5E 7D 13"
Serial = Serial.split()
j = 0
print(Serial,len(Serial))
for i in range(len(Serial)):
    if(j>=3):
        j=0
    Serial[i] = chr(int(Serial[i],16)^iXor[j])
    j += 1

Serial="".join(Serial)
print(Serial)