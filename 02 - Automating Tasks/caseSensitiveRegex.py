import re

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop').group())
print(robocop.search('ROBOCOP protects the innocent').group())

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Huddlestone gave the secret documents to Agent Barre'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carole that Agent Eve knew Agent Bob was a double agent.')) 