import os

a = [1, 2, 3, 4, 5]                 # from note on slide 57
del a[1:3]		                    # a is now [1, 4, 5]
print(a)

list1 = [1, 2, 3, 4, 5]
list2 = [x*2 for x in list1]
print(list2)                        # [2, 4, 6, 8, 10]

list1 = [1, 2, 3, 4, 5]
list2 = [x*2 for x in list1 if x % 2 == 0]
print(list2)                        # [4, 8]


# -----------------------------------------------------------
# Task 1_4 revisited using a list comprehension

dir_contents = os.listdir('.')
files = [(os.path.basename(item), os.stat(item).st_size)
         for item in dir_contents if os.path.isfile(item)]

files.sort(key=lambda fileinfo: fileinfo[1], reverse=True)
for item in files:
    print('{0:<20}{1:10}'.format(*item))


def avg_temperatures(fri_temp, sat_temp, sun_temp):
    return (fri_temp + sat_temp + sun_temp) / 3


temps = [88, 92, 94]
print(avg_temperatures(*temps))
