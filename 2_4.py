from Crypto.Cipher import AES
from Crypto.Util import Counter

def strxor(a, b):     
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def main():
	ctext = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'
	key = '36f18357be4dbd77f050515c73fcf9f2'
	block_lenth = 16
	ctext_hex = ctext.decode('hex')
	key_hex = key.decode('hex')
	iv = ctext_hex[:block_lenth]
	ctext_r = ctext_hex[block_lenth:]
	ctr = Counter.new(block_lenth*8,initial_value=long(iv.encode('hex'),16))
	result = AES.new(key_hex,AES.MODE_CTR,counter=ctr).decrypt(ctext_r)
	print(result)

if __name__ == '__main__':
	main()
