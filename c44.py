
import itertools
import re
import hashlib

def invmod(a, n):
    t = 0
    newt = 1
    r = n
    newr = a
    while newr != 0:
        q = r // newr
        (t, newt) = (newt, t - q * newt)
        (r, newr) = (newr, r - q * newr)
    if r > 1:
        raise Exception('unexpected')
    if t < 0:
        t += n
    return t

def hash(message):
    sha1 = hashlib.sha1()
    sha1.update(message)
    digest = sha1.digest()
    return int.from_bytes(digest, byteorder='big')

def getMessage(messageLines):
    msg = re.match('^msg: (.*)', messageLines[0]).group(1).encode('ascii')
    m = int(re.match('^m: (.*)', messageLines[3]).group(1), 16)
    H = hash(msg)
    if m != H:
        raise Exception(hex(H) + ' != ' + hex(m))
    s = int(re.match('^s: (.*)', messageLines[1]).group(1))
    r = int(re.match('^r: (.*)', messageLines[2]).group(1))
    return (msg, s, r, m)

def extractKey(H, r, s, k, pub):
    (p, q, g, y) = pub
    rInv = invmod(r, q)
    return (rInv * (s * k - H)) % q

def areValidKeys(pub, priv):
    (p, q, g, y) = pub
    x = priv
    return y == pow(g, x, p)

def getMessages():
    lines = list(open('44.txt', 'r').readlines())
    messageLines = [lines[4*i:4*i+4] for i in range(len(lines) // 4)]
    return [getMessage(x) for x in messageLines]

def checkForCommonK(pub, msg1, msg2):
    (p, q, g, y) = pub
    (_, s1, r1, m1) = msg1
    (_, s2, r2, m2) = msg2
    ds = (s1 - s2) % q
    dm = (m1 - m2) % q
    dsInv = invmod(ds, q)
    k = (dm * dsInv) % q
    priv1 = extractKey(m1, r1, s1, k, pub)
    priv2 = extractKey(m2, r2, s2, k, pub)
    if priv1 == priv2 and areValidKeys(pub, priv1) and areValidKeys(pub, priv2):
        return (k, priv1)
    return (None, None)

def breakRepeatedK(pub, messages):
    for pr in itertools.combinations(messages, 2):
        (msg1, msg2) = pr
        (k, priv) = checkForCommonK(pub, msg1, msg2)
        if k:
            return (k, priv)
    return (None, None)

def verifySignatureHash(H, signature, pub):
    (r, s) = signature
    (p, q, g, y) = pub
    if r <= 0 or r >= q or s <= 0 or s >= q:
        return False
    w = invmod(s, q)
    u1 = (H * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r

if __name__ == '__main__':
    (p, q, g) = (0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1, 0xf4f47f05794b256174bba6e9b396a7707e563c5b, 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291)
    y = 0x2d026f4bf30195ede3a088da85e398ef869611d0f68f0713d51c9c1a3a26c95105d915e2d8cdf26d056b86b8a7b85519b1c23cc3ecdc6062650462e3063bd179c2a6581519f674a61f1d89a1fff27171ebc1b93d4dc57bceb7ae2430f98a6a4d83d8279ee65d71c1203d2c96d65ebbf7cce9d32971c3de5084cce04a2e147821
    messages = getMessages()
    pub = (p, q, g, y)
    k, priv = breakRepeatedK(pub, messages)
    print('nonce='+str(k)+'\nprivkey='+str(priv))
    expectedHashPriv = 0xca8f6f7c66fa362d40760d135b763eb8527d3d52
    hashPriv = hash(hex(priv)[2:].encode('ascii'))
    if hashPriv != expectedHashPriv:
        raise Exception(str(hashPriv) + ' != ' + str(expectedHashPriv))
    print('RIGHT KEY')
    for msg in messages:
        (_, s, r, m) = msg
        if not verifySignatureHash(m, (r, s), pub):
            raise Exception('unexpected')
