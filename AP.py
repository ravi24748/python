def ap(a,d,l):
    while(a<=l):
        print(a)
        a=a+d

a=int(input("enter your first term of AP:  "))
d=int(input("enter diffrece of Ap:   "))
n=int(input("enter the no of terms of AP:  "))
l=a+n*d-d
print(ap(a,d,l))
