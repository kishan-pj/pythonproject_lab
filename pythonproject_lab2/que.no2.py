# Wap which accepts marks of four subject and display total marks,percentage and grade.

sub_1=float(input("enter the marks in sub_1"))
sub_2=float(input("enter the marks in sub_2"))
sub_3=float(input("enter the marks in sub_3"))
sub_4=float(input("enter the marks in sub_4"))
total_marks=sub_1+sub_2+sub_3+sub_4
print(f"the total_marks is {total_marks}")
percentage=(total_marks/400)*100
print(f"the percentage is {percentage}")
if percentage>70:
    print("distinction")
elif percentage>60:
    print("first division")
elif percentage>40:
    print("pass")
elif percentage<40:
    print("fail")
