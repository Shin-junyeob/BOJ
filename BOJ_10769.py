<<<<<<< HEAD
import sys, re
string = sys.stdin.readline().rstrip()
smile = re.findall('\:\-\)', string)
sad = re.findall('\:\-\(', string)
if not smile and not sad:
    print('none')
else:
    if len(smile) > len(sad):
        print('happy')
    elif len(smile) < len(sad):
        print('sad')
    else:
=======
import sys, re
string = sys.stdin.readline().rstrip()
smile = re.findall('\:\-\)', string)
sad = re.findall('\:\-\(', string)
if not smile and not sad:
    print('none')
else:
    if len(smile) > len(sad):
        print('happy')
    elif len(smile) < len(sad):
        print('sad')
    else:
>>>>>>> 77e016886 (Initial commit)
        print('unsure')