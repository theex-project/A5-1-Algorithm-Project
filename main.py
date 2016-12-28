from random import randint
from collections import deque

lfsr1 = int("{0:{fill}19b}".format(0, fill='0'))    #19bit
lfsr2 = int("{0:{fill}22b}".format(0, fill='0'))    #22bit
lfsr3 = int("{0:{fill}23b}".format(0, fill='0'))    #23bit

def randomInput(clock_type):
    if (clock_type=="session_key"):
        for num in range(0,64):
            temp = randint(0,1)
            if (num==1):
                randomClock = temp
            else :
                randomClock=int(str(randomClock)+str(temp))
    elif (clock_type=="frame_counter"):
        randomClock = randint(0,(2**23)-1)
        randomClock = int("{0:{fill}22b}".format(randomClock, fill='0'))
    else:
        print "Access Denied!"

    return randomClock

def tappedBit(shift_register):
    if (shift_register=="lfsr1"):
        result = [13,16,17,18]
    elif (shift_register=="lfsr2"):
        result = [20,21]
    elif (shift_register=="lfsr3"):
        result = [7,20,21,6]
    else:
        print "Access Denied!"
        result = []

    return result

def stepOneTwo(lfsr,tapped_bit,key):
    lfsr = deque(lfsr)
    for num in range(0,len(key)):
        if len(tapped_bit)==4:
            resultXorLfsr = ((lfsr[tapped_bit[3]] ^  lfsr[tapped_bit[2]]) ^ lfsr[tapped_bit[1]]) ^  lfsr[tapped_bit[0]]
        else:
            resultXorLfsr = lfsr[tapped_bit[1]] ^  lfsr[tapped_bit[0]]

        resultFinal = key[num] ^ resultXorLfsr
        lfsr = lfsr.rotate(1)
        lfsr[0] = resultFinal
    return lfsr
