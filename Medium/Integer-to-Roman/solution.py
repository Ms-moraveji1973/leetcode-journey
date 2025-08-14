'''

I:1
V:5
X:10
L:50
C:100
D:500
M:1000

'''

def integer_to_roman(number:int):
    digits = {}
    number_str = str(number)
    count = 1
    result = []
    for i in range(len(number_str)-1,-1,-1):
        number_digits = number_str[i]
        digits[count] = int(number_digits) * count
        count *= 10
    print('digits',digits)

    if 1000 in digits.keys():
        number_1 = digits[1000]
        if number_1 >= 1000 and number_1 <= 3000 :
            count_of_roman_1 = number_1 // 1000
            result.append('M' * count_of_roman_1)


    if 100 in digits.keys():
        number_2 = digits[100]
        if number_2 >= 100 and number_2 <= 900 :
            if number_2 == 400 :
                result.append('C')
                result.append('D')
            elif number_2 == 900 :
                result.append('C')
                result.append('M')

            else :
                if number_2 >= 500 :
                    count_of_roman_2 = (number_2 - 500 ) // 100
                    result.append('D')
                    result.append('C'*count_of_roman_2)
                else :
                    count_of_roman_2 = number_2 // 100
                    result.append('C'*count_of_roman_2)


    if 10 in digits.keys():
        number_3 = digits[10]
        if number_3 >= 10 and number_3 <= 90 :
            if number_3 == 40 :
                result.append('X')
                result.append('L')

            elif number_3 == 90 :
                result.append('X')
                result.append('C')

            else :
                if number_3 >= 50 :
                    count_of_roman_3 = (number_3-50) // 10
                    result.append('L')
                    result.append('X'*count_of_roman_3)
                else :
                    count_of_roman_3 = number_3 // 10
                    print(count_of_roman_3)
                    result.append('X'*count_of_roman_3)

    if 1 in digits.keys():
        number_4 = digits[1]
        if number_4 >= 1 and number_4 <= 9 :

            if number_4 == 4 :
                count_of_roman_4 = number_4 // 1
                result.append('I')
                result.append('V')

            elif number_4 == 9 :
                result.append('I')
                result.append('X')
            else :
                if number_4 >= 5 :
                    count_of_roman_4 = (number_4-5) // 1
                    result.append('V')
                    result.append('I'*count_of_roman_4)

                else :
                    count_of_roman_4 = number_4 // 1
                    result.append('I'*count_of_roman_4)

    return "".join(result)

print(integer_to_roman(1994))

