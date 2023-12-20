"""Write a function, solver() to find the nth prime number?"""

import math


"""def solver(n: int):
    #This function gives the the nth prime number
    prime = []
    for i in range(2, n * n):
        count = 0
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                count += 1
                break
        if count == 0:
            if len(prime) <= n - 1:
                prime.append(i)

    return prime[-1]


if __name__ == "__main__":
    print(solver(500))"""

# optimised method


def solver(n: int):
    count = 1
    prime = 0
    i = 2
    while count <= n:
        sq_root = int(math.sqrt(i))
        flag = True
        for sq_root in range(2, sq_root + 1):
            if i % sq_root == 0:
                flag = False
                i += 1
                break
        if flag:
            count += 1
            prime = i
            i += 1
    return prime


if __name__ == "__main__":
    print(solver(10001))
