import os
from quicksort import *

def int_arr_from_file_names(arr):
    int_arr = []

    for item in arr:
        bfr_dot = item.split(".")

        if "/" in bfr_dot[0]:
            bfr_dot = bfr_dot.split("/")
            bfr_dot = bfr_dot[len(bfr_dot - 1)]

        int_from_substr = 0

        try:
            int_from_substr = int(bfr_dot[0])
            int_arr.append(int_from_substr)

        except:
            print(f"Expected int, got {bfr_dot[0]}")
            return -1

    return int_arr


def file_names_from_int_arr(arr, ext):
    str_arr = []

    for _int in arr:
        str_arr.append(f"{str(_int)}.{ext}")

    return str_arr

def get_files(src, ext):
    files = os.listdir(src)
    int_arr = int_arr_from_file_names(files)
    sort = quicksort(0, len(int_arr) - 1, int_arr)
    file_names = file_names_from_int_arr(sort, ext)

    return file_names
