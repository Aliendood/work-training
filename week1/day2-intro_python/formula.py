def formula(n):
    list1 = {1,2,3,4,5,6}
    for i in list1:
        a=i
        for v in set(list1-{a}):
            b=v
            for k in set(list1-{a,b}):
                c=k
                for l in set(list1-{a,b,c}):
                    d=l
                    for h in set(list1-{a,b,c,d}):
                        e=h
                        for m in set(list1-{a,b,c,d,e}):
                            f=m
                            if (a + (b - c) * d - e)*f==n and (a!=b!=c!=d!=e!=f):
                                return (a,b,c,d,e,f)

if __name__ == "__main__":
    x = int(input("enter number for n: "))
    list1 = formula(x)
    template = "{0:1}|{1:1}|{2:1}|{3:1}|{4:1}|{5:1}"
    print(template.format("A","B","C","D","E","F"))
    print(template.format("=","=","=","=","=","="))
    print(template.format(*list1))
