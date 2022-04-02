from itertools import count
from gmpy2 import gcd, isqrt

from util.timeout import timeout as t_o


def mlucas(v, a, n):
    """ Helper function for williams_pp1().  Multiplies along a Lucas sequence modulo n. """
    v1, v2 = v, (v ** 2 - 2) % n
    for bit in bin(a)[3:]: v1, v2 = ((v1 ** 2 - 2) % n, (v1 * v2 - v) % n) if bit == "0" else (
        (v1 * v2 - v) % n, (v2 ** 2 - 2) % n)
    return v1


# Recursive sieve of Eratosthenes
def primegen():
    yield 2
    yield 3
    yield 5
    yield 7
    yield 11
    yield 13
    ps = primegen()  # yay recursion
    p = ps.__next__() and ps.__next__()
    q, sieve, n = p ** 2, {}, 13
    while True:
        if n not in sieve:
            if n < q:
                yield n
            else:
                next, step = q + 2 * p, 2 * p
                while next in sieve:
                    next += step
                sieve[next] = step
                p = ps.__next__()
                q = p ** 2
        else:
            step = sieve.pop(n)
            next = n + step
            while next in sieve:
                next += step
            sieve[next] = step
        n += 2


def ilog(x, b):  # greatest integer l such that b**l <= x.
    l = 0
    while x >= b:
        x /= b
        l += 1
    return l


def attack(n, timeout=60):
    with t_o(timeout):
        try:
            for v in count(1):
                for p in primegen():
                    e = ilog(isqrt(n), p)
                    if e == 0:
                        break
                    for _ in range(e):
                        v = mlucas(v, p, n)
                    g = gcd(v - 2, n)
                    if 1 < g < n:
                        return int(g), int(n // g)  # g|n
                    if g == n:
                        break
        except TimeoutError:
            pass



if __name__ == '__main__':
    print(attack(
        149767527975084886970446073530848114556615616489502613024958495602726912268566044330103850191720149622479290535294679429142532379851252608925587476670908668848275349192719279981470382501117310509432417895412013324758865071052169170753552224766744798369054498758364258656141800253652826603727552918575175830897))
