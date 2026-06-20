#type conversion are of two types implicit and explicit



#implicit type conversion
a=2
b=4.25
sum=a+b      #2.0+42.25=6.25
print(sum)



a="2"
b=4.25
#sum=a+b      #error because we cannot add string and float



#instead we can convert string to float or int(#typecasting)
a=int("2")
b=4.25
print(type(a))
print(a+b)        #6.25
