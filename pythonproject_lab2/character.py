# if name is less than 3 character long-name must be at least 3 charcters otherwise if
# it's more than
# 50 character - name must be minimum of 50 character otherwise-name looks good !

name=str(input("enter the name: "))
if (len(name)) <= 3:
    print(" The name must be 3 character")
elif len(name) >= 50:
    print("The name must be less or equal to 50 character")
else:
    print("the name is good")