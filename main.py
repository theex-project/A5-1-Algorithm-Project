from random import randint
import time
from collections import deque

def randomInput(clock_type):
    randomClock=0
    counter=0
    if (clock_type=="session_key"):
        randomClock = randint(0,(2**65)-1)
        randomClock = "{0:{fill}64b}".format(randomClock, fill='0')
    elif (clock_type=="frame_counter"):
        randomClock = randint(0,(2**23)-1)
        randomClock = "{0:{fill}22b}".format(randomClock, fill='0')
    else:
        print "Access Denied!"

    return randomClock

def tappedBit(shift_register):
    result = []
    if (shift_register=="lfsr1"):
        result = [13,16,17,18]
    elif (shift_register=="lfsr2"):
        result = [20,21]
    elif (shift_register=="lfsr3"):
        result = [7,20,21,6]
    else:
        print "Access Denied!"

    return result

def stepOneTwo(lfsr,tapped_bit,key):
    lfsr = deque(lfsr)
    for num in range(0,len(key)):
        if len(tapped_bit)==4:
            resultXorLfsr = ((int(lfsr[tapped_bit[3]]) ^  int(lfsr[tapped_bit[2]])) ^ int(lfsr[tapped_bit[1]])) ^  int(lfsr[tapped_bit[0]])
        else:
            resultXorLfsr = int(lfsr[tapped_bit[1]]) ^  int(lfsr[tapped_bit[0]])

        resultFinal = int(key[num]) ^ resultXorLfsr
        lfsr.rotate(1)
        lfsr[0] = str(resultFinal)
        # Validation Item
        # print "loop-"+str(num)
        # result = ''.join(lfsr)
        # print result

    return lfsr

# Main Program

lfsr1 = "{0:{fill}19b}".format(0, fill='0')    #19bit
lfsr2 = "{0:{fill}22b}".format(0, fill='0')    #22bit
lfsr3 = "{0:{fill}23b}".format(0, fill='0')    #23bit

print "A5/1 Algorithm\n"
# Inisialisasi LFSR
print "LFSR initiating...\n"
time.sleep(1)
print lfsr1
print lfsr2
print lfsr3

# Generating Tapped Bit
print "\nTapped Bit generating...\n"
time.sleep(3)
print "LFSR 1 : "+str(tappedBit("lfsr1"))
print "LFSR 2 : "+str(tappedBit("lfsr2"))
print "LFSR 3 : "+str(tappedBit("lfsr3"))
print "\nStep 1\n"

# Pembuatan session key secara random
print "Creating Session Key...\n"
time.sleep(3)
sessionKey = randomInput("session_key")
print "Session Key Created : "+str(sessionKey)+" \n"
sessionKey = deque(sessionKey)

# XOR-ing session key dengan lfsr menggunakan tapped bit
print "XOR-ing between session key and LFSR with tapped bit\n"
time.sleep(3)
lfsr1 = stepOneTwo(lfsr1, tappedBit("lfsr1"), sessionKey)
print "XOR-ing result on lfsr 1 : "+''.join(lfsr1)
time.sleep(1)
lfsr2 = stepOneTwo(lfsr2, tappedBit("lfsr2"), sessionKey)
print "XOR-ing result on lfsr 2 : "+''.join(lfsr2)
time.sleep(1)
lfsr3 = stepOneTwo(lfsr3, tappedBit("lfsr3"), sessionKey)
print "XOR-ing result on lfsr 3 : "+''.join(lfsr3)
time.sleep(3)
print "\nStep 2\n"

# Pembuatan frame counter secara random
print "Creating Frame Counter...\n"
time.sleep(1)
frameCounter = randomInput("frame_counter")
print "Frame Counter Created : "+frameCounter+" \n"
frameCounter = deque(frameCounter)

# XOR-ing frame counter dengan lfsr pada step1 menggunakan tapped bit
print "XOR-ing between frame counter and LFSR with tapped bit\n"
time.sleep(3)
lfsr1 = stepOneTwo(lfsr1, tappedBit("lfsr1"), frameCounter)
print "XOR-ing result on lfsr 1 : "+''.join(lfsr1)
time.sleep(1)
lfsr2 = stepOneTwo(lfsr2, tappedBit("lfsr2"), frameCounter)
print "XOR-ing result on lfsr 2 : "+''.join(lfsr2)
time.sleep(1)
lfsr3 = stepOneTwo(lfsr3, tappedBit("lfsr3"), frameCounter)
print "XOR-ing result on lfsr 3 : "+''.join(lfsr3)
time.sleep(3)
print "\nStep 3\n"
