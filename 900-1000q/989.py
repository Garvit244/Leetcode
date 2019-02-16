'''
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

 

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
'''

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        arr_k = []
        while K >0:
            digit = K%10
            K /= 10
            arr_k.append(digit)
            
        arr_k.reverse()
        if len(arr_k) > len(A):
            A, arr_k = arr_k, A
        
        sum_arr = [0]*len(A)
        i, j = len(A)-1, len(arr_k)-1
        k = len(A) -1
        digit_sum, carry = 0, 0
        while j >= 0:
            curr_sum = A[i] + arr_k[j] + carry
            sum_arr[k] = (curr_sum%10)
            carry = curr_sum//10
            i -= 1
            k -= 1
            j -= 1
        
        while i >= 0:
            curr_sum = A[i] + carry
            sum_arr[k] = (curr_sum%10)
            carry =curr_sum//10
            i -= 1
            k -= 1
            
        if carry:
            sum_arr = [carry] + sum_arr
        return sum_arr        
