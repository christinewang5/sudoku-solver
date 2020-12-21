from pprint import pprint
import submission
import collections
import util


def create_sudoku_csp(board):
    """
    Input: board, an 9x9 grid, where (i,j) either equals to given value if 
        filled out or 0
    Output: csp, an instance of a Constraint Satisfaction Problem
    """
    csp = util.CSP()
    domain = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            csp.add_variable((i, j), domain)
            
    # add unary constraints
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                csp.add_unary_potential((i, j), lambda x: x == board[i][j])

    # add row constraint
    for i in range(9):
        for j1 in range(9):
            for j2 in range(j1 + 1, 9):
                csp.add_binary_potential((i, j1), (i, j2), lambda x, y: x != y)

    # add column constraint
    for j in range(9):
        for i1 in range(9):
            for i2 in range(i1 + 1, 9):
                csp.add_binary_potential((i1, j), (i2, j), lambda x, y: x != y)

    # add grid constraint
    for box1 in range(3):
        for box2 in range(3):
            # print(f'--- box {box1}, {box2} ---')
            box_pos = []
            for row in range(3*box1, 3*box1+3):
                for col in range(3*box2, 3*box2+3):
                    box_pos.append((row, col))
            for i in range(len(box_pos)):
                for j in range(i + 1, len(box_pos)):
                    # already row/col constraint
                    if (box_pos[i][0] == box_pos[j][0]) or (box_pos[i][1] == box_pos[j][1]):
                        continue
                    csp.add_binary_potential(
                        box_pos[i], box_pos[j], lambda x, y: x != y)
    return csp


# board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#          [6, 0, 0, 1, 9, 5, 0, 0, 0],
#          [0, 9, 8, 0, 0, 0, 0, 6, 0],
#          [8, 0, 0, 0, 6, 0, 0, 0, 3],
#          [4, 0, 0, 8, 0, 3, 0, 0, 1],
#          [7, 0, 0, 0, 2, 0, 0, 0, 6],
#          [0, 6, 0, 0, 0, 0, 2, 8, 0],
#          [0, 0, 0, 4, 1, 9, 0, 0, 5],
#          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

board = [[0, 1, 6, 3, 0, 8, 4, 2, 0], 
         [8, 4, 0, 0, 0, 7, 3, 0, 0], 
         [3, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 6, 0, 9, 4, 0, 8, 0, 2], 
         [0, 8, 1, 0, 3, 0, 7, 9, 0], 
         [9, 0, 3, 0, 7, 6, 0, 4, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 3], 
         [0, 0, 5, 7, 0, 0, 0, 6, 8], 
         [0, 7, 8, 1, 0, 3, 2, 5, 0]]

csp = create_sudoku_csp(board)
search = submission.BacktrackingSearch()
search.solve(csp, mcv=True, mac=True)
# print('--------- finished solve ---------')
print(search.optimalAssignment)
result = []
for i in range(9): 
    row = []
    for j in range(9):
        row.append(search.optimalAssignment[(i,j)])
    result.append(row)
pprint(result)

# houses = collections.defaultdict(list)
# for var, house in search.optimalAssignment.items():
#     houses[house].append(var)
# print(houses)
