from Crypto.Random import random
import binascii
import hashlib

def areValidParams(L, N, p, q, g):
    return ((q.bit_length() == N) and
            isProbablePrime(q, 5) and
            (p.bit_length() == L) and
            isProbablePrime(p, 5) and
            ((p-1) % q == 0) and
            pow(g, q, p) == 1)

def isProbablePrime(p, n):
    for i in range(n):
        a = random.randint(1, p)
        if pow(a, p - 1, p) != 1:
            return False
    return True

def areValidKeys(pub, priv):
    (p, q, g, y) = pub
    x = priv
    return y == pow(g, x, p)

def hash(message):
    sha1 = hashlib.sha1()
    sha1.update(message)
    digest = sha1.digest()
    return int.from_bytes(digest, byteorder='big')

def signHashWithK(H, pub, priv, k):
    (p, q, g, y) = pub
    x = priv
    r = pow(g, k, p) % q
    if r == 0:
        return None
    kInv = invmod(k, q)
    s = (kInv * (H + x * r)) % q
    if s == 0:
        return None
    return (r, s)

def signHash(H, pub, priv):
    (_, q, _, _) = pub
    while True:
        k = random.randint(1, q-1)
        signature = signHashWithK(H, pub, priv, k)
        if not signature:
            continue
        return signature

def sign(message, pub, priv):
    return signHash(hash(message), pub, priv)

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

def verifySignature(message, signature, pub):
    return verifySignatureHash(hash(message), signature, pub)

def extractKey(H, r, s, k, pub):
    (p, q, g, y) = pub
    rInv = invmod(r, q)
    return (rInv * (s * k - H)) % q

def bruteForceKey(H, r, s, pub, kMin, kMax):
    for k in range(kMin, kMax):
        priv = extractKey(H, r, s, k, pub)
        if areValidKeys(pub, priv):
            return (k, priv)
    return None

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

if __name__ == '__main__':
    L = 1024
    N = 160
    p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1
    q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
    g = 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291
    message = b'Listen for me, you better listen for me now. '
    y = 0x84ad4719d044495496a3201c8ff484feb45b962e7302e56a392aee4abab3e4bdebf2955b4736012f21a08084056b19bcd7fee56048e004e44984e2f411788efdc837a0d2e5abb7b555039fd243ac01f0fb2ed1dec568280ce678e931868d23eb095fde9d3779191b8c0299d6e07bbb283e6633451e535c45513b2d33c99ea17
    r = 1105520928110492191417703162650245113664610474875
    s = 1267396447369736888040262262183731677867615804316
    pub = (p, q, g, y)
    H = hash(message)
    print(hex(H))
    k, priv = bruteForceKey(H, r, s, pub, 0, 2**16)
    print('nonce='+str(k)+'\tprivkey='+str(priv))
