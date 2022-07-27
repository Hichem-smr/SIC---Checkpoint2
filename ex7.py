from math import sqrt

c = 50
h = 30
list = input("Numbers should be separrated by comma\n")
l = list.split(",")
for element in l:
    if(element.isdigit()):
        d = int(element)
        q=sqrt((2*c*d)/h)
        print("D = ",d, "\nresult is :",q)
    else:
        print("The element",element,"is not a numbers")
