from array import array
from ctypes import Array
from typing import Tuple

def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    poczatek = 0
    koniec = len(ints)-1
    while poczatek <= koniec:
        middle = int((poczatek + koniec)/2)
        if numbers[middle] == value:
            return middle, True
            break
        elif numbers[middle] < value:
            poczatek = poczatek + 1
        elif numbers[middle]> value:
            koniec = koniec -1
    return False, -1

ints = array('I',[1,2,3,4,5,6,7])

print(binary_search(ints,7 ))
