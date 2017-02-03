# test open special file
file = open('.\generate\GpsCoordinateExport.py','w')

import re
match = re.match('hello[\t]*(.*)world', 'hello happy world')
b=match.group(1)
print(b)