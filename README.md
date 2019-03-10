# connect4
Simple solution for checking if a given connect4 game position represents a winning position.

The connect-4 game (https://en.wikipedia.org/wiki/Connect_Four) is a
two-player game. The problem selected here is to check if a given
board position represents a winning position, which has been
implemented with a Python program. While it is a fairly straightforward
problem to solve, I ran into difficulties in separating the
slice creation from slice checking until I recalled Python's
generator construct. Using generators made the code much cleaner than
what it was before. Hence, this program serves mostly as an
example of how to use Python generators.

