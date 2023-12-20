"""By listing the first six prime numbers: 2, 3, 5, 7, 11, 
    and 13, we can see that the 6th prime is 13.
    What is the 10,001st prime number?"""
import math

# method -1

"""def answer(n):
    This function gives the the 10,001st prime number
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
    print(answer(10001))"""

# optimised method


def answer(n):
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
    print(answer(10001))
