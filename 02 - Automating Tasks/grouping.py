import re
phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
mo2 = phoneNumRegex.search('My number is 555-4242')

print(mo.group())
print(mo2.group())