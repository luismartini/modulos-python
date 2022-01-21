from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays  

setlocale(LC_ALL, 'pt_BR.utf-8')

'''
dt = datetime.now()
formatação1 = dt.strftime('%A, %d de %B de %Y')
formatação2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatação1)
print(formatação2)
'''
dt = datetime.now()
mes_atual = int(dt.strftime('%m'))

print(mes_atual, mdays[mes_atual])

