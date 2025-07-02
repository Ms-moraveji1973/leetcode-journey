'''
awaawwvv  => 3 [awv]
مسیر حل مسئله:
- الگوریتم است از مرسوم ترین روش ها و تکنیک برای حل این مسئله استفاده از sliding windows
- حرف و ایندکسش رو در یک hashtable(dict) ذخیره میکنیم و وقتی به یک حرف تکراری رسیدیم اون ایندکس رو اپدیت میکنیم. و پنجره جدیدی رو با start باز میکنیم
- هر بار که پنجره جدیدی باز میکنیم میایم طول رشته رو ذخیره و با مقدار قبلیش مقایسه و بیشترین رو برمیگردونیم

'''

class Solution:
    def lengthOfLongestSubstring(s):
        start = 0
        s_index = {}
        max_length = 0
        for i in range(len(s)):
            if s[i] in s_index and s_index[s[i]] >= start:
                start = s_index[s[i]] + 1
            s_index[s[i]] = i
            max_length = max(max_length, i - start + 1)

        return max_length


# Example usage
b = Solution
print(b.lengthOfLongestSubstring('pwwkew'))
