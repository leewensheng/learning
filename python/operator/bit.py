'''
左移 运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数
'''
a = 3
b = 0b00011
c = 0x00003
d = 0o003
print(a,b,c,d)
print(bin(a))
print(hex(3))
print(oct(4))

bleft = b << 1 #左移1位
bright = b >> 1 #右移1位
print('00000011 left move eq 00000110 ',bleft)
print('00000011 right move eq', bright)