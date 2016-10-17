list1 = {1,2,3}

for i in range(min(list1),max(list1)+1):
    a=i
    print("this is i", i)
    print("This is a", a)
    print("this is min", min(list1))
    print("this is max", max(list1))
    print("this is min-1", min(list1-{a,1}))
        #print("this is max", max(list1))
