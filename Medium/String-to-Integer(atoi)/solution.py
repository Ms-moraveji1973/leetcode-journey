

def myAtoi(s: str) -> int:
    if len(s) == 0 :
        return 0
    MAX = 2**31 - 1
    MIN = -2**31
    result = ''
    numbers = '1234567890'
    to_strip = s.strip()
    is_negative = False

    if to_strip:
        if to_strip[0] == '-':
            is_negative = True
            to_strip = to_strip[1:]
        elif to_strip[0] == '+':
            is_negative = False
            to_strip = to_strip[1:]
            print(to_strip)

    for i in range(len(to_strip)):
        if to_strip[i] in numbers:
            result += to_strip[i]
        elif to_strip[i] not in numbers:
            break

    if result:
        result = int(result)
        if is_negative is True:
            result *= -1
        if result > MAX :
            final_result = MAX
        elif result < MIN :
            final_result = MIN
        else :
            final_result = result
    else :
        final_result = 0

    return final_result




print(myAtoi(" ++1"))