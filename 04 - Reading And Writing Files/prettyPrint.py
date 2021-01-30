import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Polka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n') 
fileObj.close()