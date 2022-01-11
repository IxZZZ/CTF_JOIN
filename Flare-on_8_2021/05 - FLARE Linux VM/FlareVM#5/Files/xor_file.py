from glob import glob

all_files = glob('*.txt.broken')

with open('all_xor_partial_key.txt', 'wb') as f:
    for i in range(len(all_files)-1):
        f.write(b'\n--------------' +
                (all_files[i]).encode('utf-8') + b'--------------\n')
        with open('key.txt', 'rb') as f1:
            with open(all_files[i], 'rb') as f2:
                f_c1 = f1.read()
                f_c2 = f2.read()
                for k in range(len(f_c1)):
                    f.write(bytes([f_c1[k] ^ f_c2[k]]))
