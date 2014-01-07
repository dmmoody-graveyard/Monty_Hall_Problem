import random

NUM_ITERATIONS = 1000

# Returns the remaining number that is not given
# as one of the inputs from 1, 2, 3
def remainingDoor (i1, i2):
	if i1 != 1 and i2 != 1:
		return 1
	if i1 != 2 and i2 != 2:
		return 2
	if i1 != 3 and i2 != 3:
		return 3
	print ('Something wrong, args should be different: %i, %i' % (i1, i2))

# Models a contestant who switches the choice
# after the knowledgeable host reveals a winless door
def  runAdaptiveSimulation():
	car = random.randint(1,3)
	guess1 = random.randint(1,3)
	door_opened = 0
	if car != guess1:
		door_opened = remainingDoor (car, guess1)
	else:
		if car == 1:
			door_opened = random.randint(2,3)
		if car == 2:
			door_opened = 1 + 2 * random.randint(0,1)
		if car == 3:
			door_opened = random.randint(1,2)
	adjusted_guess1 = remainingDoor (guess1, door_opened)

	if adjusted_guess1 == car:
		# print ('Hey, won!, original choice: %i, door opened: %i, adjusted choice (and car): %i' % (guess1, door_opened, car))
		return 1
	else:
		return 0

# Models an obstinate contestant who does not switch the choice
# and does not use the knowledge of the host to their advantage
def runUnadaptiveSimulation():
	car = random.randint(1,3)
	guess2 = random.randint(1,3)
	if car == guess2:
		return 1
	else:
		return 0


numIteration = 1
adaptiveSimulationWinCount = 0
unadaptiveSimulationWinCount = 0
while numIteration <= NUM_ITERATIONS:
	adaptiveSimulationWinCount = adaptiveSimulationWinCount + runAdaptiveSimulation()
	unadaptiveSimulationWinCount = unadaptiveSimulationWinCount + runUnadaptiveSimulation()
	# print ('numIteration: %d, running adaptive win count: %d' % (numIteration, adaptiveSimulationWinCount))
	numIteration = numIteration + 1
	
print ('Total number of times run: %d' % NUM_ITERATIONS)
print ('Win count when switching the choice: %d' % adaptiveSimulationWinCount)
print ('Win count when not switching the choice: %d' % unadaptiveSimulationWinCount)