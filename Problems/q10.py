# Pow(X,n)
"""
we have - pow(x,n) --- x^n

idea (2 was used):
1. Recurrance relation
    pow(x,n) = { 1            ; if n ==0
                 x*pow(x,n-1) ; if n>0
                }

    Will overflow recursion depth for large n

2. Recurrance relation
    pow(x,n) = {
                1 ; if n ==0
                pow(x*x,n/2) ; if n%2==0
                x*pow(x,n-1) ; if n%2==1
                }
"""
import time


# method1
def power_recursion(x, n):
    if n == 0:
        return 1
    x = x*power_recursion(x, n-1)
    return x


# method2
def power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(x*x, n/2)
    if n % 2 == 1:
        return x*power(x, n-1)


if __name__ == "__main__":
    x, n = 2, 2147
    # start = time.time()
    # pw = power_recursion(x, n)
    # end = time.time()
    # method1_time = end-start
    # print(f"{x}^{n} = {pw} ... using method 1 took:{method1_time}")
    start = time.time()
    if n < 0:
        n = abs(n)
    pw = power(x, n)
    if n < 0:
        pw = 1/pw
    end = time.time()
    method2_time = end -start
    print(f"{x}^{n} = {pw} ... using method 2 took:{method2_time}")