X = input()
Y = input()
X = int(X)
Y = int(Y)

if -1000 <= X <= 1000 and X!=0 and -1000 <= Y <= 1000 and Y!=0:
    if X>0 and Y>0:
        print(1)
    elif X<0 and Y>0:
        print(2)
    elif X<0 and Y<0:
        print(3)
    else:
        print(4)