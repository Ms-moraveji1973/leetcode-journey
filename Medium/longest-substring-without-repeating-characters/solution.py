'''
awaawwvv  => 3 [awv]
'''

class Solution:
    def lengthOfLongestSubstring(s):
        # This is the start index of the current substring without duplicates
        start = 0

        # Dictionary to save the last index where each character was seen
        s_index = {}

        # To store the maximum length found so far
        max_length = 0

        # Loop through each character in the string by index
        for i in range(len(s)):
            # If the character is already in the dictionary
            # and its index is inside the current window (after 'start')
            if s[i] in s_index and s_index[s[i]] >= start:
                # Move 'start' to the next index after the repeated character
                start = s_index[s[i]] + 1

            # Update the current character's latest index
            s_index[s[i]] = i

            # Calculate the current window size and update max_length if it's bigger
            max_length = max(max_length, i - start + 1)

        # Return the maximum length of substring without repeating characters
        return max_length


# Example usage
b = Solution
print(b.lengthOfLongestSubstring('pwwkew'))  # Output: 3
