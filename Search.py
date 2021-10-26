
import random
def midf(upper, lower):
   return int(round((upper - lower) / 2, 0))

lower = 0
upper = 1000
quit_prog = False
think = random.randrange(lower, upper)

mid = midf(upper, lower)
print(mid)

while quit_prog == False:

    if mid < think:
        print ('{} is too low'.format(mid))
        lower = mid
        mid = lower + int(round((upper - lower) / 2, 0))

    elif mid > think:
        print ('{} is too high'.format(mid))
        upper = mid
        mid = lower + int(round((upper - lower) / 2, 0))
    elif mid == think:
        print(' Correct! I guessed {} correctly, I went for {}'.format(mid, think))
        quit_prog = True


