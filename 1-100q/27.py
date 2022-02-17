class Solution:
    def removeElement(self, nums, val):
        ret = 0
        i = 0
        
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
                nums.append(None)
            elif nums[i] == None:
                i += 1
            else:
                i += 1
                ret += 1
                
        return ret