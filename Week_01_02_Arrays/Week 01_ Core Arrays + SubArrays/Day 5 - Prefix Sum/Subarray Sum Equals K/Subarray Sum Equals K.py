"""https://leetcode.com/problems/subarray-sum-equals-k/description/"""

def countSubarraySumEqualsK(arr, K):
          hmap={}

          prefixSum=0
          res=0

          for i in range(arr,0):
            prefixSum+=arr[i]
           
           res+=hmap.get(arr[prefixSum-K],0)

           if(prefixSum==K):
            res+=1
     
           hmap[prefixSum]=hmap.get(arr[prefixSum],0)+1

    return res
   
   
