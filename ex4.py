str = input("insert your value\n")
print("insert a character to delete between : (0," , (len(str)-1) , ")")  
n = int(input())
if(n>len(str)+1 or n<0):
    print("wrong range")
else:
    print(str[:n] + str[n+1:])
