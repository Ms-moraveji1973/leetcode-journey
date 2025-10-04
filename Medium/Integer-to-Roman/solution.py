'''

I:1
V:5
X:10
L:50
C:100
D:500
M:1000

'''

def integer_to_roman(num:int):
    place_values = {}
    number_str = str(num)
    count = 1
    result = []
    for i in range(len(number_str)-1,-1,-1):
        number_digits = number_str[i]
        place_values[count] = int(number_digits) * count
        count *= 10
    print('place_values',place_values)

    if 1000 in place_values.keys():
        number_1 = place_values[1000]
        if number_1 >= 1000 and number_1 <= 3000 :
            count_of_roman_1 = number_1 // 1000
            result.append('M' * count_of_roman_1)


    if 100 in place_values.keys():
        number_2 = place_values[100]
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


    if 10 in place_values.keys():
        number_3 = place_values[10]
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

    if 1 in place_values.keys():
        number_4 = place_values[1]
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

