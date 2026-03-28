"""https://www.geeksforgeeks.org/dsa/count-number-subarrays-given-xor/"""

def countSubarrayXOR(arr,k):

  prefixsum=0
  hmap={}

  count=0

  for i in range(0,arr.length):
    prefisum^=arr[i]

    res+=hmap.get(arr[prefsum^k],0)
      
    if(prefixsum==k):
      res+=1

    hmap[prefixsum]=hmap.get(hmap[prefisum],0)+1


  return res
   



