'''
Game for bonus
Haunted Hospital Adventure
Hamila10
400114912
'''
# import the requisite libraries
import random 
import math
from characters import specialPics as sp # special python file import to add characters to the game
from time import sleep

# class for character
Name, favColor, favNum, stats, tool = '', '','','',''

TIME = 0.8 # time constant used for delay to provide better user experience

phrases = ["The Powerful", "The Wise", "The Magestic", "The Brave", "The Kind"] # feature to add better user experience during the game

class createCharacter(object): # define class to create the main character
	
	def __init__(self,name,favColor,favNum,tool, stats):
		self.name = name
		self.favColor = favColor
		self.favNum = favNum
		self.tool = tool

		self.itemList = [tool]
		self.stats = stats

	def getName(self): # accessor statememnt for the name
		return self.name

	def getColor(self): # accessor statement for the color
		return self.favColor

	def getNum(self): # accessor statement for the number
		return self.favNum

	def getTools(self): # accessor statement for the tools in the charaters bag
		return self.itemList

	def getStats(self): # accessor statement for the charaters fight stats
		return self.stats

	def UserInformation(self): # method to display all of the users inforation and fight stats
		print('============================= Character Summary=============================')
		first = 'Character Name: ' + self.getName() + ' '+phrases[self.getStats()["phraseNumber"]] + '\n'
		second = 'Favourite Number: ' + str(self.getNum()) + '\n'
		third = 'Favourite Color: ' + self.getColor() + '\n'
		fourth = 'In your bag you have: ' + '\n'
		for i in range(len(self.getTools())):
			fourth += '\t- a ' + str(self.getTools()[i]) + '\n'

		fifth = 'Here are some of your stats: ' + '\n'
		fifthA = '\t- Strength (max:150): ' + str(self.getStats()["physicalAttributes"]["strength"]) + '\n'
		fifthB = '\t- Speed (max:100): ' + str(self.getStats()["physicalAttributes"]["speed"]) + '\n'
		fifthC = '\t- Wit (max: 200): ' + str(self.getStats()["physicalAttributes"]["wit"]) + '\n'
		fifthD = '\t- Height: ' + self.getStats()["Height"] + '\n'
		fifthE= '\t- Age: ' + str(self.getStats()["Age"]) + '\n'

		print('\n',first,second,third,fourth,fifth, fifthA, fifthB, fifthC, fifthD, fifthE)

class createGhostBoss(object): # create class for the ghost boss

	def __init__(self):
		self.strength = random.randint(0,80) # incorporates random module for for the strength charactersitic
		self.speed = random.randint(0,3) # incorporates random module for for the speed charactersitic

	def ghostStrength(self): # accessor statement for ghost strength
		return self.strength
	def ghostSpeed(self): # accessor statement for ghost speed
		return self.speed

def plusMinus(num): # define a generic function to determine in when used randomly, if the number is increasing or decreasing
	sign = random.randint(0,1)
	if sign == 0:
		return num*-1
	else:
		return num

#===========================================# Get Data Section ===========================
# this sections deals with the use of the data previosuly generated

def Start(): # this defines the start function
	# sets up the character generation and then calls the character class
	# incorporates many sleep(time)'s to imporve user experience, make it fell like retro game
	global Name, favColor, stats, tool, favNum
	# Print introduction
	Name = input('What would you like your character\'s name to be? ')
	colors = ['Red', 'Blue', 'Green', 'Magenta', 'Auburn', 'Fuschia', 'Black']
	colorsString = '1) Red 2) Blue 3) Green 4) Magenta 5) Auburn 6) Fuschia 7) Black'
	sleep(TIME)
	print(colorsString)
	sleep(TIME)
	favColNum = input('Please Enter the number corresponding to your favourite color: ')
	sleep(TIME)
	favColor = colors[int(favColNum) -1]
	favNum = int(input('What is your favourite number from 1-100? '))

	if favNum < 60:
		strength = abs(100 - 2*favNum)
		speed = favNum * 1.75
		wit = round((abs(math.exp(favNum/100) - 2.72))*130,2)
	else:
		strength = abs(int((100 - 3.5*favNum)))
		speed = favNum * 1.25
		wit = round((abs(math.exp(favNum/100) - 2.72))*60,2)

	stats = { # use of python dictionary to using and organizing data better
		"physicalAttributes" : {
			"strength" : strength,
			"speed" : speed,
			"wit" : wit
		},
		"Age" : random.randint(15,72),
		"Height": str(5 + plusMinus(random.randint(0,2))) + 'ft tall',
		"phraseNumber": random.randint(0,4)
	}

	toolList = ["Phone", "Calculator", "1ZC3 Textbook", "Honey-Glazed Donut", "Flashlight"]
	tools = "1) Phone 2) Calculator 3) 1ZC3 Textbook 4) Honey-Glazed Donut 5) Flashlight 6) Random Item"
	sleep(TIME)
	print(tools)
	sleep(TIME)
	toolChoice = int(input("Choose number corresponding to item or 6 for a random item: ")) -1

	if toolChoice == 5:
		tool = toolList[random.randint(0,4)]

	else:
		tool = toolList[toolChoice]

