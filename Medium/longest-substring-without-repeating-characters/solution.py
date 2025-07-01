'''
awaawwvv  => 3 [awv]
'''

class Solution :
    def lengthOfLongestSubstring(s):
        start = 0
        s_index = {}
        max_length = 0
        for i in range(len(s)):
            if s[i] in s_index and s_index[s[i]]>=start:
                print('--------',s_index[s[i]])
                start = s_index[s[i]] + 1
            s_index[s[i]] = i
            max_length = max(max_length,i-start+1)
        return max_length
b = Solution
print(b.lengthOfLongestSubstring('pwwkew'))