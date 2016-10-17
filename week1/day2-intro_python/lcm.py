""" find least common multiple """
from divisors import factors
def lcm(n,i):
    f_num = factors(n*i)
    for k in f_num:
        if k >= max(n,i) and k % i == 0 and k % n == 0:
          return k

if __name__ == "__main__":
    x,y = int(input("enter first number ")),int(input("enter second number "))
    print(lcm(x,y))