def completeChar(): # include a statement for the user after they decided they have completed their character
	print('==============================Character Creation Completed!=====================')
	sleep(TIME)
	print(sp()[3])
	sleep(TIME)

# Introduction

def introduction(): # brief introduction to the game
	part1 = 'Welcome to the Beta Version of "The Haunted House Adventure!!"'
	print(part1)
	sleep(TIME)
	part2 = 'We will begin by creating your character ...'
	print(part2)
	sleep(TIME)
	lineBrk = '===========================Character Creation Profile========================='
	print(lineBrk)
	sleep(TIME)



################################################################################
introduction()
while True: # while true loop so the player can update their character as many times asthey would want to 
	Start()
	Ghost = createGhostBoss()
	Character = createCharacter(Name, favColor, favNum, tool, stats)
	Character.UserInformation()
	sleep(TIME)
	verify = input("Are you satisfied with your character (y/n)? ")
	if verify == 'y' or verify == 'Y': # if else statement will be used to check if the user is sataisfied with character or not
		completeChar()
		break
	else:
		print('Recreate your character: ')
		sleep(TIME)
		print('==========================================================================')

######################################################################################

# Begin Playing the Game
def section1():
	# In the game sections, I defined all the lines first, then i printed them after, makes the flow of the script a bit more clesn
	# generic questions used in this section; individualized scenarios based on the items the user had in their bags from character creation
	line1 = 'Narrator: ' + Character.getName() + ' wakes up on a gurney in the middle of an empty hospital hallway.'
	line2 = 'The lights are flickering above and ' + Character.getName() + ' notices the rundown nature of the hospital.'
	line3 = Character.getName() + ' gets up and retrieves their ' + Character.getTools()[0] + ' from their bag.'
	
	#["Phone", "Calculator", "1ZC3 Textbook", "Honey-Glazed Donut", "Flashlight"]
	if (Character.getTools()[0] == "Phone") or (Character.getTools()[0] == "Calculator") or (Character.getTools()[0] == "Flashlight"):
		line4 = Character.getName() + ' trys to turn on the ' + Character.getTools()[0] + ' but notices its not working.'
		line5 = Character.getName() + ' gets up, and begins wondering down the hallway till he reaches a set of doors.'
	elif (Character.getTools()[0] == "1ZC3 Textbook"):
		line4 = Character.getName() + ' decides to read their favourite chapter on Euclidian Vector Spaces to calm themself down.'
		line5 = Character.getName() + ' gets up, now that they are calmed down, and begins wondering down the hallway till he reaches a set of doors.'
	else:
		line4 = Character.getName() + ' decides to eat some of his donut to calm themself down.'
		line5 = Character.getName() + ' gets up, now that they are calmed down, and begins wondering down the hallway till he reaches a set of doors.'
	
	print(line1)
	sleep(TIME)
	print(line2)
	sleep(TIME)
	print(line3)
	sleep(TIME)
	print(line4)
	sleep(TIME)
	print(line5)

def section2():
	# this section required user input so print statements were embedded
	line1 = 'Narrator: ' + Character.getName()+ ' sees three doors: a red one, a blue one and a green one.'
	print(line1)
	sleep(TIME)
	print('============================================================================')
	choice = input('Which door would you like to enter: 1) red, 2) blue, 3) green ? ')
	print('============================================================================')
	sleep(TIME)
	if choice == '1' or choice == 'red':
		print(Character.getName(),'enters the red door and finds a working flashlight and a pair of some fashionable gucci sunglasses!')
		sleep(TIME)
		print(sp()[4])
		sleep(TIME)
		print(Character.getName(),'puts on the cool glasses and then exits the room and cotinues down another hallway.')
	elif choice == 'blue' or choice == '2':
		 print(Character.getName(),'enters the blue door and finds a working flashlight and a pair of some fashionable gucci sunglasses!')
		 sleep(TIME)
		 print(sp()[4])
		 sleep(TIME)
		 print(Character.getName(),'puts on the cool glasses and then exits the room and cotinues down another hallway.')
	else:
		 print(Character.getName(),'enters the green door and finds a working flashlight and a 100 dollar bill!')
		 sleep(TIME)
		 print(sp()[1])
		 sleep(TIME)
		 print(Character.getName(),'puts the money in their pocket and then exits the room and cotinues down another hallway.')
	sleep(TIME)
	
