<<<<<<< HEAD
str = input()

dial = ['ABC', 'DEF', ' GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

def fun(n):
    for i in range(len(dial)):
        if n in dial[i]:
            return 3+i

ans = 0
for i in str:
    ans += fun(i)

=======
str = input()

dial = ['ABC', 'DEF', ' GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

def fun(n):
    for i in range(len(dial)):
        if n in dial[i]:
            return 3+i

ans = 0
for i in str:
    ans += fun(i)

>>>>>>> 77e016886 (Initial commit)
print(ans)