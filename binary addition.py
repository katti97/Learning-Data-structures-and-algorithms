#Given 2 binary strngs add them and return their input sum

a = '1010'
b = '1011'

length = len(a)-len(b)

if length>0:
	b = '0'*length+b
elif length<0:
	a = '0'*abs(length)+a
a = '0b'+a
b = '0b'+b
print(bin(int(a,2)+int(b,2)).replace('0b',''))