"""

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


height = [1, 8, 3]


"""



def container(heights):
    start = 0
    end = len(heights) -1
    max_water = 0
    while start < end:
        calculate = min(heights[start], heights[end]) * (end-start)
        if calculate > max_water :
            max_water = calculate
        if heights[end] > heights[start]:
            start += 1
        else :
            end -= 1
    return max_water






print(container([1,8,6,2,5,4,8,3,7]))