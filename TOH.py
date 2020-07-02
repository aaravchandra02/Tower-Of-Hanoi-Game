from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)


# Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while(num_disks < 3):
    num_disks = int(input("\nHow many disks do you want to play with?\n"))

# We will represent disks with numbers. Disk 3 is larger than Disk 1 etc.
for i in range(num_disks, 0, -1):
    left_stack.push(i)

# For towers of hanoi, the number of optimal moves is always 2Number of Disks - 1.
num_optimal_moves = 2**num_disks - 1

print(
    f"\nThe fastest you can solve this game is in {num_optimal_moves} moves\n")


# Get User Input
def get_input():
    while(True):
        choices = [i.get_name()[0] for i in stacks]
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"\tEnter {letter} for {name}")

        # for getting input after the print statement
        user_input = input("")

        # checking the user_input
        if(user_input in choices):
            for i in range(len(stacks)):
                if (user_input == choices[i]):
                    return stacks[i]


# python3 -c 'import script; script.get_input()'

# Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
    print("\n\n"+"-"*70)
    print(f"Number of moves made = {num_user_moves}")
    print("\n...Current Stacks...\n")

    for i in stacks:
        i.print_items()
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
# If the user tried to move from an empty stack, that is an invalid move because there is nothing to move
        if(from_stack.is_empty()):
            print("\n\nInvalid Move. Try Again")
# If the user moves a disk to an empty stack or moves a disk onto a larger disk, that’s a valid move
        elif(to_stack.is_empty or from_stack.peek() < to_stack.peek()):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
# The only other case is if the user tries to move a larger disk onto a smaller disk.
        else:
            print("\n\nInvalid Move. Try Again")

print(
    f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}\n")
