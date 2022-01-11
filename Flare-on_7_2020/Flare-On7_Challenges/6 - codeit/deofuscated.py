import re

with open('autoit_script.au3', 'r') as file:
    au3_source = file.read()

# deobfuscated constant
matches_const = re.finditer(
    r'(\$fl[a-z]{8})\s\=\sNumber\(\"\s([0-9]+)\s\"\)', au3_source)


# $fltnemqxvo replace by 97, ...
for m in matches_const:
    au3_source = au3_source.replace(m.groups()[0], m.groups()[1])

# deofuscated string
dlit = []

for s in re.finditer(r'\$dlit\s(\&)?\=\s\"([a-z0-9A-Z\$]{2,100})\"', au3_source):
    dlit.append(s.groups()[1])


string = ''.join(dlit)

decoded_str_arr = []
for encode in string.split('4FD5$'):
    decoded_str_arr.append(bytes.fromhex(encode).decode('utf-8'))

# print(decoded_str_arr)

for m in re.finditer(r'(arehdidxrgk\(\$os\[([0-9]+)\]\))', au3_source):
    print(m.groups())
    au3_source = au3_source.replace(
        m.groups()[0], '\"%s\"' % decoded_str_arr[int(m.groups()[1], 10)-1])


with open('autoit_script_deobf.au3', 'w') as out:
    out.write(au3_source)
