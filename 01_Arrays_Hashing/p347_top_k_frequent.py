# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
from typing import List
from collections import Counter

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    table = {}
    for k,v in freq.items():
        table[v] = table.setdefault(v, {}).append(k)
    table.sort(lambda x: x[v], reverse=True)
    return list(table.values())[:k]
