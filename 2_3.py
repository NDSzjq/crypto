from Crypto.Cipher import AES
from Crypto.Util import Counter

def main():
	key = "36f18357be4dbd77f050515c73fcf9f2" 
	ctext = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
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
