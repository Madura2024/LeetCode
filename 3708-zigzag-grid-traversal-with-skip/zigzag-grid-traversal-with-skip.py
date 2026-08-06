class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        take=True

        for i in range(len(grid)):
            if i %2==0:
                for j in range(len(grid[0])):
                    if take:
                        ans.append(grid[i][j])
                    take=not take
            else:
                for j in range(len(grid[0])-1,-1,-1):
                    if take:
                        ans.append(grid[i][j])
                    take=not take
        return ans
            