list1 = {1,2,3,4,5,6}

for i in range(min(list1),max(list1)+1):
    a=i
    for v in range(min(list1-{a}),max(list1-{a})+1):
        b=v
        for k in range(min(list1-{a,b}),max(list1-{a,b})+1):
            c=k
            for l in range(min(list1-{a,b,c}),max(list1-{a,b,c})+1):
                d=l
                for h in range(min(list1-{a,b,c,d}),max(list1-{a,b,c,d})+1):
                    e=h
                    for m in range(min(list1-{a,b,c,d,e}),max(list1-{a,b,c,d,e})+1):
                        f=m
                        if (a + (b - c) * d - e)*f==75 and (a!=b!=c!=d!=e!=f):
                            print("this is a:",a,i)
                            print("this is b:",b,i)
                            print("this is c:",c,i)
                            print("this is d:",d,i)
                            print("this is e:",e,i)
                            print("this is f:",f,i)
