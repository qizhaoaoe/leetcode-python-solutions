### 题目描述
n皇后问题研究的是如何将n个皇后放置在nxn的棋盘上，并且使皇后彼此之间不能相互攻击（要求一个皇后的对角线，水平和垂直方向不能有其他皇后）。

给定一个整数n, 返回所有不同的n皇后问题的解决方案。每一种接发包含一个明确的n皇后问题的棋子放置方案，该方案中‘Q’和'.' 分别代表了皇后和空位。

### 解决思路

这个题也是一个路径搜索问题，不断尝试，无路可走则回溯。由于要求放置的皇后之间不能相互攻击，因此棋盘的每一行都必须放置一个皇后，因此对于每个皇后，只要遍历每一行的n个位置。

时间复杂度，第一个皇后放置在第一行有n种选择，第二个皇后有(n-2)种选择...，因此放置n个皇后的选择有n*(n-2)*(n-4)*...1, 因此时间复杂度为O(n!)

另外，如何检测当前位置是否可以放置皇后？初始时，在放置一个皇后之后，我们可以设置该列，该皇后的主次对角线上的值无法访问。在一个位置上，主对角线满足row-col为常数，次对角线满足row+col为常数，因此可以设置三个数组，分别表示列，主对角线，次对角线的相应位置是否能访问。

因此借助的额外空间复杂度包括这些数组和递归栈占用的空间，递归到最后一行会返回，因此递归栈的空间复杂度为O(n)，总体的时间复杂度为O(n).

### 代码

```python
class Solution:
    
    def solveNQueens(self, n: int):
        output = []
        queens = set()
        colpos = [0] * n
        diagpos = [0] * (2*n-1)
        diagpos0 = [0] * (2*n-1)
        
        def couldplace(row, col):
            return not (colpos[col] + diagpos[row+col] + diagpos0[row-col])
        
        def placequeen(row, col):
            queens.add(col)
            colpos[col] = 1
            diagpos[row+col] = 1
            diagpos0[row-col] = 1
        
        def removequeen(row, col):
            queens.remove(col)
            colpos[col] = 0
            diagpos[row+col] = 0
            diagpos0[row-col] = 0
        
        def backtrack(row=1):
            for col in range(n):
                if couldplace(row, col):
                    placequeen(row, col)
                    if row+1 == n:
                         output.append(['.'*col+'Q'+(n-col-1)*'.' for col in sorted(queens)])
                    else:
                        backtrack(row+1)
                    remove_queen(row, col)
        backtrack()
        return output
```

注意：set是无顺序的，因此在最后加入output的时候需要根据row排序。
