'''1330번'''
a,b = input().split()
a = int(a)
b = int(b)
if(a<b):
    print("<")
elif(a>b):
    print(">")
else:
    print("==")