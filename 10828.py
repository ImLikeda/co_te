import sys

a = int(input())
l = []

for i in range(a):
    n = sys.stdin.readline().split()

    if n[0] == "push":
           l.append(n[1])

    elif n[0] == "pop":
        if len(l) > 0:
            print(l.pop(0))
        else:
            print(-1)

    elif n[0] == "size":
        print(len(l))

    elif n[0] == "empty":
        if len(l) == 0:
            print(1)

        else:
            print(0)

    elif n[0] == "front":
        if len(l) == 0:
            print(-1)

        else:
            print(l[0])

    elif n[0] == "back":
        if len(l) == 0:
            print(-1)

        else:
            print(l[-1])