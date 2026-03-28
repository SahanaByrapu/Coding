class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res=1
        prefixProd=1

        hmap={}

        for i in range(0,nums.length):
           prefixProd=max(prefixProd,prefixProd*nums[i])
           

