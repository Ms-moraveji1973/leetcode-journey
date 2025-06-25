'''
[mohammad] => [mm] , [oamd] , [ha]
m = 1
o = 2
h = 3
a = 2
m = 1
m = 2
a = 3
d = 2
'''

def zigzag(array,number):
    if number == 1:
        return array
    a = number*['']
    index = 0
    pouse = -1
    for i in array:
        a[index] += i
        if index == 0 or index == (number-1) :
            pouse = -1 * pouse
        if pouse > 0 :
            index += 1
        elif pouse < 0 :
            index = index-1
    return a


print(zigzag('adasfasasd',5))