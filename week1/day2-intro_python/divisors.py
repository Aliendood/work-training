"""divisors for n"""
def factors(n):
    if (n == 0 or n == 1): # exit if 0 or 1
        return [1]
    result_small = [1] #create list for i to sqrt(n)
    result_large = [n] #create list for n/i
    result_square = [] #list for case when n is perfect square
    sqrt = int(n**0.5)
    for i in range(2,sqrt): #only iterate to sqrt(n)
        if n % i == 0:
            result_small.append(i) #add i for mod 0 result
            result_large.append(int(n/i)) #add n/i for mod 0 result
    if sqrt > 1 and n % sqrt == 0: #check for perfect square
        result_square.append(sqrt)
        if sqrt*sqrt != n: #added due to case when floor of sqrt is a factor
            result_square.append(int(n/sqrt))
    result_large.reverse() #reverse list of divsors for ordering
    return result_small + result_square + result_large #append list
if __name__ == "__main__":
    x = int(input("enter number for n: "))
    print(factors(x))
