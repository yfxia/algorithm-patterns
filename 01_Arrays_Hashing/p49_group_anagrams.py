# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Input: strs = [""]
# Output: [[""]]

def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = get_key(s)
        groups.setdefault(key, []).append(s)
    return list(groups.values())

def get_key(s):
    index = [0] * 26
    for ch in s:
        index[ord(ch) - ord("a")] += 1
    return tuple(index)


if __name__ == "__main__":
    print(group_anagrams([]))
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))