from Crypto.Cipher import AES					 
from base64 import b64decode
import hashlib


def main():
	ctext = b64decode('9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI')
	key = hashlib.sha1('12345678<811101821111167').hexdigest()
	key = bytearray.fromhex(key[:32]+'00000001')
	key = hashlib.sha1(key).hexdigest()
	real_key = key[:32]
	key = 'ea8645d97ff725a898942aa280c43179'
	block_lenth = 16
	key_hex = key.decode('hex')
	iv = chr(0)*16
	obj = AES.new(key_hex,AES.MODE_CBC,iv)
	result = obj.decrypt(ctext)
	print(result)

if __name__ == '__main__':
	main()
