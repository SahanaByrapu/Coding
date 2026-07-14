"""https://www.geeksforgeeks.org/dsa/longest-sub-array-sum-k/"""

def longestSubarrayWithSumK(arr,k):

  hmap={}
  prefixsum=0
  maxlength=0
  for i in range(len(arr)):
      prefixsum=prefixsum+arr[i]
      if prefixsum not in hmp:
        hmp[prefixsum]=i
      elif prefixsum==k:
        maxlen=max(maxlen, i+1)
        
  return maxlen

#TimeComplexity: O(n)
#SpaceComplexity: O(1)
  
