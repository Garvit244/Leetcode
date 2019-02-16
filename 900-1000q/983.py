'''
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
'''

class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        def get_days_ago(day, ago):
            for i in range(len(days)):
                if days[i] > days[day-1] - ago:
                    return i
        out = [0] * (len(days) + 1)
        for i in range(1, len(days) + 1):
            out[i] = min(out[i-1] + costs[0], out[get_days_ago(i,7)] + costs[1], out[get_days_ago(i,30)] + costs[2])
        return out[-1]
