#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list[0:x]:
            count += 1
            print("{:d}".format(i),end='')
        print()
        return count
    except Exception:
        pass
