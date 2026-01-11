# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    prev_start, prev_end = intervals[0]
    intervals.append([float('inf'), float('inf')])
    res = []
    for start, end in intervals:
        if start <= prev_end:
            prev_end = max(prev_end, end)
        else:
            res.append([prev_start, prev_end])
            prev_start, prev_end = start, end
    return res

if __name__ == '__main__':
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))