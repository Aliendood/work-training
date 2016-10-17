def prime(n):
    if n <=3 and n>=1:
        return True
    sqrt=int(n*0.5)+1
    for i in range(3,sqrt,2):
        if n%i==0:
            return False
    return True

if __name__ == "__main__":
    x = int(input("enter number for n: "))
    print(prime(x))
