# 思路:
# - 遍历所有的坐标, 发现一个`1`, 就将与它相连的`1`都找出来, 把它(们)赋为`0`.
# - 然后总数加一, 继续遍历, 找下一个`1`
# - 直到遍历到最后一个
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 防止grid为空时, grid[0]报错
        if len(grid) == 0:
            return 0

        self.leng = len(grid)
        self.wid = len(grid[0])
        self.grid = grid

        count = 0

        for w in range(self.wid):
            for l in range(self.leng):
                if self.grid[l][w] == '1':
                    count += 1
                    self.countIsland(w, l)

        return count

    def countIsland(self, w, l):
        if(w < 0 or w >= self.wid or l < 0 or l >= self.leng or self.grid[l][w] == '0'):
            return
        self.grid[l][w] = '0'
        self.countIsland(w-1, l)
        self.countIsland(w+1, l)
        self.countIsland(w, l-1)
        self.countIsland(w, l+1)

if __name__ == "__main__":
    a = Solution()

    # num = a.numIslands([\
    # ["1","1","0","0","0"],\
    # ["1","1","0","0","0"],\
    # ["0","0","1","0","0"],\
    # ["0","0","0","1","1"]])

    # num = a.numIslands([\
    # ["1","1","1"],\
    # ["0","1","0"],\
    # ["1","1","1"]])

    # num = a.numIslands([\
    # ["1","0","1","1","1"],\
    # ["1","0","1","0","1"],\
    # ["1","1","1","0","1"]])

    num = a.numIslands([])

    print(num)