import re
greedyRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyRegex.search('HaHaHaHaHa')
print(mo1.group())

nonGreedyRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyRegex.search('HaHaHaHaHa')
print(mo2.group())