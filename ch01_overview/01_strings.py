my_str = 'Python is fun'
print(my_str[0])         # 'P'

print(my_str[0:9])       # 'Python is'

print(my_str[:3])        # 'Pyt'

print(my_str[3:])        # 'hon is fun'

print(my_str[-3:])     # 'fun'


# ------------------------------------------
#        Using str.format()
#
s6 = '{lang} is over {0:0.2f} {date} old.'.format(20, date='years', lang='Python')
print(s6)


# format() examples:
print('{:>8}'.format('101.55'))                 # right-justify in a field-width of 8
print('{:-^20}'.format('hello'))                # center in a field-width of 20
