#!/usr/bin/env python
enc = [0x0000002C, 0x00000021, 0x0000001E, 0x00000073, 0x00000032, 0x00000012, 0x00000072, 0x00000037, 0x00000010, 0x00000038, 0x00000038, 0x00000001, 0x0000001D, 0x0000006B, 0x00000066, 0x00000079, 0x00000079, 0x00000026]
for i in range(len(enc)):
    enc[i] ^= 0x45
key = [1, 5, 4, 2, 3, 0]
tmp = [0 for i in range(18)]
for i in range(18):
    tmp[6 * (i / 6) + key[i % 6]] = enc[i]
flag = ''
for i in range(len(tmp)):
    flag += chr(tmp[i] ^ i)

what = [0xCC, 0x22, 0x7F, 0x52, 0x52, 0x27, 0xAA, 0x48, 0x34, 0x72, 0x5F, 0xD0, 0x0F, 0x27, 0x6B, 0x39]
long_list = []
for i in range(len(what) / 4):
    long_list.append(what[4*i] << 24 | what[4*i+1] << 16 | what[4*i+2] << 8 | what[4*i+3])
long_list = long_list[::-1]

data = [0x0000001B, 0x0000005D, 0x00000042, 0x0000002B, 0x0000000D, 0x00000005, 0x00000048, 0x000000E6, 0x00000035, 0x00000016, 0x0000009E, 0x000000B5, 0x000000BB, 0x000000E3, 0x00000024, 0x0000000F, 0x00000013, 0x000000C0, 0x00000059, 0x00000096, 0x0000005A, 0x00000012, 0x0000002B, 0x000000E0, 0x0000008F, 0x00000021, 0x0000008C, 0x00000052, 0x000000DE, 0x00000092, 0x00000012, 0x00000084, 0x000000A3, 0x000000E2, 0x0000006E, 0x0000007B, 0x00000076, 0x000000A2, 0x0000000F, 0x00000051, 0x00000093, 0x000000A9, 0x00000078, 0x000000AB, 0x0000005F, 0x0000005E, 0x00000016, 0x00000082, 0x00000072, 0x00000082, 0x00000026, 0x000000D1, 0x00000026, 0x000000D4, 0x00000009, 0x000000BF, 0x00000074, 0x000000DA, 0x000000A7, 0x0000003E, 0x00000099, 0x00000002, 0x00000065, 0x000000C3, 0x000000B3, 0x000000AD, 0x000000E0, 0x0000005A, 0x000000AB, 0x0000007A, 0x00000083, 0x00000093, 0x0000003F, 0x000000A4, 0x00000011, 0x0000003D, 0x0000008E, 0x0000000D, 0x000000DF, 0x0000005A, 0x00000071, 0x00000008, 0x0000003A, 0x000000C8, 0x000000F4, 0x00000090, 0x00000016, 0x0000001B, 0x00000088, 0x000000C6, 0x00000050, 0x0000006F, 0x000000D1, 0x000000A4, 0x000000B3, 0x00000073, 0x0000007B, 0x00000082, 0x000000BF, 0x000000B2, 0x0000005F, 0x00000094, 0x000000DE, 0x000000CA, 0x0000005A, 0x0000005E, 0x000000AB, 0x00000025, 0x000000BE, 0x0000008C, 0x0000001B, 0x00000080, 0x00000065, 0x0000009E, 0x000000EC, 0x0000005A, 0x00000037, 0x0000002A, 0x00000075, 0x0000002C, 0x0000002D, 0x000000BA, 0x00000056, 0x000000D0, 0x000000BA, 0x0000003A, 0x000000B6, 0x00000094, 0x00000081, 0x00000070, 0x00000087, 0x00000075, 0x0000003D, 0x00000048, 0x00000063, 0x0000007D, 0x00000052, 0x00000081, 0x00000039, 0x000000B5, 0x00000023, 0x000000D4, 0x000000D3, 0x000000DD, 0x0000004B, 0x000000D9, 0x000000B8, 0x00000035, 0x000000A3, 0x000000CA, 0x00000040, 0x00000077, 0x00000052, 0x0000007C, 0x0000009E, 0x0000006C, 0x00000042, 0x000000D8, 0x00000053, 0x0000006F, 0x000000EA, 0x0000002E, 0x0000000C, 0x0000009A, 0x000000F3, 0x0000002A, 0x0000006A, 0x000000D5, 0x000000EA, 0x0000006B, 0x00000093, 0x0000002F, 0x00000018, 0x0000005C, 0x000000BE, 0x00000096, 0x000000B4, 0x00000026, 0x0000000F, 0x000000DB, 0x0000009F, 0x00000007, 0x00000030, 0x000000AF, 0x00000093, 0x00000034, 0x00000027, 0x0000008E, 0x0000000A, 0x000000CA, 0x00000053, 0x000000B7, 0x000000C9, 0x0000008F, 0x0000009B, 0x00000040, 0x00000087, 0x00000054, 0x00000050, 0x00000053, 0x0000001E, 0x00000055, 0x00000006, 0x00000004, 0x00000087, 0x000000C9, 0x0000005E, 0x00000078, 0x000000A0, 0x0000003F, 0x00000066, 0x00000008, 0x000000B0, 0x00000009, 0x0000006E, 0x00000083, 0x000000E5, 0x0000006C, 0x00000023, 0x000000E6, 0x00000074, 0x00000083, 0x00000001, 0x000000A4, 0x0000007F, 0x00000062, 0x00000039, 0x00000009, 0x00000094, 0x00000032, 0x000000D3, 0x00000088, 0x00000093, 0x00000061, 0x000000C2, 0x000000C6, 0x00000061, 0x0000006B, 0x00000028, 0x000000C7, 0x00000061, 0x000000DD, 0x000000DB, 0x00000090, 0x000000A9, 0x000000D5, 0x000000D8, 0x0000008A, 0x000000A4, 0x000000A0, 0x00000065, 0x000000C1, 0x00000035, 0x00000041, 0x000000BA, 0x000000CF, 0x0000004A, 0x00000047, 0x000000CA, 0x000000AF, 0x00000051, 0x000000E1, 0x00000072, 0x0000005A, 0x000000BF, 0x0000001E, 0x000000B3, 0x0000007A, 0x00000080, 0x000000F2, 0x0000007A, 0x000000CB, 0x00000025, 0x000000E6, 0x00000098, 0x00000096, 0x0000001B, 0x00000053, 0x00000044, 0x000000D8, 0x0000003C, 0x000000AC, 0x00000012, 0x000000B1, 0x00000064, 0x00000047, 0x00000035, 0x00000000, 0x000000FF, 0xFFFFFFFF, 0xFFFFFFFF]
print len(data)

