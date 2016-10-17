def series(n):
    if n==0:
        return 1
    a = 1
    total = [1]
    for i in range(1,n+1):
        a=a*2+1
        total.append(a)

    return total[n]

if __name__ == "__main__":
    x = int(input("enter number for n: "))
    print(series(x))
