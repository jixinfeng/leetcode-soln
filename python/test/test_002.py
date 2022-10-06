import pytest
from singlyLinkedList import *
from src.p002_add_two_numbers import Solution


test_args = [(
    singlyLinkedList([2, 4, 3]).head,
    singlyLinkedList([5, 6, 4]).head,
    singlyLinkedList([7, 0, 8]).head,
)]


@pytest.mark.parametrize(argnames=["l1", "l2", "expected_output"], argvalues=test_args)
def test_addTwoNumbers(l1, l2, expected_output):
    result = Solution().addTwoNumbers(l1, l2)
    assert result.val == expected_output.val
    while result.next and expected_output.next:
        result = result.next
        expected_output = expected_output.next
        assert result.val == expected_output.val
    assert not result.next and not expected_output.next
