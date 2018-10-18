from Crypto.Hash import SHA256

block_size = 1024
#f = open('6.2.birthday.mp4_download', 'rb')      
f = open('6.1.intro.mp4_download', 'rb')      
f.seek(0)
file = f.read()           
size = f.tell()             
last_block_size = size % block_size
index = range(0,size, block_size)
index.reverse()     
last_hash = ""
for l in index:
    f.seek(l,0)
    block = f.read(block_size)
    h = SHA256.new()
    h.update(block)
    h.update(last_hash)
    last_hash = h.digest()
print last_hash.encode('hex')
