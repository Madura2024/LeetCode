class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bs(left):

            l=0
            r=len(nums)-1
            ans=-1

            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                  ans=m
                  if left:
                    r=m-1
                  else:
                    l=m+1
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return ans

        return[bs(True),bs(False)]








        
