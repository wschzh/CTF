from gmpy2 import powmod, gcd

# from util.timeout import timeout


def pollard(N):
    a = 2
    n = 2
    try:
        while True:
            a = powmod(a, n, N)
            p = gcd(a-1, N)
            if p != 1 and p != N:
                return p
            n += 1
    except TimeoutError:
        return


def attack(n):
    return pollard(n)


if __name__ == '__main__':
    print(attack(10*1024+7))