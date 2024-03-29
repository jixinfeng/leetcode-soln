"""
You are playing the following Bulls and Cows game with your friend: You write
down a number and ask your friend to guess what the number is. Each time your
friend makes a guess, you provide a hint that indicates how many digits in said
guess match your secret number exactly in both digit and position (called
"bulls") and how many digits match the secret number but locate in the wrong
position (called "cows"). Your friend will use successive guesses and hints to
eventually derive the secret number.

For example:

    Secret number:  "1807"
    Friend's guess: "7810"
    Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
    Write a function to return a hint according to the secret number and
    friend's guess, use A to indicate the bulls and B to indicate the cows. In
    the above example, your function should return "1A3B".

    Please note that both secret number and friend's guess may contain duplicate
    digits, for example:

    Secret number:  "1123"
    Friend's guess: "0111"
    In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is
    a cow, and your function should return "1A1B".
    You may assume that the secret number and your friend's guess only
    contain digits, and their lengths are always equal.

Credits:
    Special thanks to @jeantimex for adding this problem and creating
    all test cases.
"""
import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        correct_locations = set(
            [i for i in range(len(secret)) if secret[i] == guess[i]])
        remaining_secret_count = collections.Counter(
            [secret[i] for i in range(len(secret)) if i not in correct_locations])
        remaining_guess_count = collections.Counter(
            [guess[i] for i in range(len(guess)) if i not in correct_locations])
        num_cows = 0
        for k, v in remaining_secret_count.items():
            guess_count = remaining_guess_count.get(k, 0)
            num_cows += min(v, guess_count)

        num_bulls = len(correct_locations)
        return f"{num_bulls}A{num_cows}B"


"""
faster and much faster version from
http://bookshadow.com/weblog/2015/10/31/leetcode-bulls-and-cows/

class Solution(object):
    def getHint(self, secret, guess):
        bull = sum(map(operator.eq, secret, guess))
        sa = collections.Counter(secret)
        sb = collections.Counter(guess)
        cow = sum((sa & sb).values()) - bull
        return str(bull) + 'A' + str(cow) + 'B'

class Solution(object):
    def getHint(self, secret, guess):
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
        return '%dA%dB' % (bulls, both - bulls)
"""
