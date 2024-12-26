import sys

a = int(sys.stdin.readline())
l = []

for i in range(a):
    n = sys.stdin.readline().split()

    if len(n) == 2:
        l.append(n[1])

    elif n[0] == 'pop':
        if len(l) > 0:
            print(l[-1])
            l.pop()

        else:
            print(-1)

    elif n[0] == 'size':
        print(len(l))

    elif n[0] == 'empty':
        if len(l) == 0:
            print(1)

        else:
            print(0)

    elif n[0] == 'top':
        if len(l) > 0:
            print(l[-1])

        else:
            print(-1)
