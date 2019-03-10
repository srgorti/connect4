import pprint
import random
import sys

# One way to implement checking for connect4 winning
# position. It uses Python's generators to cleanly
# separate slice creation from slice checking.

def fill_colors(b, rows, cols, c1, c2):
    colors = [ 'b', c1, c2, 'b']
    for r in reversed(range(rows)):
        for c in reversed(range(cols)):
            b[r][c] = colors[random.randrange(0, 3)]
            
def make_board(rows, cols, c1, c2):
    b = list()
    for c in range(rows):
        b.append([ 'b' ] * cols)
    fill_colors(b, rows, cols, c1, c2)
    # TODO: validate board
    return b

def compare_element(current, running, running_count):
    if current != running:
        return current, 1
    else:
        return running, running_count + 1

# check for four-consecutive of a color
# the actual slice of consecutive elements
# are obtained by calling the generator.
def is_four_connected_itr(gen_func, board, loc):
    c, count = None, 0
    for t in gen_func(board, loc):
        v = t[0]
        c, count = compare_element(v, c, count)
        if count == 4 and c != 'b':
            #print t
            return t

    return False
    
def row_walker(board, row):
    cols = len(board[0])
    for c in range(cols):
        yield (board[row][c], (row, c,),)

def col_walker(board, col):
    rows = len(board)
    for r in range(rows):
        yield (board[r][col], (r, col,),)
    
def diag_lr1_walker(board, row):
    cols = len(board[0])
    for c in range(cols):
        yield (board[row][c], (row, c,),)
        row -= 1
        if row < 0:
            break
    
def diag_lr2_walker(board, col):
    rows = len(board)
    cols = len(board[0])
    for r in reversed(range(rows)):
        yield (board[r][col], (r, col,),)
        col += 1
        if col >= cols:
            break
        
def diag_rl1_walker(board, row):
    cols = len(board[0])
    for c in reversed(range(cols)):
        yield (board[row][c], (row, c,),)
        row -= 1
        if row < 0:
            break

def diag_rl2_walker(board, col):
    rows = len(board)
    for r in reversed(range(rows)):
        yield (board[r][col], (r, col,),)
        col -= 1
        if col < 0:
            break

def walk_and_check(board, walker_descr, walker_fn, n_times):
    found4 = filter(None, 
                    map(lambda x: is_four_connected_itr(walker_fn, board, x),
                        range(n_times)))
    if found4:
        return (found4[0][0], found4[0][1], walker_descr)
    print 'Done with checking %s' % (walker_descr)
    return False
       
def find_connected_four(board):
    rows = len(board)
    cols = len(board[0])
    all_walkers = [
        ('rows', row_walker, rows),
        ('cols', col_walker, cols),
        ('LR1-diag', diag_lr1_walker, rows),
        ('RL1-diag', diag_rl1_walker, rows),
        ('LR2-diag', diag_lr2_walker, cols),
        ('RL2-diag', diag_rl2_walker, cols),
    ]
    for descr, fn, count in all_walkers:
        res = walk_and_check(board, descr, fn, count)
        if res:
            return res

    return (None, (-1, -1,), '')

def print_board(board):
    sys.stdout.write(' ')
    for k in range(len(board[0])):
        sys.stdout.write(chr(k % 10 + ord('0')))
    print ' '
    for i, r in enumerate(board):
        sys.stdout.write(chr(i % 10 + ord('0')))
        for color in r:
            sys.stdout.write(color)
            #print '%c' % (color),
        print ' '
    print ''

def main():
    board = make_board(6, 7, 'r', 'y')
    print_board(board)
    c, pos, descr = find_connected_four(board)
    if c:
        print 'Color=%s, end_pos=%s, dir=%s' % (c, pos, descr)
    else:
        print 'Failed to find 4-connected'

if __name__ == '__main__':
    main()
