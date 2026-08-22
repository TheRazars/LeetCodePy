class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        num_islands = 0

        def set_zero_island(grid, r, c):
            if (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and grid[r][c] == "1":
                grid[r][c] = "0"
                for row_i, column_i in directions:
                    set_zero_island(grid, r + row_i, c + column_i)

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    num_islands += 1
                    set_zero_island(grid, row, column)
        return num_islands