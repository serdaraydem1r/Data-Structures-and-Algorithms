def bigon(n):
    for i in range(0,n):
        print(i)
bigon(5)

def bigon2(n):
    for i in range(0,n):
        for j in range(0,n):
            print(i,j)
bigon2(5)

def bigon3(n):
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                print(i,j,k)
bigon3(5)

import math
def logn(n):
    while n>1:
        n = math.floor(n/2)
        print(n)
logn(8)

def nlogn(n):
    limit=n
    while n>1:
        n = math.floor(n/2)
        for i in range(1,limit):
            print(i)
nlogn(8)

