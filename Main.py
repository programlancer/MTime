import math

cont = True

while cont:
    selector = input('select>').upper()

    if selector == 'M':
        h = int(input('hours    >'))
        m = int(input('minutes  >'))
        s = int(input('seconds  >'))

        print('Magic time is {0}'.format(h * 3600 + m * 60 + s))

    elif selector == 'T':
        time = int(input('seconds  >'))

        h = math.trunc(time / 3600)
        m = math.trunc((time - h * 3600) / 60)
        s = time - h * 3600 - m * 60

        print('Time is {0:02d}:{1:02d}:{2:02d}'.format(h, m, s))

    else:
        print('bye')
        cont = False
