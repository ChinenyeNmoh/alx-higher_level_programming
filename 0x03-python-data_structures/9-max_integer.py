#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxm = my_list[0]
    for i in my_list:
        if maxm < i:
            maxm = i
            i +=1
    return maxm
