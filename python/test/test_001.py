import pytest
from src.p001_two_sum import Solution


test_args = [
        ([1, 2], 3, [0, 1]),
        ([2, 5, 5, 10], 10, [1, 2]),
        ([3, 2, 4], 6, [1, 2])
    ]


@pytest.mark.parametrize(argnames=["nums", "target", "expected_output"], argvalues=test_args)
def test_twoSum(nums, target, expected_output):
    assert Solution().twoSum(nums, target) == expected_output
