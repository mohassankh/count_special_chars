def s(x):
    def count(x,i):
        return (x).count(i)
    dic={}    
    for i in "!@#$%^&*()_+~":
        dic[i]=count(x,i)
    return(dic)
x="name #$% is ^^&*&% mohamed ?"
print(s(x))