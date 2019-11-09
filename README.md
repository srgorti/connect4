## connect4
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

### Sample usage and output

python connect4_v0.py.  
 0123456  
0ybrybby  
1rryryry   
2ryyryry   
3ybbbyyb  
4yybrbyb  
5rrbyrry  
  
Done with checking rows.  
Done with checking cols.  
Color=y, end_pos=(0, 3), dir=LR1-diag. 

Note: This program works directly on Python 2.7. To get it working on
      Python 3, the print statements have to be converted to function
      format.
