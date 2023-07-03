# Matthew Fries, Assignment #5.
# This program simulates a simple game known as Wumpus World. A game board is randomly generated with
# 16 cells in a 4 by 4 grid. The player, gold, wumpus, and pits are all randomly generated on the
# game board. The goal of the game is to move the player to the gold without falling into a pit or
# being caught by the wumpus. Multiple 2D lists are utilized as a knowledge base for the program
# in an attempt to make safe moves before having to take a potentially dangerous move on the game board.
import random


# This function moves the player up on the board.
def moveUp(RowCtr, ColCtr, proceedFlag):
    w[RowCtr][ColCtr].remove('A')
    if len(w[RowCtr][ColCtr]) == 0:
        w[RowCtr][ColCtr].append('')
    RowCtr = RowCtr - 1
    if 'W' in w[RowCtr][ColCtr]:
        print("You were caught by the Wumpus. Game Over!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if 'G' in w[RowCtr][ColCtr]:
        print("You found the gold. You Win!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if 'P' in w[RowCtr][ColCtr]:
        print("You fell into a pit. Game Over!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if w[RowCtr][ColCtr][0] == '':
        w[RowCtr][ColCtr][0] = 'A'
        return RowCtr, ColCtr, proceedFlag
    else:
        w[RowCtr][ColCtr].append('A')
        return RowCtr, ColCtr, proceedFlag


# This function moves the player down on the board.
def moveDown(RowCtr, ColCtr, proceedFlag):
    w[RowCtr][ColCtr].remove('A')
    if len(w[RowCtr][ColCtr]) == 0:
        w[RowCtr][ColCtr].append('')
    RowCtr = RowCtr + 1
    if 'W' in w[RowCtr][ColCtr]:
        print("You were caught by the Wumpus. Game Over!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if 'G' in w[RowCtr][ColCtr]:
        print("You found the gold. You Win!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if 'P' in w[RowCtr][ColCtr]:
        print("You fell into a pit. Game Over!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if w[RowCtr][ColCtr][0] == '':
        w[RowCtr][ColCtr][0] = 'A'
        return RowCtr, ColCtr, proceedFlag
    else:
        w[RowCtr][ColCtr].append('A')
        return RowCtr, ColCtr, proceedFlag


# This function moves the player left on the board.
def moveLeft(RowCtr, ColCtr, proceedFlag):
    w[RowCtr][ColCtr].remove('A')
    if len(w[RowCtr][ColCtr]) == 0:
        w[RowCtr][ColCtr].append('')
    ColCtr = ColCtr - 1
    if 'W' in w[RowCtr][ColCtr]:
        print("You were caught by the Wumpus. Game Over!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if 'G' in w[RowCtr][ColCtr]:
        print("You found the gold. You Win!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if 'P' in w[RowCtr][ColCtr]:
        print("You fell into a pit. Game Over!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if w[RowCtr][ColCtr][0] == '':
        w[RowCtr][ColCtr][0] = 'A'
        return RowCtr, ColCtr, proceedFlag
    else:
        w[RowCtr][ColCtr].append('A')
        return RowCtr, ColCtr, proceedFlag


# This function moves the player right on the board.
def moveRight(RowCtr, ColCtr, proceedFlag):
    w[RowCtr][ColCtr].remove('A')
    if len(w[RowCtr][ColCtr]) == 0:
        w[RowCtr][ColCtr].append('')
    ColCtr = ColCtr + 1
    if 'W' in w[RowCtr][ColCtr]:
        print("You were caught by the Wumpus. Game Over!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if 'G' in w[RowCtr][ColCtr]:
        print("You found the gold. You Win!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if 'P' in w[RowCtr][ColCtr]:
        print("You fell into a pit. Game Over!")
        proceedFlag = False
        return RowCtr, ColCtr, proceedFlag
    if w[RowCtr][ColCtr][0] == '':
        w[RowCtr][ColCtr][0] = 'A'
        return RowCtr, ColCtr, proceedFlag
    else:
        w[RowCtr][ColCtr].append('A')
        return RowCtr, ColCtr, proceedFlag


# 3d list to represent game world
w = [
    [[''], [''], [''], ['']],
    [[''], [''], [''], ['']],
    [[''], [''], [''], ['']],
    [[''], [''], [''], ['']]
]

# 2D list to represent what cells do NOT have a pit
noPit = [
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', '']
]

# 2D list to represent what cells have a breeze
brz = [
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', '']
]

# 2D list to represent what cells have a stench
stn = [
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', '']
]

# 2D list to represent potential moves
potentialMoves = [
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', '']
]

# Roll random numbers to decide placement of agent, wumpus, pits, and gold.
goldRow = random.randint(0, 3)
goldCol = random.randint(0, 3)
w[goldRow][goldCol][0] = 'G'

# Place the wumpus randomly on board, only places in an empty cell
wumpus = False
while not wumpus:
    wumpusRow = random.randint(0, 3)
    wumpusCol = random.randint(0, 3)
    if "G" in w[wumpusRow][wumpusCol]:
        continue
    w[wumpusRow][wumpusCol][0] = 'W'
    wumpus = True

# Place the agent randomly on board, only places in an empty cell
agent = False
while not agent:
    agentRow = random.randint(0, 3)
    agentCol = random.randint(0, 3)
    if "G" in w[agentRow][agentCol]:
        continue
    if "W" in w[agentRow][agentCol]:
        continue
    w[agentRow][agentCol][0] = 'A'
    agent = True

# Prompt user to enter number of pits to be placed in game world
numPits = int(input("How many pits would you like to generate in the world? (1-3)\n"))
while not 1 <= numPits <= 3:
    print("Invalid number of pits. Please enter a number 1-3.")
    numPits = int(input("How many pits would you like to generate in the world? (1-3)\n"))

# Randomly place pits in game world, only placed in empty cells
loopCtr = 0
while loopCtr < numPits:
    pitRow = random.randint(0, 3)
    pitCol = random.randint(0, 3)
    if "G" in w[pitRow][pitCol]:
        continue
    elif "W" in w[pitRow][pitCol]:
        continue
    elif "A" in w[pitRow][pitCol]:
        continue
    elif "P" in w[pitRow][pitCol]:
        continue
    else:
        w[pitRow][pitCol][0] = 'P'
        loopCtr += 1

# Generate breezes on game board based on where pits are on the board.
rowCtr2 = -1
colCtr2 = -1
for row in w:
    rowCtr2 += 1
    for col in row:
        colCtr2 += 1
        if colCtr2 == 4:
            colCtr2 = 0
        for cell in col:
            if cell == 'P':
                if rowCtr2 - 1 >= 0:
                    if 'B' not in w[rowCtr2 - 1][colCtr2]:
                        if 'P' not in w[rowCtr2 - 1][colCtr2]:
                            if w[rowCtr2 - 1][colCtr2][0] == '':
                                w[rowCtr2 - 1][colCtr2][0] = 'B'
                            else:
                                w[rowCtr2 - 1][colCtr2].append('B')
                if rowCtr2 + 1 <= 3:
                    if 'B' not in w[rowCtr2 + 1][colCtr2]:
                        if 'P' not in w[rowCtr2 + 1][colCtr2]:
                            if w[rowCtr2 + 1][colCtr2][0] == '':
                                w[rowCtr2 + 1][colCtr2][0] = 'B'
                            else:
                                w[rowCtr2 + 1][colCtr2].append('B')
                if colCtr2 - 1 >= 0:
                    if 'B' not in w[rowCtr2][colCtr2 - 1]:
                        if 'P' not in w[rowCtr2][colCtr2 - 1]:
                            if w[rowCtr2][colCtr2 - 1][0] == '':
                                w[rowCtr2][colCtr2 - 1][0] = 'B'
                            else:
                                w[rowCtr2][colCtr2 - 1].append('B')
                if colCtr2 + 1 <= 3:
                    if 'B' not in w[rowCtr2][colCtr2 + 1]:
                        if 'P' not in w[rowCtr2][colCtr2 + 1]:
                            if w[rowCtr2][colCtr2 + 1][0] == '':
                                w[rowCtr2][colCtr2 + 1][0] = 'B'
                            else:
                                w[rowCtr2][colCtr2 + 1].append('B')
            # Generate stench on game board based on where the wumpus is on the game board.
            if cell == 'W':
                if rowCtr2 - 1 >= 0:
                    if w[rowCtr2 - 1][colCtr2][0] == '':
                        w[rowCtr2 - 1][colCtr2][0] = 'S'
                    else:
                        w[rowCtr2 - 1][colCtr2].append('S')
                if rowCtr2 + 1 <= 3:
                    if w[rowCtr2 + 1][colCtr2][0] == '':
                        w[rowCtr2 + 1][colCtr2][0] = 'S'
                    else:
                        w[rowCtr2 + 1][colCtr2].append('S')
                if colCtr2 - 1 >= 0:
                    if w[rowCtr2][colCtr2 - 1][0] == '':
                        w[rowCtr2][colCtr2 - 1][0] = 'S'
                    else:
                        w[rowCtr2][colCtr2 - 1].append('S')
                if colCtr2 + 1 <= 3:
                    if w[rowCtr2][colCtr2 + 1][0] == '':
                        w[rowCtr2][colCtr2 + 1][0] = 'S'
                    else:
                        w[rowCtr2][colCtr2 + 1].append('S')

print("\nGame Board: ")
for row in w:
    for col in row:
        print(col, end="")
    print()

# Locate where agent is on the board.
rowCtr = -1
colCtr = -1
foundAgent = False
while not foundAgent:
    for row in w:
        rowCtr += 1
        for col in row:
            colCtr += 1
            if colCtr == 4:
                colCtr = 0
            for cell in col:
                if 'A' in cell:
                    aRowCtr = rowCtr
                    aColCtr = colCtr
                    noPit[rowCtr][colCtr] = 'N'
                    if 'B' in w[rowCtr][colCtr]:
                        brz[rowCtr][colCtr] = 'B'
                    if 'S' in w[rowCtr][colCtr]:
                        stn[rowCtr][colCtr] = 'S'
                    foundAgent = True

# Begin game simulation
proceed = True
while proceed:
    move = input("Would you like to move? (Y, N)\n")
    if move == 'N' or move == 'n':
        proceed = False
    elif move == 'Y' or move == 'y':
        # Mark all potential moves as either dangerous or safe.
        if aRowCtr - 1 >= 0:
            potentialMoves[aRowCtr - 1][aColCtr] = 'Safe'
            if stn[aRowCtr - 1][aColCtr] == 'S':
                potentialMoves[aRowCtr - 1][aColCtr] = 'Danger'
            if brz[aRowCtr - 1][aColCtr] == 'B':
                potentialMoves[aRowCtr - 1][aColCtr] = 'Danger'
        if aRowCtr + 1 <= 3:
            potentialMoves[aRowCtr + 1][aColCtr] = 'Safe'
            if stn[aRowCtr + 1][aColCtr] == 'S':
                potentialMoves[aRowCtr + 1][aColCtr] = 'Danger'
            if brz[aRowCtr + 1][aColCtr] == 'B':
                potentialMoves[aRowCtr + 1][aColCtr] = 'Danger'
        if aColCtr - 1 >= 0:
            potentialMoves[aRowCtr][aColCtr - 1] = 'Safe'
            if stn[aRowCtr][aColCtr - 1] == 'S':
                potentialMoves[aRowCtr][aColCtr - 1] = 'Danger'
            if brz[aRowCtr][aColCtr - 1] == 'B':
                potentialMoves[aRowCtr][aColCtr - 1] = 'Danger'
        if aColCtr + 1 <= 3:
            potentialMoves[aRowCtr][aColCtr + 1] = 'Safe'
            if stn[aRowCtr][aColCtr + 1] == 'S':
                potentialMoves[aRowCtr][aColCtr + 1] = 'Danger'
            if brz[aRowCtr][aColCtr + 1] == 'B':
                potentialMoves[aRowCtr][aColCtr + 1] = 'Danger'
        # Code to prevent agent from getting stuck in the corner of game board.
        if aRowCtr - 1 == -1 and noPit[aRowCtr + 1][aColCtr] == 'N':
            if aColCtr + 1 <= 3 and potentialMoves[aRowCtr][aColCtr + 1] == 'Safe':
                if 'B' in w[aRowCtr][aColCtr]:
                    brz[aRowCtr][aColCtr] = 'B'
                if 'S' in w[aRowCtr][aColCtr]:
                    stn[aRowCtr][aColCtr] = 'S'
                aRowCtr, aColCtr, proceed = moveRight(aRowCtr, aColCtr, proceed)
                if proceed:
                    noPit[aRowCtr][aColCtr] = 'N'
            elif aColCtr - 1 >= 0 and potentialMoves[aRowCtr][aColCtr - 1] == 'Safe':
                if 'B' in w[aRowCtr][aColCtr]:
                    brz[aRowCtr][aColCtr] = 'B'
                if 'S' in w[aRowCtr][aColCtr]:
                    stn[aRowCtr][aColCtr] = 'S'
                aRowCtr, aColCtr, proceed = moveLeft(aRowCtr, aColCtr, proceed)
                if proceed:
                    noPit[aRowCtr][aColCtr] = 'N'
            else:
                if 'B' in w[aRowCtr][aColCtr]:
                    brz[aRowCtr][aColCtr] = 'B'
                if 'S' in w[aRowCtr][aColCtr]:
                    stn[aRowCtr][aColCtr] = 'S'
                aRowCtr, aColCtr, proceed = moveDown(aRowCtr, aColCtr, proceed)
                if proceed:
                    noPit[aRowCtr][aColCtr] = 'N'
        # Attempt to make a safe move first.
        if aRowCtr - 1 >= 0 and potentialMoves[aRowCtr - 1][aColCtr] == 'Safe':
            if aRowCtr - 1 >= 0:
                if 'B' in w[aRowCtr][aColCtr]:
                    brz[aRowCtr][aColCtr] = 'B'
                if 'S' in w[aRowCtr][aColCtr]:
                    stn[aRowCtr][aColCtr] = 'S'
                aRowCtr, aColCtr, proceed = moveUp(aRowCtr, aColCtr, proceed)
                if proceed:
                    noPit[aRowCtr][aColCtr] = 'N'
        elif aRowCtr + 1 <= 3 and potentialMoves[aRowCtr + 1][aColCtr] == 'Safe':
            if aRowCtr + 1 <= 3:
                if 'B' in w[aRowCtr][aColCtr]:
                    brz[aRowCtr][aColCtr] = 'B'
                if 'S' in w[aRowCtr][aColCtr]:
                    stn[aRowCtr][aColCtr] = 'S'
                aRowCtr, aColCtr, proceed = moveDown(aRowCtr, aColCtr, proceed)
                if proceed:
                    noPit[aRowCtr][aColCtr] = 'N'
        elif aColCtr - 1 >= 0 and potentialMoves[aRowCtr][aColCtr - 1] == 'Safe':
            if aColCtr - 1 >= 0:
                if 'B' in w[aRowCtr][aColCtr]:
                    brz[aRowCtr][aColCtr] = 'B'
                if 'S' in w[aRowCtr][aColCtr]:
                    stn[aRowCtr][aColCtr] = 'S'
                aRowCtr, aColCtr, proceed = moveLeft(aRowCtr, aColCtr, proceed)
                if proceed:
                    noPit[aRowCtr][aColCtr] = 'N'
        elif aColCtr + 1 <= 3 and potentialMoves[aRowCtr][aColCtr + 1] == 'Safe':
            if aColCtr + 1 <= 3:
                if 'B' in w[aRowCtr][aColCtr]:
                    brz[aRowCtr][aColCtr] = 'B'
                if 'S' in w[aRowCtr][aColCtr]:
                    stn[aRowCtr][aColCtr] = 'S'
                aRowCtr, aColCtr, proceed = moveRight(aRowCtr, aColCtr, proceed)
                if proceed:
                    noPit[aRowCtr][aColCtr] = 'N'
        else:
            # Move randomly up or down if no potential moves are safe.
            if aRowCtr - 1 >= 0:
                if 'B' in w[aRowCtr][aColCtr]:
                    brz[aRowCtr][aColCtr] = 'B'
                if 'S' in w[aRowCtr][aColCtr]:
                    stn[aRowCtr][aColCtr] = 'S'
                aRowCtr, aColCtr, proceed = moveUp(aRowCtr, aColCtr, proceed)
                if proceed:
                    noPit[aRowCtr][aColCtr] = 'N'
            elif aRowCtr + 1 <= 3 and potentialMoves[aRowCtr + 1][aColCtr] == 'Safe':
                if aRowCtr + 1 <= 3:
                    if 'B' in w[aRowCtr][aColCtr]:
                        brz[aRowCtr][aColCtr] = 'B'
                    if 'S' in w[aRowCtr][aColCtr]:
                        stn[aRowCtr][aColCtr] = 'S'
                    aRowCtr, aColCtr, proceed = moveDown(aRowCtr, aColCtr, proceed)
                    if proceed:
                        noPit[aRowCtr][aColCtr] = 'N'

        potentialMoves.clear()
        potentialMoves = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]

        # Print breeze, stench, and no pit lists. These act as a knowledge base and are updated each move.
        print("\nBreeze: ")
        for row in brz:
            print(row, end="")
            print()

        print("\nStench: ")
        for row in stn:
            print(row, end="")
            print()

        print("\nNo Pit: ")
        for row in noPit:
            print(row, end="")
            print()
    else:
        print("Invalid input. Enter Y or N")
        continue

# Print game board
print("\nGame Board: ")
for row in w:
    for col in row:
        print(col, end="")
    print()
