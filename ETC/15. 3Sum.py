class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = len(nums)
        nums.sort()
        ans = []
        for i in range(a-2):
            j,k = i+1, a-1
            while j < k:
                val = nums[j] + nums[k]
                if val == (0 - nums[i]):
                    if [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    k -=1
                    j +=1
                elif val > (0-nums[i]):
                    k -=1
                else:
                    j +=1
        return ans
                
        
        
        
        
