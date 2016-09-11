# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        output = []
        if not intervals: return []
        prev = intervals[0]
        for interval in intervals:
            if interval.start <= prev.end:
                prev = Interval(min(prev.start, interval.start), max(prev.end, interval.end)) # merge
            else:
                output.append(prev)
                prev = interval
        output.append(prev)
        return output

