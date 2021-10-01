import decimal
import time

print ('Please input the number of decimal spaces')
dec = int(input())

decimal.getcontext().prec = dec

r5 = decimal.Decimal(2.2360679775)
oldr5 = decimal.Decimal(0)

n = int(0) 

with open ('PHI_logs/' + time.strftime("%Y%m%d-%H%M") + '.txt','w+') as text_file:
    print('Square-root of five', file=text_file)
    print('decimal Spaces: ', dec, file=text_file)
    print('start time: ', time.strftime("%Y%m%d-%H%M%S" ), file=text_file)
    while r5 != oldr5:
    
        oldr5 = r5

        r5 = decimal.Decimal(decimal.Decimal(0.5)*decimal.Decimal(r5+decimal.Decimal(5/r5)))

        n += 1
      
    Gold = decimal.Decimal(decimal.Decimal(1+r5)/decimal.Decimal(2))
        
    
    print('end time: ', time.strftime("%Y%m%d-%H%M%S"), file=text_file)
    print('interactions: ', (n), file=text_file)
    print('Golden Ratio: ', (Gold), file=text_file)

print('DONE')
