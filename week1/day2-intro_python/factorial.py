"""returns factoiral"""
if __name__ == '__main__':
    x = int(input("enter number: "))

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    print(factorial(x))
