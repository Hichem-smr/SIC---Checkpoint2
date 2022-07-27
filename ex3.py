dict = {}
n = int(input("input your limits for dictionnary\n"))
if(n>0):
    for i in range(1,n+1):
        dict[i] = i*i
    print(dict)
else:
    print("please insert a positive value\n")