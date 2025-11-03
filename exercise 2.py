x=int(input("enter the temperature you want to convert in fahrenheit:"))
y=input("enter the first letter of to what unit you want to change it:")
if y=="c":
	print(x*1.8+32,"c")
elif y=="k":
	print(x*1.8+32+273.15,"k")
else: print(y,"f")
    