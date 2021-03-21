def did_some1_win(grid):
    '''
        takes an input as as a 3x3 list and returns the True if someone wins.
    '''
    for i in range(2):
        if (grid[i][0] == grid[i][1] == grid[i][2] == 'X') or \
           (grid[i][0] == grid[i][1] == grid[i][2] == 'O'):
            return True

    #did_some1_win all columns one by one
    for j in range(2):
        if (grid[0][j] == grid[1][j] == grid[2][j] == 'X') or \
           (grid[0][j] == grid[1][j] == grid[2][j] == 'O') :
            return True

    #did_some1_win major diagonal
    if (grid[0][0] == grid[1][1] == grid[2][2] == 'X') or \
       (grid[0][0] == grid[1][1] == grid[2][2] == 'O'):
        return True

    #did_some1_win minor diagonal
    if (grid[0][2] == grid[1][1] == grid[2][0] == 'X') or \
       (grid[0][2] == grid[1][1] == grid[2][0] == 'O'):
        return True

    #No Trio together
    return False

def alter(c):
    if c == 'O': c = 'X'
    else : c ='O'
    return c


def gen_grid(action_list):
    grid = [[None, None, None],  [None, None, None],  [None, None, None]]
    c = 'O'

    for v in action_list:
        x = int(v)%3
        y = int(v)//3
        grid[y][x] = c

        c = alter(c)

    return grid

def get_optimal_action_list(action_list):
    '''
        each permutation is reduced in such a way that if a game concludes before 9 moves. 
        the extra elements are removed.
    '''
    grid = [[None, None, None],  [None, None, None],  [None, None, None]]

    c = 'O'
    for v in action_list[:5]:
        x = int(v)%3
        y = int(v)//3
        grid[y][x] = c

        c = alter(c)

    if did_some1_win(grid):
        return action_list[:5]

    for i in range(5,9):
        v = int(action_list[i])
            
        x = v%3
        y = v//3

        grid[y][x] = c
        c = alter(c)

        if did_some1_win(grid):
            return action_list[:i+1]

    return action_list 

def get_action_list(filename):
    with open(filename) as InputFile:
        ways = map(list,InputFile.read().split('\n'))

    return ways

if __name__ == "__main__":
    reduced_list = [get_optimal_action_list(way) for way in get_action_list("./permute.txt")]
    for v in set("".join(action_list) for action_list in reduced_list):
        print(v)
