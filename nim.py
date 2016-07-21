import random
from string import ascii_uppercase
import sys

heaps=[]
numberOfHeaps=3
maxHeapSize=10
currentPlayer=True

def displayHeap():
    print
    print '  '.join(ascii_uppercase[:numberOfHeaps])
    print '  '.join(str(x) for x in heaps)

def checkWinState(player):
    player = not currentPlayer
    if sum(heaps)==0:
        print "GAME OVER!"
        if player:
            print "You Win!"
        else:
            print "I win"
        sys.exit(0)

for i in xrange(numberOfHeaps):
    heaps.append(random.randint(1,maxHeapSize))

def computerMove():
    print "My move : ",
    global numberOfHeaps
    nim_sum=reduce(lambda a,b: a^b, heaps)
    bin_nim=int("{0:b}".format(nim_sum))
    largest=heaps.index(max(heaps))
    curr_heap=0
    for i in xrange(numberOfHeaps):
        if nim_sum^heaps[i] < heaps[i] :
            curr_heap=i
            print ascii_uppercase[i] + " ",
    if bin_nim==0: #losing position, hope for opponent mistake.
        heaps[largest]-=random.randint(1,max(heaps))
    else:
        prev_val = heaps[curr_heap]
        heaps[curr_heap]^=nim_sum
        new_val=heaps[curr_heap]
        print prev_val - new_val

print "\nWelcome to NIM!"
while(True):
    displayHeap()
    if currentPlayer:
        print "Your move : ",
    else:
        computerMove()
        currentPlayer = not currentPlayer
        checkWinState(currentPlayer)
        continue
    try:
        userInputHeap,userInputNumber = raw_input().split()
        userInputNumber=int(userInputNumber)
        heapIndex=ascii_uppercase.index(userInputHeap)
        if userInputHeap not in ascii_uppercase[:numberOfHeaps]:
            raise LetterError
        if userInputNumber > heaps[heapIndex]:
            raise NumberError
    except:
        print "Enter a valid move. ( Heap, number )"
        continue
    heaps[heapIndex]-=userInputNumber
    currentPlayer = not currentPlayer
    checkWinState(currentPlayer)