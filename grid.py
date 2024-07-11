
def make_grid(R,C):
    grid = []
    for i in range(R):
        line = []
        for j in range(C):
            line.append("0")
        grid.append(line)
    return grid

# no use of now
def check_bellow_char(GRID, cux ,cuy):
    if GRID[cuy][cux] != "0":    
        if cuy + 1 != len(GRID) and GRID[cuy + 1][cux] == GRID[cuy][cux]:
            check_bellow_char(GRID, cux,cuy + 1)
        if cuy + 1 == len(GRID) and  GRID[cuy - 1][cux] == GRID[cuy][cux]:
            return True


def check_win(GRID, playerchar):
    # vertical check
    for a in range(len(GRID[0])):
        k = []
        for b in range(len(GRID)):
            k.append(GRID[b][a])
        if k.count(playerchar) == len(k):
            return 1

    # diagonal check
    principalDiagonal = []
    diagonal2 = []
    for i in range(len(GRID)):

        for j in range(len(GRID[i])):
            if i == j:
                principalDiagonal.append(GRID[i][j])
            if i + j == len(GRID) - 1:
                diagonal2.append(GRID[i][j])
        
    if principalDiagonal.count(playerchar) == len(GRID) or diagonal2.count(playerchar) == len(GRID):
        return 1

    # horizontal check
    for i in GRID:
        if i.count(playerchar) == len(i):
            print("Count: ",i.count(playerchar))
            return 1
























"""    if len(GRID) != 1:
        for i in range(len(GRID[0])):
            if(GRID[0][i] != "0" and check_bellow_char(GRID, 0, i)):
                return True

 
                








    streakx = streaky = 0
    
    previous = GRID[0][0] 

    for i in range(0,len(GRID)):
        streakx = 0
        for j in range(0,len(GRID[i])):
            if GRID[i][j] != "0":
                if GRID[i][j] == previous:
                    if streakx == len(GRID[i]) - 1:
                        return True
                    else:
                        streakx += 1
                else:
                    streakx = 0
            previous = GRID[i][j]
                    """