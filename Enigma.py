#!/usr/bin/python

# Define global variables
rotorsUsed = []
rotorPositions = []
reflector = ""
message = ""

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

rotorMapForward = {
	'I' : {
		0 : 4,
		1 : 10,
		2 : 12,
		3 : 5,
		4 : 11,
		5 : 6,
		6 : 3,
		7 : 16,
		8 : 21,
		9 : 25,
		10 : 13,
		11 : 19,
		12 : 14,
		13 : 22,
		14 : 24,
		15 : 7,
		16 : 23,
		17 : 20,
		18 : 18,
		19 : 15,
		20 : 0,
		21 : 8,
		22 : 1,
		23 : 17,
		24 : 2,
		25 : 9
	},
	'II' : {
		0 : 0,
		1 : 9,
		2 : 3,
		3 : 10,
		4 : 18,
		5 : 8,
		6 : 17,
		7 : 20,
		8 : 23,
		9 : 1,
		10 : 11,
		11 : 7,
		12 : 22,
		13 : 19,
		14 : 12,
		15 : 2,
		16 : 16,
		17 : 6,
		18 : 25,
		19 : 13,
		20 : 15,
		21 : 24,
		22 : 5,
		23 : 21,
		24 : 14,
		25 : 4
	},
	'III' : {
		0 : 1,
		1 : 3,
		2 : 5,
		3 : 7,
		4 : 9,
		5 : 11,
		6 : 2,
		7 : 15,
		8 : 17,
		9 : 19,
		10 : 23,
		11 : 21,
		12 : 25,
		13 : 13,
		14 : 24,
		15 : 4,
		16 : 8,
		17 : 22,
		18 : 6,
		19 : 0,
		20 : 10,
		21 : 12,
		22 : 20,
		23 : 18,
		24 : 16,
		25 : 14
	},
	'IV' : {
		0 : 4,
		1 : 18,
		2 : 14,
		3 : 21,
		4 : 15,
		5 : 25,
		6 : 9,
		7 : 0,
		8 : 24,
		9 : 16,
		10 : 20,
		11 : 8,
		12 : 17,
		13 : 7,
		14 : 23,
		15 : 11,
		16 : 13,
		17 : 5,
		18 : 19,
		19 : 6,
		20 : 10,
		21 : 3,
		22 : 2,
		23 : 12,
		24 : 22,
		25 : 1
	},
	'V' : {
		0 : 21,
		1 : 25,
		2 : 1,
		3 : 17,
		4 : 6,
		5 : 8,
		6 : 19,
		7 : 24,
		8 : 20,
		9 : 15,
		10 : 18,
		11 : 3,
		12 : 13,
		13 : 7,
		14 : 11,
		15 : 23,
		16 : 0,
		17 : 22,
		18 : 12,
		19 : 9,
		20 : 16,
		21 : 14,
		22 : 5,
		23 : 4,
		24 : 2,
		25 : 10
	}
}

rotorMapBackward = {
	'I' : {
		0 : 20,
		1 : 22,
		2 : 24,
		3 : 6,
		4 : 0,
		5 : 3,
		6 : 5,
		7 : 15,
		8 : 21,
		9 : 25,
		10 : 1,
		11 : 4,
		12 : 2,
		13 : 10,
		14 : 12,
		15 : 19,
		16 : 7,
		17 : 23,
		18 : 18,
		19 : 11,
		20 : 17,
		21 : 8,
		22 : 13,
		23 : 16,
		24 : 14,
		25 : 9
	},
	'II' : {
		0 : 0,
		1 : 9,
		2 : 15,
		3 : 2,
		4 : 25,
		5 : 22,
		6 : 17,
		7 : 11,
		8 : 5,
		9 : 1,
		10 : 3,
		11 : 10,
		12 : 14,
		13 : 19,
		14 : 24,
		15 : 20,
		16 : 16,
		17 : 6,
		18 : 4,
		19 : 13,
		20 : 7,
		21 : 23,
		22 : 12,
		23 : 8,
		24 : 21,
		25 : 18
	},
	'III' : {
		0 : 19,
		1 : 0,
		2 : 6,
		3 : 1,
		4 : 15,
		5 : 2,
		6 : 18,
		7 : 3,
		8 : 16,
		9 : 4,
		10 : 20,
		11 : 5,
		12 : 21,
		13 : 13,
		14 : 25,
		15 : 7,
		16 : 24,
		17 : 8,
		18 : 23,
		19 : 9,
		20 : 22,
		21 : 11,
		22 : 17,
		23 : 10,
		24 : 14,
		25 : 12
	},
	'IV' : {
		0 : 7,
		1 : 25,
		2 : 22,
		3 : 21,
		4 : 0,
		5 : 17,
		6 : 19,
		7 : 13,
		8 : 11,
		9 : 6,
		10 : 20,
		11 : 15,
		12 : 23,
		13 : 16,
		14 : 2,
		15 : 4,
		16 : 9,
		17 : 12,
		18 : 1,
		19 : 18,
		20 : 10,
		21 : 3,
		22 : 24,
		23 : 14,
		24 : 8,
		25 : 5
	},
	'V' : {
		0 : 16,
		1 : 2,
		2 : 24,
		3 : 11,
		4 : 23,
		5 : 22,
		6 : 4,
		7 : 13,
		8 : 5,
		9 : 19,
		10 : 25,
		11 : 14,
		12 : 18,
		13 : 12,
		14 : 21,
		15 : 9,
		16 : 20,
		17 : 3,
		18 : 10,
		19 : 6,
		20 : 8,
		21 : 0,
		22 : 17,
		23 : 15,
		24 : 7,
		25 : 1
	}
}

