def pythagorean_triples(n):
    """
    function takes n as an argument and returns the
    number of pythagorean triples from 1 to n.
    """
    counter = 0
    for i in range(1, n + 1):
        a = i * i
        for j in range(i, n + 1):
            b = j * j
            for k in range(1, n + 1):
                c = k * k
                if c == a + b and a <= b <= c:
                    counter += 1
                    # print(i, j, k)
    return counter


n = int(input())    # getting input data
print(pythagorean_triples(n))   # printing the result
