
from Crypto.Cipher import AES

def strxor(a, b):     
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def main():
	ctext = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
	key = '140b41b22a29beb4061bda66b6747e14'
	block_lenth = 16
	ctext_hex = ctext.decode('hex')
	key_hex = key.decode('hex')
	ctext_block = [ctext_hex[i:i+block_lenth] for i in range(0,len(ctext_hex),block_lenth)]
	block_num = len(ctext_block)
	result = ''
	for i in range(block_num-1):
		ptext_block_p = AES.new(key_hex,AES.MODE_ECB).decrypt(ctext_block[i+1])
		ptext_block_l = strxor(ptext_block_p,ctext_block[i])
		result += ptext_block_l
	padding_num = ord(result[-1])
	result = result[:-padding_num]
	print(result)


if __name__ == '__main__':
	main()
