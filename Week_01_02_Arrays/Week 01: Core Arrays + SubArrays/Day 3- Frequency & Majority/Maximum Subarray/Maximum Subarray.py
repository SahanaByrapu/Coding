"""https://leetcode.com/problems/maximum-subarray/description/"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subsum=nums[0]
        maxsum=nums[0]

        for i in range(1,len(nums)):
             subsum=max(nums[i],subsum+nums[i])
             maxsum=max(maxsum,subsum)


        return maxsum


#SlidingWindow
#TimeComplexity : O(n)
#SpaceComplexity : O(1)


