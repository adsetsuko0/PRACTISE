def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    res=[]
    for i in range(a,b+1):
        digit=list(map(int,str(i)))
        s=sum(d**(i+1) for i,d in enumerate(digit))
        if s==i:
            res.append(i)
    return res

r=sum_dig_pow(1,100)
print(r)