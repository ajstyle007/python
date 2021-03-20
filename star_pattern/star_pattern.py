n = int(input("enter no. of rows:\n"))
t = int(input("enter 1 for right pattern or 0 for left pattern:\n"))
r = 0
y = n
x = bool(t)
if x == 1 :
    while True:

        print(r*"*")
        r = r + 1
        if r == n+1:
            break
elif x == 0:
    while True:

        print(y*"*")
        y = y - 1
        if y == 0:
            break
