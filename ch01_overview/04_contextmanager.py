"""
    Before and after using the 'with' control
"""

lines = []
try:
    f = open('alice.txt')
    try:
        lines = f.readlines()
    finally:
        f.close()
except IOError as e:
    print('Handled {0}'.format(e))

print('{0} lines read.'.format(len(lines)))


lines = []
try:
    with open('alice.txt') as f:
        lines = f.readlines()
except IOError as e:
    print('Handled {0}'.format(e))

print('{0} lines read.'.format(len(lines)))
