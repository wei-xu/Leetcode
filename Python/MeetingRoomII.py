# Definition for an interval.
import sys
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        num_room = 0
        num_avail = 0
        x = 0
        y = 0
        while x < len(starts):
            if starts[x] < ends[y]:
                if num_avail != 0:
                    num_avail -= 1
                else:
                    num_room += 1
                x += 1
            else:
                num_avail += 1
                y += 1
        return num_room


s = Solution()
intervals = [
    Interval(0, 30),
    Interval(5, 10),
    Interval(15, 20),
]
intervals2 = [
    Interval(0, 10),
    Interval(10, 20),
    Interval(20, 30),
]
intervals3 = [
    Interval(0, 10),
    Interval(5, 20),
    Interval(20, 30),
]
intervals4 = [
    Interval(9, 10),
    Interval(4, 9),
    Interval(4, 17),

]
print s.minMeetingRooms(intervals)
print s.minMeetingRooms(intervals2)
print s.minMeetingRooms(intervals3)
print s.minMeetingRooms(intervals4)