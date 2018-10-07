from __future__ import print_function
import base64
ciphertext = base64.b64decode(open('6.txt', 'r').read())
def keyPerByte(n,key_len):
	keyscore = [0] *256
	for m in range(256):
		for num in range(int(len(ciphertext)/key_len)):
			if(ord(ciphertext[(n%key_len)+key_len*num])^m in range(0x40,0x7f)):
				keyscore[m] += 1
			if(ord(ciphertext[(n%key_len)+key_len*num])^m == 0x20):
				keyscore[m] += 1
			else:
				continue
	for m in range(256):
		if(keyscore[m] == max(keyscore)):
			return m
		else:
			continue

def decrypt(key_len):
	key =[0]* key_len
	for i in range(key_len):
		key[i] = keyPerByte(i,key_len)
	for num in range(int(len(ciphertext)/key_len)):
		for i in range(key_len):
			print((chr(ord(ciphertext[i+key_len*num])^key[i])),end='')
				
	

def main():
	for key_len in range(28,30):
		decrypt(key_len)



if __name__ == '__main__':
	main()