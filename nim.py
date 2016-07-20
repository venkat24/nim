import random
from string import ascii_uppercase
import sys

heaps=[]
numberOfHeaps=3
maxHeapSize=20
currentPlayer=True

def displayHeap():
	print
	print '  '.join(ascii_uppercase[:numberOfHeaps])
	print '  '.join(str(x) for x in heaps)

def checkWinState(player):
	if sum(heaps)==0:
		print "GAME OVER!"
		if player:
			print "You Win!"
		else:
			print "I win"
			sys.exit()

for i in xrange(numberOfHeaps):
	heaps.append(random.randint(1,maxHeapSize))

def computerMove():
	pass

print "\nWelcome to NIM!"
while(True):
	try:
		displayHeap()
		if currentPlayer:
			print "Your move : ",
		else:
			print "My move : ",
			computerMove()
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