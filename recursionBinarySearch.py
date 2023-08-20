def binarySearch(array: list, left: int, right: int, target: int) -> int:
    if left > right: # не существует такого значения
        return -1

    mid = (left+right) // 2 # среднее значение в массиве

    if array[mid] == target:
        return mid

    elif array[mid] < target:
        return binarySearch(array, mid+1, right, target) # смещение вправо от середины

    else:
        return binarySearch(array, left, mid-1, target)# смещение влево от середины

array = [2, 3, 5, 7, 8, 9]
target = 8

print(binarySearch(array, 0, len(array)-1, target))

array = [25, 33, 51, 75, 82, 93]
target = 18

print(binarySearch(array, 0, len(array)-1, target))