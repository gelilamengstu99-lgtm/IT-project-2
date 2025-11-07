h=int(input("enter 1 if you want to convert a temperature and press 2 if you want to convert length:"))
if h==1:
	x=int(input("enter the temperature you want to convert in fahrenheit:"))
	y=input("enter the first letter of to what unit you want to change it:")
	if y=="c":
		print(x*1.8+32,"c")
	elif y=="k":
		print(x*1.8+32+273.15,"k")
	else: print(y,"f")
elif h==2:
	z=int(input("enter the length you want to convert in meter:"))
	i=str(input("enter the short form of the unit to which you want to convert it to:"))
	if i=="cm":
		print(z*100,"cm")
	elif i=="km":
		print(z%1000,"km")
	else:print(z,"m")
	