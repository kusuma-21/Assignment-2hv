# import pandas as pd
# a = [1,5,7,9,12]
# Mydata = pd.Series(a)
# print(Mydata)

x=open("code_result.txt","a")
import pandas as pd

a = int(input("Enter n1:"))
b = int(input("Enter n2:"))
c = int(input("Enter n3:"))
d = int(input("Enter n4:"))
e = int(input("Enter n5:"))
k = a**2, b**2, c**2 ,d**2, e**2
z = pd.Series(k)
print(k)
print("result is :",k,file=x)
