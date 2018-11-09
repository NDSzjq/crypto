from Crypto.Cipher import AES

def main():
	ctext = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
	key = '140b41b22a29beb4061bda66b6747e14'
	block_lenth = 16
	ctext_hex = ctext.decode('hex')
	key_hex = key.decode('hex')
	iv = ctext_hex[:block_lenth]
	ctext_r = ctext_hex[block_lenth:]
	obj = AES.new(key_hex,AES.MODE_CBC,iv)
	result = obj.decrypt(ctext_r)
	padding = ord(result[-1])
	result = result[:-padding]
	print(result)

if __name__ == '__main__':
	main()

	
