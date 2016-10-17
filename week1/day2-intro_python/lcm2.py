def gcf(x,y):

    while(y!=0):
        x,y = y, x % y
    return x

def lcm2(x,y):
    lcm = (x*y)//gcf(x,y)
    return lcm

if __name__ == "__main__":
    x,y = int(input("enter first number ")),int(input("enter second number "))
    print(lcm2(x,y))
