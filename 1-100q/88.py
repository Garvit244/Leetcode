class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(len(nums1)):
            if i >= m:
                nums1.pop()
        
        i = 0
        
        while nums2 and i < len(nums1):
            if nums2[0] <= nums1[i]:
                nums1.insert(i, nums2[0])
                nums2.pop(0)
            else:
                i += 1
            
        if nums2:
            nums1.extend(nums2)
