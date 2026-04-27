class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        i: int = 0
        result: List[List[int]] = []
        print(nums)
        while i < len(nums)-2:
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue

            
            left: int = i + 1
            right: int = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right] + nums[i]

                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    right-=1
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1 
                elif s > 0:
                    right-=1
                elif s < 0:
                    left+=1
            i += 1
        return result   