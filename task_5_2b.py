#!/usr/bin/python3.7

from sys import argv

print(argv[1])
print(argv[2])

ip = list(argv[1].split('.'))

mask_b = "1" * int(argv[2]) + "0" * (32 - int(argv[2]))

ip_b = str(bin(int(ip[0]))) + str(bin(int(ip[1]))) + str(bin(int(ip[2]))) + "0" * 4
ip_b = ip_b.replace('0b', '0000')

print(f'''
Network:
{int(ip[0]):<8} {int(ip[1]):<8} {int(ip[2]):<8} {0:<8}
{ip_b[0:8]:<08} {ip_b[8:16]:<08} {ip_b[16:24]:<08} {ip_b[24:31]:<08}
''')

print('Mask:\n' +
'/' + argv[2])
print(f'''
{int(mask_b[0:8], 2):<8} {int(mask_b[8:16], 2):<8} {int(mask_b[16:24], 2):<8} {int(mask_b[24:31], 2):<8}
{int(mask_b[0:8]):<08} {int(mask_b[8:16]):<08} {int(mask_b[16:24]):<08} {int(mask_b[24:31]):<08}
''')
