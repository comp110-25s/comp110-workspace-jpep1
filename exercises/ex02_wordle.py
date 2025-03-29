"Program to Create Worlde"

__author__: str = "730574950"


def contains_char(search_string: str, target_char: str) -> bool:
    """
    Parameters:
    search_string (str): The string to search through.
    target_char (str): A single character to search for in the search string.
    Returns:
    bool: True if target_char is found in search_string, False otherwise.
    The function checks to see if the target character is present,
    within the search string.
    """

    assert len(target_char) == 1, f"len('{target_char}') is not 1"
    i = 0
    while i < len(search_string):
        if search_string[i] == target_char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Converts a guess into a string of emoji symbols,
    based on the similarity to the secret."""

    assert len(guess) == len(secret), "Guess must be same length as secret"

    WHITE_BOX = "\U00002B1C"
    GREEN_BOX = "\U0001F7E9"
    YELLOW_BOX = "\U0001F7E8"

    emoji_result = ""
    idx = 0

    while idx < len(guess):
        if guess[idx] == secret[idx]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        idx += 1

    return emoji_result


def input_guess(expected_length: int) -> str:
    """Indicates a guess of the expected length"""

    guess = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """Main game loop"""

    # State variables
    max_turns = 6
    turns_left = max_turns
    has_won = False
    current_turn = 1

    # Game loop
    while turns_left > 0 and not has_won:
        print(f"=== Turn {current_turn}/{max_turns} ===")

        # Retrieve the user's guess using the input_guess
        # Verify that it matches the length of the secret word
        guess = input_guess(len(secret))

        # Display the emoji result indicating the accuracy of the guess
        emoji_result = emojified(guess, secret)
        print(emoji_result)

        # Determine if the user has correctly guessed the word
        if guess == secret:
            has_won = True
        else:
            turns_left -= 1
            current_turn += 1

    # End Game
    if has_won:
        print(f"You won in {current_turn}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
