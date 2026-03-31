class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        rres=0
        maxsofar=nums[0]
        minsofar=nums[0]

        for i in range(1,len(nums)):
           
           maxsofar=max(maxsofar,maxsofar*nums[i])
           minsofar=min(minsofar, minsofar*nums[i])

           int tmp_max=Math.max(curr,Math.max(curr*max_so_far,curr*min_so_far));
           min_so_far=Math.min(curr,Math.min(curr*max_so_far,curr*min_so_far));

           max_so_far=tmp_max;
           res=Math.max(res,max_so_far);

           res= max(res, maxsofar)

        return res
