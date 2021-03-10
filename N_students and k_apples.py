# N students take K apples and distribute them among each other evenly.
# The remaining (the undivisible) part remains in the basket.
# How many apples will each single student get? How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for the questions above.

N=int(input("enter a number of students:"))
K=int(input("enter a number of apple:"))
y=K%N
z=K//N
print("apples remain in basket:",y)
print("apple gain by each student:",z)

