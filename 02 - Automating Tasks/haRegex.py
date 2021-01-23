import re
haRegex = re.compile(r'(Ha){1,3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('HaHa')
print(mo2 == None)