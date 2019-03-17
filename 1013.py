'''
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
'''

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        count_arr = [0]*60
        result = 0
        for t in time:
            remainder = t%60
            complement = (60-remainder)%60
            result += count_arr[complement]
            count_arr[remainder] += 1
        return result
 
 '''
	Explanation: 
	Q1: why create array of size 60? 
		it is similar to the map which store the count. Why only 60 because 60 modulo of number cannot be more than 60
	Q2: why we need complement?
		to check the pair if it exisit with given value or not example: if remainder is 20 then we need to check if we have any number with remainder 40 or not.
	Q3: why 60 modulo complement?
		for handle cause when remainder is zero 
 '''