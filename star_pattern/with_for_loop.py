#star pattern with for loop

n = int(input("enter the number of rows:\n"))
x = int(input("enter 1 for right pattern or 0 for left pattern:\n"))
r = 0

if x == 1:
    for r in range(n+1):
        print(r*"*")

elif x == 0:
    for t in reversed(range(n+1)):
        print(t*"*")
