# question: https://leetcode.com/explore/featured/card/queue-stack/231/practical-application-queue/1374/

import queue
# about queue module: https://www.geeksforgeeks.org/stack-queue-python-using-module-queue/


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # if grid is empty
        if len(grid) == 0:
            return 0

        # store all nodes which are waiting to be processed
        q = queue.Queue()
        # width of the grid
        wid = len(grid[0])
        # length of the grid
        leng = len(grid)
        # store all the location of lands that haven't been processed
        lands = set()
        for l in range(leng):
            for w in range(wid):
                if grid[l][w] == '1':
                    lands.add((l*wid + w))

        # store the number of the islands
        islands = 0
        # flag of whether the lands set if empty
        flag = 1

        # BFS
        while len(lands):
            # initialize if the lands set is not empty
            if flag:
                ##
                q.put(lands.pop())
                islands += 1
                # only need to initialize for one time
                flag = 0

            # q is empty means no more land connect to the current land
            if q.empty():
                islands += 1
                # move the next first unprocessed land to the q
                q.put(lands.pop())
            
            size = q.qsize()
            for i in range(size):
                # get and remove the first land
                land_loc = q.get()
                # remove the lands that has been processed
                ## use discard method instead of remove because the first land has already been removed outside the while
                lands.discard(land_loc)
                # transform the location
                x = land_loc % wid
                y = land_loc // wid

                # check if the left is land
                ## `wid` not `wid - 1`
                if (x+1 < wid) and grid[y][x+1] == '1':
                    q.put(land_loc + 1)

                # check if the bottom is land
                if (y+1 < leng) and grid[y+1][x] == '1':
                    q.put(land_loc + wid)
                
                # check if the right is land
                if (x-1 >= 0) and grid[y][x-1] == '1' and (land_loc-1 in lands):
                    lands.discard(land_loc-1)
                    q.put(land_loc - 1)

                # check if the top is the land
                if (y-1 >= 0) and grid[y-1][x] == '1' and (land_loc-wid in lands):
                    lands.discard(land_loc-wid)
                    q.put(land_loc - wid)
        
        return islands

if __name__ == "__main__":
    a = Solution()

    #  num = a.numIslands([\
    # ["1","1","0","0","0"],\
    # ["1","1","0","0","0"],\
    # ["0","0","1","0","0"],\
    # ["0","0","0","1","1"]])

    # num = a.numIslands([\
    # ["1","1","1"],\
    # ["0","1","0"],\
    # ["1","1","1"]])

    num = a.numIslands([\
    ["1","0","1","1","1"],\
    ["1","0","1","0","1"],\
    ["1","1","1","0","1"]])
    print(num)