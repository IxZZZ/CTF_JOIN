strs = "1584 1776 1824 1584 1856 1632 1968 1664 768 1728 784 784 784 784 784 1520 1840 1664 784 784 784 784 784 784 816 816 816 816 816 816 1856 1856 1856 1856 1856 1520 784 1856 1952 1520 1584 688 688 528 2000"

for str in strs.split(' '):
    print(chr(int(int(str,10)/16)),end='')