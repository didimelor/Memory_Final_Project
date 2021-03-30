'''
Diana Karen Melo Reyes
Final Project: Memory
October 21st 2019
'''
import random

# Global Variables
scorePlayer1 = 0
scorePlayer2 = 0

def main():
    numMatrix = [[1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18],
            [1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18]]
    guessedCards = [[False,False,False,False,False,False],
                      [False,False,False,False,False,False],
                      [False,False,False,False,False,False],
                      [False,False,False,False,False,False],
                      [False,False,False,False,False,False],
                      [False,False,False,False,False,False]]

    #Randomize functions for the number matrix
    numMatrix = rand(numMatrix)

    selectedOption = 0

    while (selectedOption != 3): #Option 3 is exit game, so if 3 is not selected the game continues
        selectedOption = menu()

        if (selectedOption == 1): #Continue playing
            leaveOpen(numMatrix, guessedCards)
            player1 (numMatrix, guessedCards)
            player2 (numMatrix, guessedCards)
        if (selectedOption == 2): #Restart, all cards shuffle and are printed as "-"
            numMatrix = rand(numMatrix)
            restart(guessedCards, numMatrix)
    if (selectedOption == 3): #Exit
        exit()
         
def menu ():
    selectedOption = 0
    print('Welcome to the menu')
    print('Keep playing: 1')
    print('Restart the game: 2')
    print('Exit: 3 ')
    selectedOption = int(input('Type your selected number\n'))
    if(selectedOption == 1 or selectedOption == 2 or selectedOption == 3):
        print("Your selected option was: ", selectedOption)
    else:
        while(selectedOption != 1 or selectedOption != 2 or selectedOption != 3):
            selectedOption = int(input("Please type a valid number\n"))
            if(selectedOption == 1 or selectedOption == 2 or selectedOption == 3):
                print("Your selected option was: ", selectedOption)
                break
    '''
    while(selectedOption != 1 or selectedOption != 2 or selectedOption != 3):
            selectedOption = int(input("Please type a valid number\n"))
    '''
    return selectedOption
          
def rand (numMatrix):
    random.shuffle(numMatrix) #randomize the rows
    for rows in range(len(numMatrix)):
        for cols in range (len(numMatrix[rows])):
            random.shuffle(numMatrix[rows]) #randomize numbers for each row
    return numMatrix

# Prints matrix
def leaveOpen (numMatrix, guessedCards):
    for row in range(len(numMatrix)):
        for col in range (len(numMatrix[row])):
            if guessedCards[row][col] == False:
                print('-', end=' ') #Has not been guessed prints -
            else:
                print(numMatrix[row][col], end=' ')#It was guessed print the number
        print()

def validateInput(guessedCards):
    #Ask input
    x = 0
    y = 0
    x = int(input('Column: '))
    y = int(input('Row: '))
    #Input out of range
    while x < 0 or x > 5 or y < 0 or y > 5:
        print('Invalid row or column, please type numbers from 0 to 5')
        x = int(input('Row: '))
        y = int(input('Column: '))
    #Input already a guessed card
    while guessedCards[y][x] == True:
        print('The input has a guessed card, choose another one')
        x = int(input('Row: '))
        y = int(input('Column: '))
    return x, y

def player1 (numMatrix, guessedCards):
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    global scorePlayer1
    print('\n')
    print('Player 1 turn, choose the card to open. Remember the rows and columns start at cero')
    #Ask first card input
    x, y = validateInput(guessedCards)
    #Opens selected card
    guessedCards[y][x] = True
    leaveOpen (numMatrix, guessedCards)
    #Ask second card input   
    print("Select the row and column for the second card")
    x2, y2 = validateInput(guessedCards)
    #Opens selected card     
    guessedCards[y2][x2] = True
    leaveOpen(numMatrix, guessedCards)
    #Correct or incorrect guess comparison
    if numMatrix[y][x] != numMatrix[y2][x2]:
        guessedCards[y][x] = False
        guessedCards[y2][x2] = False
        print('Incorrect guess :(')
        print('Player 1 score:', scorePlayer1)
    else:
        scorePlayer1 += 1
        print('Correct guess!')
        print('Player 1 score:', scorePlayer1)
        
    leaveOpen(numMatrix, guessedCards)
    
    
def player2 (numMatrix, guessedCards):
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    global scorePlayer2
    print('\n')
    print('Player 2 turn, choose the card to open. Remember the rows and columns start at cero ')
    #Ask first card input
    x, y = validateInput(guessedCards)
    #Opens selected card
    guessedCards[y][x] = True
    leaveOpen(numMatrix, guessedCards)
    #Ask second card input
    print("Select the row and column for the second card")
    x2, y2 = validateInput(guessedCards)
    #Opens selected card
    guessedCards[y2][x2] = True
    leaveOpen(numMatrix, guessedCards)
    #Correct or incorrect guess comparison
    if numMatrix[y][x] != numMatrix[y2][x2]:
        guessedCards[y][x] = False
        guessedCards[y2][x2] = False
        print('Incorrect guess :(')
        print('Player 2 score: ', scorePlayer2)
    else:
        scorePlayer2 += 1
        print('Player 2 score: ', scorePlayer2)
        
    leaveOpen(numMatrix, guessedCards)

def restart (guessedCards, numMatrix):
    print('You chose to restart the game')
    for y in range(len(guessedCards)):
        for x in range (len(guessedCards[y])):
            guessedCards[y][x] = False
    print('Game restarted')
    #Print new game
    leaveOpen(numMatrix, guessedCards)
    
#Shows score before exiting
def exit():
    global scorePlayer1 
    global scorePlayer2
    print('You chose to exit the game')
    print('Player 1 score: ', scorePlayer1)#Imprime las puntuaciones
    print('Pplayer 2 score: ', scorePlayer2)
    if(scorePlayer1 > scorePlayer2):
        print('Player 1 wins!')
    elif(scorePlayer2 > scorePlayer1):
        print('Player 2 wins!')
    else:
        print('Its a tie')
    print('Bye')
            
main()