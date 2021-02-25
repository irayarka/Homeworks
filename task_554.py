from math import sqrt, ceil


def gcd(a, b):
    """
    Returns greatest common divisor of a and b
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def pythagorean_triples(num):
    """
    Finds triples using Euclid's formula
    (Modified to print not only primitive triples)
    """
    for m in range(2, ceil(sqrt(num))):
        for n in range(1, m):
            # m and n are coprime and not both odd
            if gcd(m, n) == 1 and (m - n) % 2 and (m ** 2 + n ** 2) < num:
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                if a > b:
                    a, b = b, a
                k = 1
                while k * c < num:
                    print(k * a, k * b, k * c)
                    k += 1


num = int(input())
pythagorean_triples(num + 1)
