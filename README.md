Algorithms Project: Dominoes Game
This project is a simple implementation of a dominoes game using Python. The game involves two players, Player1 and Player2, each drawing dominoes randomly and using stacks to manage game moves. This project demonstrates the use of stacks and matrices to store and manipulate data.

Description
The game initializes by generating a full set of dominoes and randomly drawing 7 dominoes for each player. Players then try to find the biggest equal pair of dominoes and play moves by stacking dominoes on a chosen pile.

How to Use
Clone the Repository:

Use the command to clone and navigate into the repository.

Run the Game:

Execute the main file to start the game.

Code Explanation
Initialize Players' Hands and Dominoes
This section initializes two empty lists for Player1 and Player2's hands and generates the full set of dominoes using a list comprehension.

Draw Function
Functionality: Draws a domino at random from the provided list of dominoes. Input: List of dominoes. Output: A randomly drawn domino, removed from the list.

Draw 7 Dominoes for Each Player
This loop assigns 7 randomly drawn dominoes to each player.

Stack Implementation
Functionality: Implements a basic stack using a linked list. Methods:

push(value): Pushes a value onto the stack.

pop(): Pops the top value off the stack.

Initialize Stacks
Creates four stack instances to represent the game piles.

Find Biggest Equal Pair Function
Functionality: Finds the biggest equal pair (e.g., [2, 2]) in a player's hand. Input: List of dominoes (player's hand). Output: The biggest equal pair of dominoes, if any.

Move Function
Functionality: Manages the player's move by choosing a tile from their hand and placing it on one of the four stacks based on user input. Input: Player's hand (list of dominoes). Output: Modifies the player's hand and the game stacks based on the move.

Game Function
Functionality: Orchestrates the game by alternating moves between players until one player runs out of dominoes. Input: Hands of both players. Output: Runs the game loop and declares a winner.

This should be easier to copy and use for your project. Good luck with your algorithms project! 🎲🀄️
