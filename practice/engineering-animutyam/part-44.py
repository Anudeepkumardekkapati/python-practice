class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def fun(arr,k):

            ans=0
            l=0
            temp=0
            for r in range(len(arr)):
                if arr[r]%2==1:
                    temp=temp+1
                

                while(temp>k):

                    if arr[l]%2==1:
                        temp=temp-1
                    l=l+1
                # ans=max(ans,r-l+1)
                ans=ans+r-l+1
            return ans
        a=fun(nums,k)
        b=fun(nums,k-1)
        ans=a-b
        return ans


        