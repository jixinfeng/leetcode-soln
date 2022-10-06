import pytest
from src.p003_longest_substring_without_repeating_characters import Solution


test_args = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3)
]


@pytest.mark.parametrize(argnames=["s", "expected_output"], argvalues=test_args)
def test_lengthOfLongestSubstring(s, expected_output):
    assert Solution().lengthOfLongestSubstring(s) == expected_output
