<<<<<<< HEAD
import sys

a = sys.stdin.readline().rstrip()
lst = a.split('-')

for i in range(len(lst)):
    lst[i] = list(map(int, lst[i].split('+')))
    lst[i] = sum(lst[i])

for i in range(len(lst)):
    if i == 0:
        lst[i] = lst[i]
    else:
        lst[i] = lst[i-1] - lst[i]

=======
import sys

a = sys.stdin.readline().rstrip()
lst = a.split('-')

for i in range(len(lst)):
    lst[i] = list(map(int, lst[i].split('+')))
    lst[i] = sum(lst[i])

for i in range(len(lst)):
    if i == 0:
        lst[i] = lst[i]
    else:
        lst[i] = lst[i-1] - lst[i]

>>>>>>> 77e016886 (Initial commit)
print(lst[-1])