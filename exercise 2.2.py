x=int(input("enter your salary:"))
if 0<=x<=2000:
	print("your tax is 0 birr")
	print("your net salary is",x,"birr")
elif 2000<x<=4000:
	print("your tax is",x*0.15,"birr")
	print("your net salary is", x-(x*0.15),"birr")
elif 4000<x<=7000:
	print("your tax is",x*0.20,"birr")
	print("your net salary is",x-(x*0.20),"birr")
elif 7000<x<=10000:
	print("your tax is",x*0.25,"birr")
	print("your net sa;lary is",x-(x*0.25),"birr")
elif 10000<X<=14000:
	print("your tax is",x*0.30,"birr")
	print("your net salary is",x-(x*0.30),"birr")
else:print("your tax is",x*0.35,"birr and your net salary is",x-(x*0.35),"birr")
    

