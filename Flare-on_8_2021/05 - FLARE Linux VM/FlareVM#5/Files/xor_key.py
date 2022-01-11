from glob import glob

all_files = glob('*.txt.broken')
with open('key.txt', 'rb') as f1:
    f_c1 = f1.read()
    for i in range(len(all_files)):
        with open(all_files[i], 'rb') as f2:
            
            f_c2 = f2.read()
            with open('./save/'+all_files[i], 'wb') as f:
                for k in range(len(f_c1)):
                    f.write(bytes([f_c1[k] ^ f_c2[k]]))
