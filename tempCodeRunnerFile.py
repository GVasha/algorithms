import random

# Initialize players' hands and dominoes
Player1 = []
Player2 = []
dominoes = [[i, j] for i in range(7) for j in range(i, 7)]  # Generate dominoes

# Function to draw a domino at random
def draw(dominoes_list):
    return dominoes_list.pop(random.randint(0, len(dominoes_list) - 1)) if dominoes_list else "No more dominoes left."

# Draw 7 dominoes for each player
for _ in range(7):
    Player1.append(draw(dominoes))
    Player2.append(draw(dominoes))

print("Player1's hand:", Player1)
print("Player2's hand:", Player2)

# Stack implementation
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if not self.top:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

# Initialize stacks
stacks = [Stack() for _ in range(4)]  # Create four stacks

# Function to find the biggest equal pair
def find_biggest_equal_pair(domino_stack):
    return max((domino for domino in domino_stack if domino[0] == domino[1]), default=None)

# Find biggest equal pairs
biggest_pair_stack1 = find_biggest_equal_pair(Player1)
biggest_pair_stack2 = find_biggest_equal_pair(Player2)

if biggest_pair_stack1 and (not biggest_pair_stack2 or biggest_pair_stack1[0] >= biggest_pair_stack2[0]):
    print("Player1 has the biggest equal pair:", biggest_pair_stack1)
    for stack in stacks:
        stack.push(biggest_pair_stack1)
else:
    print("Player2 has the biggest equal pair:", biggest_pair_stack2)
    for stack in stacks:
        stack.push(biggest_pair_stack2)

# Move function unchanged
def move(playerstack):
    print(stacks[0].top.value[0], stacks[1].top.value[0], stacks[2].top.value[0], stacks[3].top.value[0])
    number = int(input("Choose the tile you would like to use from your stack: "))
    stacktoappend = int(input("Choose the stack you want to place the tile on (1-4): "))
    
    if 1 <= stacktoappend <= 4:
        target_stack = stacks[stacktoappend - 1]
        if target_stack.top.value[0] in (playerstack[number - 1][0], playerstack[number - 1][1]):
            target_stack.push(playerstack[number - 1][1] if target_stack.top.value[0] == playerstack[number - 1][0] else playerstack[number - 1][0])
        else:
            print('Please enter another tile, as it is impossible to put it.')
            move(playerstack)

# Define the game function
def game(starter, ender):
    print("Start the game")
    print(starter)
    move(starter)

game(Player1, Player2)
