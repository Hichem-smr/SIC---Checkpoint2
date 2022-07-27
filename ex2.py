x = int(input("insert number to calculate factorial\n"))
s =1
if(x<0):
    print("number is not positive !")
else: 
    for i in range(1,x+1):
        s = s*i
    print(s)