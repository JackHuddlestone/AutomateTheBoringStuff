import re
#batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures Of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures Of Batwowoman')
try:
    print(mo2.group())
except:
    print('I cant find Batwoman')


batRegex2 = re.compile(r'Bat(wo)*man')
mo3 = batRegex2.search('The Adventures Of Batman')
mo4 = batRegex2.search('The Adventures Of Batwoman')
mo5 = batRegex2.search('The Adventures Of Batwowowowowoman')

print(mo3.group())
print(mo4.group())
print(mo5.group())