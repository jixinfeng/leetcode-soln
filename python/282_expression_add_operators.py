"""
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.



Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
Example 3:

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.


Constraints:

1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1
"""


# Time Limit Exceeded
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        return self.helper("", num, target, [])

    def helper(self, left, right, target, results):
        if (len(right) == 1 or (len(right) > 1 and not right.startswith('0'))) and eval(left + right) == target:
            results.append(left + right)

        for i in range(1, len(right)):
            right_left = right[:i]
            right_right = right[i:]
            if len(right_left) > 1 and right_left.startswith('0'):
                break
            for op in ['+', '-', '*']:
                results = self.helper(left + right_left + op, right_right, target, results)

        return results
