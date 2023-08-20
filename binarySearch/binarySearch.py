def binarySearch(array: list, target: int) -> int:

    left, right = (0, len(array)-1) # два крайних значение

    while left <= right:

        mid = (left+right) // 2 # среднее значение

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            left = mid + 1 # смещаем край вправо, тк записанное значение больше

        else:
            right = mid - 1 # смещаем край влево, тк записанное значение меньше

    return -1 # нет такого значения в списке

# array = [2, 3, 5, 7, 8, 9]
# target = 8
#
# print(binarySearch(array, target))

import time

start = time.perf_counter()

array = list(range(100000000))
target = 988088

print(binarySearch(array, target))

print(time.perf_counter()-start)