
# brute force approach
def palindromic(s:str):
    result = ""
    longest = ""
    for i in range(len(s)):
        for j in range(i,len(s)):
            result = s[i:j+1]
            if result == result[::-1] :
                if len(result) > len(longest) :
                    longest = result

    return longest
print(palindromic('cbbd'))

