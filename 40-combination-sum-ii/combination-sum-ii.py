class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []

        def dfs(start, target, path):
            if target == 0:
                res.append(path)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break

                dfs(i + 1, target - candidates[i], path + [candidates[i]])

        dfs(0, target, [])
        return res