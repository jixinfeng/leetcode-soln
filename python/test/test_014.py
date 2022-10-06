import pytest
from src.p014_longest_common_prefix import Solution


test_args = [(["leetcode"], "leetcode"), (["apps", "apple", "append"], "app")]


@pytest.mark.parametrize(argnames=["strs", "expected_output"], argvalues=test_args)
def test_longestCommonPrefix(strs, expected_output):
    assert Solution().longestCommonPrefix(strs) == expected_output
