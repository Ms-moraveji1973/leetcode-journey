"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

"""



def group_anagram(group:list):
    group_dict = {}
    for name in group:
        sorted_name = "".join(sorted(name))
        if sorted_name in group_dict:
            group_dict[sorted_name].append(name)
        else:
            group_dict[sorted_name] = [name]
    return list(group_dict.values())

print(group_anagram(["eat","tea","tan","ate","nat","bat"]))