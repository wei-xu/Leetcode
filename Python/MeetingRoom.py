# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x:x.start)
        prev = Interval()
        for interval in intervals:
            if interval.start < prev.end:
                return False
            prev = interval
        return True

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
    Interval(13, 15),
    Interval(1, 13),
]
# print s.canAttendMeetings(intervals)
# print s.canAttendMeetings(intervals2)
# print s.canAttendMeetings(intervals3)
print s.canAttendMeetings(intervals4)