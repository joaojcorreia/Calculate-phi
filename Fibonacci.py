import decimal
import time

print ('Please input the number of decimal spaces')
dec = int(input())

decimal.getcontext().prec = dec

Gold = decimal.Decimal(4)
oldGold = decimal.Decimal(0)
i = 1
a = 0
b = 1
oldb = 1

with open ('PHI_logs/' + time.strftime("%Y%m%d-%H%M") + '.txt','w+') as text_file:
    print('Fibonacci', file=text_file)
    print('decimal Spaces: ', dec, file=text_file)
    print('start time: ', time.strftime("%Y%m%d-%H%M%S" ), file=text_file)
    while Gold != oldGold:
        
        oldb = b
        oldGold = Gold

        b = a + b
        a = oldb  

        Gold = decimal.Decimal(decimal.Decimal(b)/decimal.Decimal(a))
        
        i += 1 
        
    
    print('end time: ', time.strftime("%Y%m%d-%H%M%S"), file=text_file)
    print('interactions: ', (i), file=text_file)
    print('Golden Ratio: ', (Gold), file=text_file)

print('DONE')
