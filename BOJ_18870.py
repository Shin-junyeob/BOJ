<<<<<<< HEAD
import sys

n = int(sys.stdin.readline())
lst = [int(x) for x in sys.stdin.readline().split()]
lst2 = sorted(list(set(lst)))

dic = {}
for i in range(len(lst2)):
    dic[lst2[i]] = i

for i in lst:
=======
import sys

n = int(sys.stdin.readline())
lst = [int(x) for x in sys.stdin.readline().split()]
lst2 = sorted(list(set(lst)))

dic = {}
for i in range(len(lst2)):
    dic[lst2[i]] = i

for i in lst:
>>>>>>> 77e016886 (Initial commit)
    print(dic[i], end = ' ')