import random


def empty(input: str) -> bool:
    if input is None or input.strip() == "":
        return True
    else:
        return False

def roll_die(dice_quantity: int, die_face: int) -> int:
    """Roll the dice for the user

    Args:
        dice_quantity (int): The number of dice to roll
        die_face (int): The face of the die to roll

    Returns:
        list[int]: The list of dice rolls
    """

    # Roll the dice and store the result
    roll_total = 0
    for i in range(dice_quantity):
        roll_total += random.randint(1, die_face)

    return roll_total

def parse_dice_roll(roll: str) -> list[int]:
        # Add a 1 to the front of the roll if the roll starts with a 'd'
    if roll[0] == "d":
        roll = f"1{roll}"

    # Split user text into individual parts: 1d20 -> ["1", "20"]
    # Example invocation: 2d6, "3d6+2d8", "3d20+6"
        # [3d6, +, 2d8]
        # [2d6]
    roll_parts: list[str] = roll.split("+")

    # Go through each of the individual roll parts and parse them
    for part in roll_parts:
        # Split the part into individual parts: 1d20 -> ["1", "20"]
        # Example invocation: 2d6, 3d6, 3d20
        # [3, 6]
        # [3, 20]
        dice_roll: list[str] = part.split("d")

        # If the parsed component is not 2 (number of dice and die face), then the roll is invalid
        if len(dice_roll) != 2:
            return None
        
        # Activate the random Number Generator!
        roll_result = roll_die(int(dice_roll[0]), int(dice_roll[1])

def is_valid_roll(user_input: str) -> bool:
    """Determine if the user's input is a valid roll. A valid roll should contain the letter 'd' and be like "1d12"

    Args:
        user_input (str): The user's input

    Returns:
        bool: True if the user's input is a valid roll, False otherwise
    """

    # Check if the roll is empty
    if empty(user_input):
        return False

    # A valid text roll should contain the letter 'd'. E.g. 1d20 OR d20, 2d6, 3d8
    if "d" not in user_input.casefold():
        return False

    return True
