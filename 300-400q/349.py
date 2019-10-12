'''
Given two arrays, write a function to compute their intersection.

Examples
--------
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
'''

class Solution:
  def intersection(self, arrA: List[int], arrB: List[int]) -> List[int]:
    
    arrA.sort()
    arrB.sort()

    intersection = []

    aIndex = 0
    bIndex = 0
    recentOverlap = None

    while aIndex < len(arrA) and bIndex < len(arrB):
      if arrA[aIndex] > arrB[bIndex]:
        bIndex += 1
      elif arrA[aIndex] == arrB[bIndex]:
        if arrB[bIndex] != recentOverlap: # skip duplicate overlapping elements
          recentOverlap = arrB[bIndex]
          intersection.append(recentOverlap)
        bIndex += 1 # you could increment aIndex instead
      else:
        # arrA[aIndex] < arrB[bIndex]
        aIndex += 1

    return intersection