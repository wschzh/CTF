import gmpy2


def getPQ(pub, priv):
    return gmpy2.gcd(pub, gmpy2.powmod(2, pub*priv, pub)-2)


def decrypt(pub, priv, enc):
    return gmpy2.powmod(enc, priv, getPQ(pub, priv))


def attack(n, d, c):
    return decrypt(n, d, c)