<<<<<<< HEAD
import sys
k = int(sys.stdin.readline())
stack = []
for i in range(k):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

=======
import sys
k = int(sys.stdin.readline())
stack = []
for i in range(k):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

>>>>>>> 77e016886 (Initial commit)
print(sum(stack))