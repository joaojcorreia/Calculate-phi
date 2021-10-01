import decimal
import math
import time

print ('Please input the number of decimal spaces')
dec = int(input())

decimal.getcontext().prec = dec

a = decimal.Decimal(0)
b = decimal.Decimal(0)

u=decimal.Decimal(0)
oldu = decimal.Decimal(3)

Gold = decimal.Decimal(3)

n = int(0)

with open ('PHI_logs/' + time.strftime("%Y%m%d-%H%M") + '.txt','w+') as text_file:
    print('Method: Taylor series', file=text_file)
    print('decimal Spaces: ', dec, file=text_file)
    print('start time: ', time.strftime("%Y%m%d-%H%M%S" ), file=text_file)
    while u != oldu:
        
        
        oldu = u

        a = decimal.Decimal(decimal.Decimal((-1)**(n+1))*decimal.Decimal(math.factorial((2*n)+1)))
        b = decimal.Decimal(decimal.Decimal((4)**((2*n)+3))*decimal.Decimal(decimal.Decimal(math.factorial(n))*decimal.Decimal(math.factorial(n+2))))

        u += decimal.Decimal(a/b)

        n += 1



    Gold = decimal.Decimal(decimal.Decimal(13/8)+u)

    print('end time: ', time.strftime("%Y%m%d-%H%M%S"), file=text_file)
    print('interactions: ', (n), file=text_file)
    print('Golden Ratio: ', (Gold), file=text_file)

    print('DONE')
