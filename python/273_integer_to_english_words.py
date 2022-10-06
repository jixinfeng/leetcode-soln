"""
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


Constraints:

0 <= num <= 2^31 - 1
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        number_dict = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        ty_dict = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        large_number_dict = {
            10 ** 3: 'Thousand',
            10 ** 6: 'Million',
            10 ** 9: 'Billion'
        }
        words = []

        coef_b, num_m = divmod(num, 10 ** 9)
        if coef_b:
            words.append(number_dict[coef_b])
            words.append('Billion')

        coef_m, num_k = divmod(num_m, 10 ** 6)
        if coef_m:
            coef_h, num_t = divmod(coef_m, 100)
            if coef_h:
                words.append(number_dict[coef_h])
                words.append('Hundred')
            if num_t == 0:
                pass
            elif num_t < 20:
                words.append(number_dict[num_t])
            else:
                coef_t, num_d = divmod(num_t, 10)
                if coef_t:
                    words.append(ty_dict[coef_t])
                if num_d:
                    words.append(number_dict[num_d])

            words.append('Million')

        coef_k, num_h = divmod(num_k, 10 ** 3)
        if coef_k:
            coef_h, num_t = divmod(coef_k, 100)
            if coef_h:
                words.append(number_dict[coef_h])
                words.append('Hundred')
            if num_t == 0:
                pass
            elif num_t < 20:
                words.append(number_dict[num_t])
            else:
                coef_t, num_d = divmod(num_t, 10)
                if coef_t:
                    words.append(ty_dict[coef_t])
                if num_d:
                    words.append(number_dict[num_d])

            words.append('Thousand')

        if num_h:
            coef_h, num_t = divmod(num_h, 100)
            if coef_h:
                words.append(number_dict[coef_h])
                words.append('Hundred')
            if num_t == 0:
                pass
            elif num_t < 20:
                words.append(number_dict[num_t])
            else:
                coef_t, num_d = divmod(num_t, 10)
                if coef_t:
                    words.append(ty_dict[coef_t])
                if num_d:
                    words.append(number_dict[num_d])

        return ' '.join(words)
