"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""


def search_in_matrix(matx, trgt):
    for r_idx in range(len(matx)):
        c_idx = 0
        while c_idx < len(matx[0]) and matx[r_idx][c_idx] <= trgt :
            if matx[r_idx][c_idx] == trgt:
                return [r_idx, c_idx]
            c_idx +=1
    return [-1,-1]

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

print(search_in_matrix(matrix, target))

targets = [
    44,
    128,
    0,
    -1,
    1,
    1001,
    1000,
    1004,
]

for target in targets:
    print(search_in_matrix(matrix, target))

# Nice work! Can you think of a way to make it more efficient relying
# on the fact they're sorted?
# Lost 1 mark we'd like to see some extra tests (target/matrix)
