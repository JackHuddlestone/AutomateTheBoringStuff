import re 

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures Of Batwoman')
print(mo1.group())
# Prints Batwoman

mo2 = batRegex.search('The Adventures Of Batwowowowoman')
print(mo2.group())
# Prints Batwowowoman

mo3 = batRegex.search('The Adventures Of Batman')
print(mo3 == None)
# Prints True
