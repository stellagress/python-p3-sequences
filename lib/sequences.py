#!/usr/bin/env python3

# def print_fibonacci(length):
#     ini_values = [0,1]

#     if length == 0:
#         ini_values=[]
#     elif length == 1:
#         ini_values=[0]
#     print(ini_values)




def print_fibonacci(length):
    ini_value = [0,1]

    if length == 0:
        ini_value = []
    elif length == 1:
        ini_value = [0]
    elif length > 2 :
        while len(ini_value) < length:
            ini_value.append(ini_value[-1] + ini_value[-2])
    print(ini_value)



      