def fightStats():
	# function the displayed the ghosts stats and the character stats
	# acts as an explanation for the following event 
	# i.e. were they strong enough to win the fight? fast enough to run away
	in_ = '==================================== Character Stats ======================================================'
	fifth = 'Here are some of your stats: ' + '\n'
	fifthA = '\t- Strength (max:150): ' + str(Character.getStats()["physicalAttributes"]["strength"]) + '\n'
	fifthB = '\t- Speed (max:100): ' + str(Character.getStats()["physicalAttributes"]["speed"]) + '\n'
	fifthC = '\t- Wit (max: 200): ' + str(Character.getStats()["physicalAttributes"]["wit"]) + '\n'
	gin_ = '==================================== Ghost Stats ======================================================'
	Gfifth = 'Here are the Ghost\'s stats: ' + '\n'
	GfifthA = '\t- Strength (max:150): ' + str(Ghost.ghostStrength()) + '\n'
	GfifthB = '\t- Speed (max:100): ' + str(Ghost.ghostSpeed()) + '\n'
	out = '======================================================================================================='
	print(in_)
	sleep(TIME)
	print(fifth)
	sleep(TIME)
	print(fifthA, fifthB, fifthC)
	sleep(TIME)
	print(gin_)
	sleep(TIME)
	print(Gfifth, GfifthA, GfifthB, out)
	sleep(TIME)


def fight(): # if character decides to fight the ghost this is the scenario that is used
	# if else statement checks if the user is stronger/weaker, and in these instances, different scenarios are seen
	fightStats()
	#print('flee')
	line1 = 'Narrator: ' + Character.getName() + ' lunges at the Ghost weilding their flashlight in one hand and ' + Character.getTools()[0] + 'in the Other!'
	print(line1)
	if Character.getStats()["physicalAttributes"]["strength"] > Ghost.ghostStrength():
		line2 = 'The blow successfully lands on the ghosts head and he shrieks!'
		line3 = 'Ghost: I am sooorryy. Please do not hurt meee. I will do whatever you wish!'
		line33 = '=============================================================================='
		print(line2)
		sleep(TIME)
		print(line3)
		sleep(TIME)
		print(line33)
		choice = input('What do you want to say to the ghost? ')
		sleep(TIME)
		line4 = 'Ghost: Thank you for being merciful! You must be lost in this hospital. I will help you leave!'
		print(line4)
	else:

		line2 = 'Narrator: The blow passes right through the ghost and he begins to yell with RAGE. He picks you up with his ghostly powers and tosses you across the hallway!'
		line3 = 'Ghost: Whyyy do you punnyyy humans always try to fight me!?'
		line33 = '=============================================================================='
		print(line2)
		sleep(TIME)
		print(line3)
		sleep(TIME)
		print(line33)
		response = input("What do you want to say to the ghost? ")

		line4 = 'Ghost: Hmmmm, maybe I was tooooo rash. I apologize small human. You seem lost. Let me guide you out of this hospital!'
		sleep(TIME)
		print(line4)

def flee(): # if the chararcter decides to run from the ghost this is the event that happens
	fightStats()
	#print('flee')
	line1 = 'Narrator: ' + Character.getName() + ' flees successfully! However, as they run away, they trip on a rock and fall onto the floor! The ghost manages to catch up to them ...'
	line2 = 'Ghost: Why do you run away from me! I just wanted to help you leave this hospital!'
	line33 = '=============================================================================='
	print(line1)
	sleep(TIME)
	print(line2)
	sleep(TIME)
	print(line33)
	sleep(TIME)
	response = input('What do you want to say to the ghost? ')
	sleep(TIME)
	line4 = 'Ghost: I accept your appology! ** :] the ghost smiles ** I will help you out of the hospital'
	print(line4)

def section3(): # this is the section that cues of the big fight event
	line1 = 'Narrator: ' + Character.getName() + ' continues walking down the hallway wielding the flashlight when they see a ghastly figure approaching...'
        #sleep(TIME)
	print(line1)
	sleep(TIME)
	print(sp()[-1])
	sleep(TIME)
	line2 = 'Ghost: oooooOOOOOooooo!! Whooooo goes theree!'
	line3 = 'Narrator: ' + Character.getName() + ' begins to panic! What will they decide to do ?'
	print(line2)
	sleep(TIME)
	print(line3)
	sleep(TIME)

	decision = input('What would you like to do? 1) Run 2) Fight the Ghost ? ')
	sleep(TIME)


	if decision == '1': # based on the users choice, the fight or flee event will be cued up
	# the events are very similar so in either event, the ghost will apologize and will help them out of the hospital
		flee()
	else:
		fight()
	

def FINISH(): # termination section
	line33 = '=============================================================================='
	final = 'Narrator: '+Character.getName()+ ' and the Ghost make their way through the hospital. ' + Character.getName()+ ' and the ghost live happily ever after and meetup on the weekends to hangout!'
	final1 = '\nThe END!! I hope you enjoyed playing!'
	print(line33)
	sleep(TIME)
	print(final)
	sleep(TIME)
	print(final1)


################################################################ 
# This section is used to display the Story line upon running the function

section1()
section2()
section3()
FINISH()

