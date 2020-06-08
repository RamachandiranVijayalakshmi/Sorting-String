def inputstring(a):
    print("The original string is :",a)
    print("arranging characters giving precedence to lowercase letters:")
    d=sorted(a,key=lambda b:b.casefold())
    print(''.join(d))
    b=[]
    c=[]
    for i in a:
        if i.islower():
          b.append(i)
        else:
          c.append(i) 
    print("arranging characters giving precedence to lowercase letters:")
    print(''.join(b+c))
inputstring('WeLcoMe')  


