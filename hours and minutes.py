# Given the integer N- the number of minutes that is passed since midnight
# how many hours and minutes are displayed on the 24th digital clock?
# the program should print two numbers:the number of hours (between 0 and 25)
# and the number of minutes (between 0 and 59)
# for example ,if N=150,then 150 minutes have since midnight -ienow is 2:30 ,so the program should print is 20


N = int(input("enter the minutes passed since midnight:"))
hours = (N//60)
minutes =(N%60)
print(f"the hours is {hours}")
print(f"the minutes is {minutes}")
print(f"Its {hours}:{minutes} now")