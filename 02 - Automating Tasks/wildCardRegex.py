import re

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Jack Last Name: Huddlestone')
mo1 = nameRegex.search('First Name: Sally-Anne Last Name: Townsend')

print(mo.groups())
print(mo1.groups())