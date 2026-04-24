import symbol

import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("spring", "Spring"),
    ("hello", "Hello"),
    ("test", "Test")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("123qwe", "123qwe"),
    ("", ""),
    ("   ", "   ")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


@pytest.mark.parametrize("input_str, expected", [
    (" spring", "spring"),
    (" hello", "hello"),
    (" test", "test")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


def test_trim_negative():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


@pytest.mark.parametrize("input_str, expected", [
    ("Spring", "S"),
    ("Hello", "H"),
    ("Test", "T")
])
def test_contains_positive(input_str, expected):
    assert string_utils.contains(input_str, expected) is True


@pytest.mark.parametrize("input_str, expected", [
    ("", "S"),
    ("Spring", "H"),
    ("1", "T")
])
def test_contains_negative(input_str, expected):
    assert string_utils.contains(input_str, expected) is False


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "Pro", "Sky"),
    ("hello world", "l", "heo word"),
    ("Test", "t", "Tes")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol), expected

@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "p", "SkyPro"),
    ("hello world", "W", "hello world"),
    ("test", " ", "test")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol), expected

