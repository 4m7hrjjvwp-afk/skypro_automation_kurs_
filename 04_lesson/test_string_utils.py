import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("spring", "Spring")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("123", "123")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


@pytest.mark.parametrize("input_str, expected", [
    (" spring", "spring")])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


def test_trim_negative():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


def test_contains_positive():
    assert string_utils.contains("Skypro", "S") is True


def test_contains_negative():
    assert string_utils.contains("", "S") is False


def test_delete_symbol_positive():
    assert string_utils.delete_symbol("SkyPro", "Pro"), "Sky"


def test_delete_symbol_negative():
    assert string_utils.delete_symbol("SkyPro", "p"), "SkyPro"