reflectorMap = {
	'B' : {
		0 : 24,
		1 : 17,
		2 : 20,
		3 : 7,
		4 : 16,
		5 : 18,
		6 : 11,
		7 : 3,
		8 : 15,
		9 : 23,
		10 : 13,
		11 : 6,
		12 : 14,
		13 : 10,
		14 : 12,
		15 : 8,
		16 : 4,
		17 : 1,
		18 : 5,
		19 : 25,
		20 : 2,
		21 : 22,
		22 : 21,
		23 : 9,
		24 : 0,
		25 : 19
	}
}

rotorSteps = {
	'I' : 17,
	'II' : 4,
	'III' : 21,
	'IV' : 9,
	'V' : 25
}

plugboard = {
	'A' : 'A',
	'B' : 'B',
	'C' : 'C',
	'D' : 'D',
	'E' : 'E',
	'F' : 'F',
	'G' : 'G',
	'H' : 'H',
	'I' : 'I',
	'J' : 'J',
	'K' : 'K',
	'L' : 'L',
	'M' : 'M',
	'N' : 'N',
	'O' : 'O',
	'P' : 'P',
	'Q' : 'Q',
	'R' : 'R',
	'S' : 'S',
	'T' : 'T',
	'U' : 'U',
	'V' : 'V',
	'W' : 'W',
	'X' : 'X',
	'Y' : 'Y',
	'Z' : 'Z'
}

# Function to decrypt message
def decryptMessage():
	global rotorsUsed, rotorPositions

	print("Rotors:",rotorsUsed)
	print("Staring Positions:",rotorPositions)
	print("Plugboard:",printPlugboard())

	# Decrypt/encrypt message
	return enigma()


# Function to emulate enigma machine
def enigma():
	# Define global variables
	global rotorsUsed, rotorPositions, reflector

	decryptedMessage = ""
	chars = list(message)

	for letter in chars:
		# Pass through plug board
		letter = plugboard[letter]

		# Get index of input letter
		letterIndex = alphabet.index(letter)
		stepRotor(2) # Advance the rightmost rotor

		# Propagate forward through the machine
		for i in range(len(rotorsUsed)-1,-1,-1):
			letterIndex = rotorMapForward[rotorsUsed[i]][(rotorPositions[i] + letterIndex) % 26] - rotorPositions[i]
			# Ensure the letter index is positive
			letterIndex %= 26

		# Pass through the reflector
		letterIndex = reflectorMap[reflector][letterIndex]

		# Propagate backward through the machine
		for i in range(0,len(rotorsUsed)):
			letterIndex = rotorMapBackward[rotorsUsed[i]][(rotorPositions[i] + letterIndex) % 26] - rotorPositions[i]
			# Ensure the letter index is positive
			letterIndex %= 26

		# Get letter at index
		letter = alphabet[letterIndex]

		# Pass through plug board
		letter = plugboard[letter]

		# Compile the decrypted letters into a return variable
		decryptedMessage += letter

	return decryptedMessage


# Function to rotate rotors
def stepRotor(rotorNum):
	# Define global variables
	global rotorPositions, rotorSteps, rotorsUsed

	index = rotorPositions[rotorNum]

	# Step current rotor
	rotorPositions[rotorNum] = (index+1) % 26

	# Double step middle rotor
	if rotorNum == 2 and rotorPositions[1] == rotorSteps[rotorsUsed[1]]: stepRotor(1)

	# Step adjacent rotors if necessary
	if rotorNum > 0 and index == rotorSteps[rotorsUsed[rotorNum]]:
		stepRotor(rotorNum-1); # Step the rotor to the left


# Function to print out plugboard configuration
def printPlugboard():
	# Initalize variable
	configuration = ""
	# Loop through the remaining lines in alphabetical order
	for letter in alphabet:
		if letter is not plugboard[letter]:
			configuration += letter + "=>" + plugboard[letter] + ", "

	# Trim off last two characters and return formatted printout
	if len(configuration) > 0: return configuration.rstrip(", ")
	else: return "Default"


def main():
	# Define global variables
	global rotorPositions, rotorsUsed, reflector, message

	# Open the file to read
	file = open("enigma.txt", "r")

	# Read in configuration line
	configuration = file.readline().rstrip("\n").split("  ")

	# Read in the message from the input file
	message = file.readline()

	# Close the file
	file.close()

	# If the file contains a key, decrypt the message using that.
	# Otherwise, predefine the default settings for the enigma machine.
	if (configuration[0] is "Unknown"):
		hasKey = False
		reflector = 'B'
		rotorsUsed = ['I','II','III']
		rotorPositions = [0,0,0]
	else:
		hasKey = True
		# Assign configuration variables
		reflector = configuration[0]
		rotorsUsed = configuration[1].split(",")
		for letter in list(configuration[2]):
			rotorPositions.append(alphabet.index(letter))
		
		if len(configuration) == 4:
			for pair in configuration[3].split():
				letters = list(pair)
				# Assign letters to each other on the plugboard
				plugboard[letters[0]], plugboard[letters[1]] = plugboard[letters[1]], plugboard[letters[0]]

	# Print out the encrypted message
	print("Input message:",message)

	# Print out the decrypted message
	print("Output message:",decryptMessage());

main()