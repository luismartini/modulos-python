'''
Datas e horas
'''
from datetime import datetime, timedelta

#Criar uma data - strptime(str, fmt)
#.strftime(fmt)
#.timestamp
#.fromtimestemp()

d1 = datetime.strptime('14/07/1977 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('19/07/1977 22:33:00', '%d/%m/%Y %H:%M:%S')

print(d1 != d2)