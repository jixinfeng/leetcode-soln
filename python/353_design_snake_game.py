"""
Design a Snake game that is played on a device with screen size = width x
height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1
unit.

You are given a list of food's positions in row-column order. When a snake eats
the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will
not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear
on a block occupied by the snake.

Example:
Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that,
the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
"""
from collections import deque
class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snake = deque([(0, 0)])
        self.w, self.h = width, height
        self.food = list(map(tuple, food[::-1]))

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        head_x, head_y = self._next_head_loc(direction)
        if not self._is_valid_loc(head_x, head_y):
            return -1
        elif self.food and (head_x, head_y) == self.food[-1]:
            self.snake.appendleft((head_x, head_y))
            self.food.pop()
        else:
            self.snake.appendleft((head_x, head_y))
            _ = self.snake.pop()
        return len(self.snake) - 1

    def _next_head_loc(self, direction):
        assert len(self.snake) > 0
        if direction not in ['U', 'D', 'L', 'R']:
            raise ValueError("invalid direction")
        curr_x, curr_y = self.snake[0]
        if direction == 'U':
            return (curr_x - 1, curr_y)
        elif direction == 'D':
            return (curr_x + 1, curr_y)
        elif direction == 'L':
            return (curr_x, curr_y - 1)
        else:
            return (curr_x, curr_y + 1)

    def _is_valid_loc(self, x, y):
        return x >= 0 and y >= 0 and x < self.h and y < self.w \
                and ((x, y) not in self.snake or (x, y) == self.snake[-1])

# a = SnakeGame(3, 2, [[1,2],[0,1]])
# a.move('R')
# a.move('D')
# a.move('R')
# a.move('U')
# a.move('L')
# a.move('U')

a = SnakeGame(3, 3, [[2,0],[0,0],[0,2],[2,2]])
print(a.move('D'))
print(a.move('D'))
print(a.move('R'))
print(a.move('U'))
print(a.move('U'))
print(a.move('L'))
print(a.move('D'))
print(a.move('R'))
print(a.move('R'))
print(a.move('U'))
print(a.move('L'))
print(a.move('D'))
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
