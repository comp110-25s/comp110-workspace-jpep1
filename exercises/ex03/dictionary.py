"Dictionary"

__author__: str = "730574950"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values. Raises KeyError if duplicate values exist."""
    inverted_dict: dict[str, str] = dict()
    # Initialize an empty dictionary for the inverted key-value pairs
    for key in input_dict:
        value: str = input_dict[key]  # Get the value for the current key
        if value in inverted_dict:  # If the value exists, raise a KeyError
            raise KeyError
        else:
            inverted_dict[value] = key  # Add the value as key and the key as the value
    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    """Counts occurrences and returns a dictionary of frequencies."""
    result: dict[str, int] = (
        dict()
    )  # Initialize an empty dictionary to store item frequencies
    for item in input_list:
        if (
            item in result
        ):  # If the item is already in the dictionary, increment its count
            result[item] += 1
        else:  # If the item is not in the dictionary, set its count to 1
            result[item] = 1
    return result


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Finds most frequent color from dictionary."""
    color_counts: dict[str, int] = dict()
    # Loop through each name in the input dictionary
    for (
        color
    ) in (
        names_and_colors.values()
    ):  # Get the favorite color (value) for each name (key)
        if (
            color in color_counts
        ):  # If the color is already in the dictionary, increment its count
            color_counts[color] += 1
        else:  # If the color is not in the dictionary, add it with a count of 1
            color_counts[color] = 1

    # Find the most frequent color
    most_frequent_color: str = ""
    max_count: int = 0

    for color, count in color_counts.items():  # Loop through the color counts
        if (
            count > max_count
        ):  # If the current color has a higher count, update the result
            most_frequent_color = color
            max_count = count

    return most_frequent_color


def bin_len(input_list: list[str]) -> dict[int, set[str]]:
    """Bins a list of strings by their lengths into a dictionary."""
    result: dict[int, set[str]] = (
        {}
    )  # Initialize an empty dictionary for the bin lengths

    for word in input_list:
        word_len: int = len(word)  # Get the length of the current word

        # If the length is not already a key, create a new set for that length
        if word_len not in result:
            result[word_len] = {word}
        else:
            # If the length exists, add the word to the corresponding set
            result[word_len].add(word)

    return result
