<<<<<<< HEAD
n = int(input())

lst = []
for i in range(n+1):
    if i <= 1:
        lst.append(i)
    elif i > 1:
        lst.append(int(lst[i-2]+int(lst[i-1])))

=======
n = int(input())

lst = []
for i in range(n+1):
    if i <= 1:
        lst.append(i)
    elif i > 1:
        lst.append(int(lst[i-2]+int(lst[i-1])))

>>>>>>> 77e016886 (Initial commit)
print(lst[-1])