def ror(x, r):
    return ((x >> r) | (x << (32 - r))) & 0xFFFFFFFF

def rol(x, r):
    return ((x << r) | (x >> (32 - r))) & 0xFFFFFFFF

def func(idx):
    v1 = (data[idx >> 24] << 24) | (data[idx >> 16 & 0xFF] << 16) | (data[idx >> 8 & 0xFF] << 8) | data[idx & 0xFF]
    v2 = ror(v1, 6) & 0xFFFFFFFF
    v3 = ror(v1, 8) ^ v2 & 0xFFFFFFFF
    v4 = rol(v1, 10) ^ v3 & 0xFFFFFFFF
    return v4 ^ rol(v1, 12) & 0xFFFFFFFF

for i in range(30):
    idx = (long_list[i + 1] ^ long_list[i + 2] ^ long_list[i + 3]) & 0xFFFFFFFF
    long_list.append(long_list[i] ^ func(idx) & 0xFFFFFFFF)
print [hex(e) for e in long_list]

long_list = long_list[::-1]
l = []
for i in range(4, 8):
    l.append(long_list[i] & 0xFF)
    l.append(long_list[i] >> 8 & 0xFF)
    l.append(long_list[i] >> 16 & 0xFF)
    l.append(long_list[i] >> 24)

plus = ''
for i in range(len(l)):
    plus += chr(l[i])
flag = 'UNCTF{' + plus + '-' + flag + '}'
print flag
