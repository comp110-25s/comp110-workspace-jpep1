"Dictionary Test"

__author__: str = "730574950"

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


# Tests for invert
def test_invert_basic():
    """Test normal inversion of key-value pairs."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single_pair():
    """Test dictionary with a single key-value pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_duplicate_values():
    """Test inversion where duplicate values exist, which should raise a KeyError."""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


# Tests for count
def test_count_basic():
    """Test counting occurrences in a basic list."""
    assert count(["a", "b", "a", "c", "b", "b"]) == {"a": 2, "b": 3, "c": 1}


def test_count_single_element():
    """Test a list with a single repeating element."""
    assert count(["x", "x", "x"]) == {"x": 3}


def test_count_empty_list():
    """Test an empty list, which should return an empty dictionary."""
    assert count([]) == {}


# Tests for favorite_color
def test_favorite_color_basic():
    """Test finding the most frequent color."""
    assert favorite_color({"Alice": "blue", "Bob": "red", "Charlie": "blue"}) == "blue"


def test_favorite_color_tie():
    """Test tie-breaking (return first encountered)."""
    assert (
        favorite_color(
            {"Alice": "green", "Bob": "blue", "Charlie": "green", "Dave": "blue"}
        )
        == "green"
    )


def test_favorite_color_single_entry():
    """Test when there's only one person in the dictionary."""
    assert favorite_color({"Alice": "purple"}) == "purple"


# Tests for bin_len
def test_bin_len_basic():
    """Test binning words by length."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_repeated_words():
    """Test repeated words to ensure sets keep unique values."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_empty_list():
    """Test an empty list, which should return an empty dictionary."""
    assert bin_len([]) == {}
