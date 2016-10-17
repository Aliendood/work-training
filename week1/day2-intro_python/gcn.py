""" find greatest common denominator"""
from divisors import factors
def gcn(n,i):
    num1 = factors(n)
    num2 = factors(i)
    num1.reverse()
    num2.reverse()
    for k in num1:
        if k in num2:
            return k
            break

if __name__ == "__main__":
    x,y = int(input("enter first number ")),int(input("enter second number "))
    print(gcn(x,y))
