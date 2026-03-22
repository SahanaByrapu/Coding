"""https://www.geeksforgeeks.org/dsa/largest-subarray-with-equal-number-of-0s-and-1s/"""

def longestSubarrayWithEqualZerosandOnes(arr):

  hmap={}
  prefixsum=0
  maxlen=0

   
    for i in range(0,len(arr)):
        # if current element is zero, add -1
        prefixsum+=-1 if arr[i]==0 else 1

         # To handle sum = 0 at last index
        if prefixsum==0:
       		maxlen=i+1

        # If this sum is seen before, then update 
      	# result with maximum
        if prefixsum in hmap:
          maxlen=max(maxlen, i-arr[prefixsum])
        # Else put this sum in hash table
        else:
          hmap[prefixsum]=i
          
    return maxlen

if __name__ == "__main__":
    arr = [0]
    print(maxLen(arr))

    
